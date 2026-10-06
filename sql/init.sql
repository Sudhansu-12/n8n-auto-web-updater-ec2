-- Create trends table
CREATE TABLE trends (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cycle_id VARCHAR(255) UNIQUE NOT NULL,
  timestamp TIMESTAMP DEFAULT now(),
  keyword VARCHAR(255) NOT NULL,
  source VARCHAR(50), -- 'x', 'instagram', 'facebook', 'reddit', 'tiktok', 'youtube'
  trend_score FLOAT DEFAULT 0,
  engagement_volume INTEGER DEFAULT 0,
  velocity FLOAT DEFAULT 0,
  category VARCHAR(100),
  sentiment VARCHAR(20), -- 'positive', 'negative', 'neutral'
  headline TEXT,
  summary TEXT,
  primary_color VARCHAR(7),
  secondary_color VARCHAR(7),
  mood VARCHAR(50),
  imagery_keywords TEXT[],
  status VARCHAR(50) DEFAULT 'new', -- 'new', 'published', 'archived', 'failed'
  website_deployed BOOLEAN DEFAULT FALSE,
  deployed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_timestamp ON trends(timestamp DESC);
CREATE INDEX idx_status ON trends(status);
CREATE INDEX idx_website_deployed ON trends(website_deployed);

-- Create website_themes table
CREATE TABLE website_themes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  trend_id UUID REFERENCES trends(id),
  theme_config JSONB, -- Full theme object
  content_config JSONB, -- Homepage content
  css_variables TEXT, -- CSS custom properties
  html_generated TEXT, -- Generated HTML
  git_commit_sha VARCHAR(40),
  created_at TIMESTAMP DEFAULT now(),
  FOREIGN KEY (trend_id) REFERENCES trends(id) ON DELETE CASCADE
);

-- Create engagement_metrics table
CREATE TABLE engagement_metrics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  trend_id UUID REFERENCES trends(id),
  metric_name VARCHAR(100),
  value FLOAT,
  timestamp TIMESTAMP DEFAULT now(),
  FOREIGN KEY (trend_id) REFERENCES trends(id) ON DELETE CASCADE
);

CREATE INDEX idx_trend_metrics ON engagement_metrics(trend_id, timestamp);

-- Create audit_log table
CREATE TABLE audit_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cycle_id VARCHAR(255),
  action VARCHAR(100),
  status VARCHAR(50),
  error_message TEXT,
  duration_seconds FLOAT,
  created_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_audit_cycle ON audit_log(cycle_id);
CREATE INDEX idx_audit_created ON audit_log(created_at DESC);
