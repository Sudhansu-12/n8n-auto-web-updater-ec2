import os
import json
from datetime import datetime
from typing import Dict, List, Any
import requests
from openai import OpenAI

class TrendAnalyzer:
    """Analyzes and ranks trends from multiple social platforms."""
    
    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.x_headers = {
            "Authorization": f"Bearer {os.getenv('X_BEARER_TOKEN')}"
        }
    
    def fetch_x_trends(self, woeid: int = 1) -> List[Dict]:
        """Fetch trending topics from X API."""
        url = f"https://api.x.com/2/trends/place.json?id={woeid}"
        try:
            response = requests.get(url, headers=self.x_headers)
            if response.status_code == 200:
                trends_data = response.json()
                trends = []
                for item in trends_data[0]['trends']:
                    trends.append({
                        'keyword': item['name'],
                        'source': 'x',
                        'volume': item.get('tweet_volume', 0),
                        'url': item['url'],
                        'timestamp': datetime.now().isoformat()
                    })
                return trends
        except Exception as e:
            print(f"Error fetching X trends: {e}")
        return []
    
    def fetch_reddit_trends(self, subreddits: List[str] = None) -> List[Dict]:
        """Fetch trending posts from Reddit."""
        if not subreddits:
            subreddits = ['all', 'worldnews', 'technology', 'funny']
        
        trends = []
        for subreddit in subreddits:
            try:
                url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                headers = {'User-Agent': 'TrendBot/1.0'}
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    posts = response.json()['data']['children']
                    for post in posts[:5]:
                        post_data = post['data']
                        trends.append({
                            'keyword': post_data['title'],
                            'source': 'reddit',
                            'volume': post_data['score'],
                            'comments': post_data['num_comments'],
                            'url': f"https://reddit.com{post_data['permalink']}",
                            'timestamp': datetime.now().isoformat()
                        })
            except Exception as e:
                print(f"Error fetching Reddit trends from r/{subreddit}: {e}")
        
        return trends
    
    def score_trend(self, trend: Dict) -> float:
        """Score a trend based on multiple factors."""
        volume = trend.get('volume', 0)
        comments = trend.get('comments', 0)
        engagement = trend.get('engagement', 0)
        
        # Normalize scores
        volume_score = min(volume / 100000, 1.0) * 0.4
        engagement_score = min(engagement / 10000, 1.0) * 0.35
        comments_score = min(comments / 5000, 1.0) * 0.25
        
        total_score = (volume_score + engagement_score + comments_score) * 10
        return min(total_score, 10.0)
    
    def rank_trends(self, trends: List[Dict]) -> List[Dict]:
        """Rank trends by score."""
        for trend in trends:
            trend['score'] = self.score_trend(trend)
        
        return sorted(trends, key=lambda x: x['score'], reverse=True)
    
    def generate_theme_with_ai(self, trend: Dict) -> Dict:
        """Use GPT to generate theme and content for a trend."""
        prompt = f"""
You are a creative AI designer and copywriter specializing in trend-driven web design.
Given the following trending topic, generate a complete website theme transformation in JSON format.

Trending Topic: {trend['keyword']}
Trend Score: {trend['score']:.1f}/10
Source: {trend['source']}
Engagement Level: {trend.get('volume', 0)}

Respond ONLY with valid JSON (no markdown, no extra text):
{{
  "theme": {{
    "primary_color": "#HEX",
    "secondary_color": "#HEX",
    "accent_color": "#HEX",
    "mood": "one word mood",
    "style": "one word style"
  }},
  "content": {{
    "headline": "Main headline",
    "subheading": "Supporting text",
    "cta_text": "Call to action",
    "body_summary": "2-3 sentences about why this trend matters"
  }},
  "imagery": {{
    "keywords": ["keyword1", "keyword2", "keyword3"],
    "style": "photography style description"
  }},
  "layout": {{
    "hero_style": "layout type",
    "animation_level": "none|subtle|moderate|heavy"
  }}
}}
"""
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a creative AI designer. Respond only with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=1500
            )
            
            response_text = response.choices[0].message.content.strip()
            theme = json.loads(response_text)
            return theme
        except Exception as e:
            print(f"Error generating theme with AI: {e}")
            return {}


if __name__ == "__main__":
    analyzer = TrendAnalyzer()
    
    # Fetch trends
    x_trends = analyzer.fetch_x_trends()
    reddit_trends = analyzer.fetch_reddit_trends()
    all_trends = x_trends + reddit_trends
    
    # Rank trends
    ranked = analyzer.rank_trends(all_trends)
    
    # Get top trend
    if ranked:
        top_trend = ranked[0]
        print(f"Top Trend: {top_trend['keyword']}")
        print(f"Score: {top_trend['score']:.2f}")
        
        # Generate theme
        theme = analyzer.generate_theme_with_ai(top_trend)
        print(f"Generated Theme: {json.dumps(theme, indent=2)}")
