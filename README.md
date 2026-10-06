# n8n-auto-web-updater-ec2

An AI-powered endless automation loop that monitors real-time social trends (X, Instagram, Facebook, Reddit, TikTok, YouTube) and automatically transforms your entire website theme, design, and content to match what's currently trending in society.

## The Vision: Infinite AI Loop

**Your website is never static.** Every 15-60 minutes:

1. Social APIs report the hottest trends globally
2. AI analyzes which trend is the strongest
3. AI generates new homepage content, copy, and visual themes
4. AI picks color schemes, imagery suggestions, and messaging
5. Website automatically rebuilds with the new trend as its theme
6. The cycle repeats endlessly

Your site becomes a **living, breathing entity** that always reflects what the internet is talking about **right now**.

## Key Features

✅ **Endless AI Loop**: No human intervention required  
✅ **Real-time Trend Detection**: X, Instagram, Facebook, Reddit, TikTok, YouTube, Google Trends  
✅ **Automatic Theme Generation**: AI creates color palettes, typography, and design guidance  
✅ **Dynamic Content Creation**: Headlines, body copy, CTAs, and visual descriptions auto-generated  
✅ **Website Auto-Update**: Git push, CMS API, or webhook deployment  
✅ **Trend History**: Track what trends drove engagement over time  
✅ **Self-Healing**: Detects failed updates and retries  
✅ **Production Safe**: Content review and moderation gates included  

## How the infinite loop works

```
┌─────────────────────────────────────────────────────────┐
│                     INFINITE CYCLE                       │
└─────────────────────────────────────────────────────────┘
                            ↓
        [Trigger: Every 15-60 minutes]
                            ↓
    [Fetch Live Trends from Social Platforms]
    • X (top tweets, hashtags, conversations)
    • Instagram (Reels, Stories, creator content)
    • Facebook (viral posts, groups, pages)
    • Reddit (hot posts, trending subreddits)
    • TikTok (trending sounds, challenges)
    • YouTube (trending videos, categories)
    • Google Trends (search velocity)
                            ↓
          [AI Trend Analysis & Ranking]
    • Score by: volume, velocity, engagement, sentiment
    • Filter duplicates and stale trends
    • Pick top 3-5 trends per cycle
                            ↓
        [AI Theme Generation for Each Trend]
    • Color palette (hex codes)
    • Typography recommendations
    • Imagery keywords and style
    • Emotional tone and messaging
    • Visual metaphor or brand angle
                            ↓
         [AI Content Generation]
    • Homepage hero headline
    • Subheading and value proposition
    • Feature cards (why this trend matters)
    • CTA buttons and micro-copy
    • Meta descriptions and SEO tags
    • Blog post ideas or articles
                            ↓
          [AI Visual Asset Suggestions]
    • Recommended image search terms
    • Photography style (filter, lighting, mood)
    • Icon pack recommendations
    • Layout suggestions
                            ↓
         [Build & Store Website Config]
    • Generate JSON theme file
    • Create HTML/JSX components
    • Generate CSS variables
    • Store in database or Git
                            ↓
           [Deploy to Live Website]
    • Git commit & push
    • Trigger CI/CD pipeline
    • Update CMS or API endpoint
    • Notify Slack/Discord
                            ↓
         [Track Metrics & Update Loop]
    • Store trend data (engagement, clicks, time online)
    • Log what worked, what didn't
    • Adjust scoring algorithm
    • Sleep X minutes, then repeat
                            ↓
                    [Loop Forever]
```

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      EC2 Instance                            │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              n8n Workflow Engine                      │  │
│  │  (Runs on Docker, starts loops every 15-60 min)     │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│          ┌────────────────┼────────────────┐               │
│          ↓                ↓                ↓               │
│  [Trend Fetcher]   [AI Engine]      [Deployer]             │
│  (APIs & feeds)    (OpenAI GPT)     (Git/CMS/Webhook)     │
│          │                ↓                ↓               │
│          └────────────────┼────────────────┘               │
│                           ↓                                  │
│               ┌───────────────────────┐                    │
│               │  PostgreSQL / Supabase│                    │
│               │  (Trend History DB)   │                    │
│               └───────────────────────┘                    │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              Your Live Website / CMS                         │
│  (Always showing the current #1 trending theme)             │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Design Theme: AI-generated color, fonts, layout    │   │
│  │  Content: AI-generated copy based on trend          │   │
│  │  Images: AI-suggested visual direction              │   │
│  │  Updated: Every 15-60 minutes automatically          │   │
│  └─────────────────────────────────────────────────────┘   │
└──────────────────────────────��──────────────────────────────┘
```

## The Endless Loop in Action

### Cycle 1 (12:00 PM)
**Trend**: AI avatars going viral on Instagram  
**Website Theme**: Neon colors, glitch effects, tech-forward fonts  
**Headline**: "AI is Creating the Next Generation of Creators"  
**Content**: Features about AI video tools, deep fakes, persona creation  

### Cycle 2 (12:30 PM)
**Trend**: Shift to climate action posts spiking on TikTok  
**Website Theme**: Green & earth tones, organic fonts, nature imagery  
**Headline**: "The Climate Crisis is Trending—Here's Why Gen Z Cares"  
**Content**: Features about sustainability, renewable energy, activism  

### Cycle 3 (1:00 PM)
**Trend**: Celebrity drama exploding on X  
**Website Theme**: Bold reds, dramatic fonts, entertainment-focused  
**Headline**: "Entertainment News That's Breaking the Internet Right Now"  
**Content**: Features about celebrity culture, parasocial relationships  

### Cycle 4 (1:30 PM)
**Trend**: New workout trend on TikTok  
**Website Theme**: Energetic purples, fitness fonts, motion-based design  
**Headline**: "The Fitness Revolution is Here—Join the Movement"  
**Content**: Features about health, wellness, fitness trends  

**And it continues... forever. Your site is never the same twice.**

## Tech Stack

- **Host**: AWS EC2 (Ubuntu 22.04+)
- **Automation Engine**: n8n (self-hosted)
- **AI/LLM**: OpenAI GPT-4o or Claude 3.5 Sonnet
- **Database**: PostgreSQL / Supabase
- **Frontend**: React / Next.js / Vue.js / Static HTML
- **Version Control**: GitHub / GitLab
- **Deployment**: CI/CD (GitHub Actions, GitLab CI)
- **Monitoring**: n8n logs, Slack/Discord alerts, Datadog/CloudWatch

## Trend Data Sources

```json
{
  "sources": {
    "x_twitter": {
      "endpoint": "https://api.x.com/2/trends/place.json",
      "api_key": "REQUIRED",
      "rate_limit": "15 calls per 15 min",
      "data": ["trends", "volume", "url_data"]
    },
    "instagram": {
      "endpoint": "Meta Graph API - Trending Hashtags",
      "api_key": "REQUIRED",
      "rate_limit": "Variable",
      "data": ["hashtag_name", "recent_posts", "engagement"]
    },
    "facebook": {
      "endpoint": "Meta Graph API - Public Pages",
      "api_key": "REQUIRED",
      "rate_limit": "Variable",
      "data": ["trending_topics", "posts_engaging", "shares"]
    },
    "reddit": {
      "endpoint": "https://www.reddit.com/r/<subreddit>/hot.json",
      "api_key": "OPTIONAL",
      "rate_limit": "60 calls per min",
      "data": ["post_title", "upvotes", "comments", "subreddit"]
    },
    "tiktok": {
      "endpoint": "TikTok API (if available) or third-party",
      "api_key": "REQUIRED",
      "rate_limit": "Variable",
      "data": ["trending_sounds", "trending_hashtags", "video_challenges"]
    },
    "youtube": {
      "endpoint": "https://www.youtube.com/api/trending",
      "api_key": "REQUIRED",
      "rate_limit": "Variable",
      "data": ["video_title", "category", "views", "engagement"]
    },
    "google_trends": {
      "endpoint": "Google Trends API or Pytrends",
      "api_key": "OPTIONAL",
      "rate_limit": "Moderate",
      "data": ["keyword", "search_volume", "rising_queries"]
    }
  }
}
```

## AI Prompt Template for Theme Generation

```
You are a creative AI designer and copywriter. Given a trending topic,
generate a complete website theme transformation.

Trending Topic: {{TREND_KEYWORD}}
Trend Score: {{TREND_SCORE}}
Trend Category: {{CATEGORY}}
Engagement Level: {{ENGAGEMENT}}

Respond with JSON:
{
  "theme": {
    "primary_color": "#HEX",
    "secondary_color": "#HEX",
    "accent_color": "#HEX",
    "background_color": "#HEX",
    "text_color": "#HEX",
    "mood": "energetic | calm | dramatic | playful | serious",
    "style": "minimalist | maximalist | retro | futuristic | natural"
  },
  "typography": {
    "headline_font": "font name",
    "body_font": "font name",
    "accent_font": "font name",
    "font_sizes": {"h1": "3.5rem", "p": "1rem"}
  },
  "content": {
    "headline": "Main heading for the website",
    "subheading": "Supporting subheading",
    "cta_primary": "Primary call-to-action text",
    "cta_secondary": "Secondary call-to-action text",
    "body_copy": "2-3 sentences explaining why this trend matters",
    "features": [
      {"title": "Feature 1", "description": "..."},
      {"title": "Feature 2", "description": "..."}
    ]
  },
  "imagery": {
    "image_keywords": ["keyword1", "keyword2", "keyword3"],
    "photography_style": "Description of visual style",
    "illustration_style": "Description of illustration approach",
    "icon_style": "minimalist | filled | outline | animated"
  },
  "layout": {
    "hero_style": "fullscreen | split | centered | asymmetric",
    "grid_layout": "1-column | 2-column | 3-column | masonry",
    "animation_level": "none | subtle | moderate | heavy"
  },
  "messaging": {
    "emotional_tone": "Description of tone",
    "target_audience_message": "What this trend means to the audience",
    "call_to_action_message": "Why should visitors take action now?"
  }
}
```

## Expected Loop Frequency

- **Every 15 minutes**: Lightweight trend check (new cycle starts)
- **Every 30 minutes**: Full theme generation and deployment (if significant trend change)
- **Every hour**: Comprehensive analysis and optional manual review
- **24/7**: Website is always live and reflects current internet trends

## Example Output: One Complete Cycle

```json
{
  "cycle_id": "cycle-2026-10-06-120000",
  "timestamp": "2026-10-06T12:00:00Z",
  "duration_seconds": 87,
  "top_trend": {
    "keyword": "AI avatars",
    "source": "instagram",
    "score": 9.8,
    "volume": 245000,
    "velocity": "rising",
    "category": "technology"
  },
  "generated_theme": {
    "colors": {"primary": "#00D9FF", "secondary": "#FF006E"},
    "mood": "futuristic",
    "headline": "AI is Creating the Next Generation of Creators"
  },
  "content_generated": true,
  "deployment_status": "success",
  "website_updated_at": "2026-10-06T12:01:27Z",
  "metrics": {
    "engagement_predicted": 0.87,
    "trend_sustainability": 0.74
  }
}
```

## Getting Started

See the `/setup` directory for:
- EC2 installation guide
- n8n workflow setup
- Database schema
- Environment configuration
- Deployment guide

## Production Considerations

⚠️ **Important**:
- Use official APIs and respect rate limits
- Add content moderation before auto-publishing
- Include a "pause" button for manual override
- Monitor AI-generated content quality
- Keep a safety layer for brand-damaging trends
- Test extensively before going live
- Have a rollback plan if something breaks

## License

MIT
