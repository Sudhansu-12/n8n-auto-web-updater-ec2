#!/bin/bash

# Deploy generated theme to website repository
# This script is called by n8n after theme generation

set -e

TREND_ID=$1
THEME_JSON=$2
REPO_PATH=${SITE_REPO_PATH:-/var/www/html}
GITHUB_TOKEN=${GITHUB_TOKEN}
GITHUB_REPO=${GITHUB_REPO}

echo "[$(date)] Starting website deployment for trend: $TREND_ID"

# Navigate to website repo
cd "$REPO_PATH"

# Create theme configuration file
echo "$THEME_JSON" > theme-config.json

# Generate index.html with new theme
cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trending Now</title>
    <style id="theme-styles"></style>
    <script>
        const themeConfig = THEME_DATA_HERE;
        document.documentElement.style.setProperty('--primary-color', themeConfig.theme.primary_color);
        document.documentElement.style.setProperty('--secondary-color', themeConfig.theme.secondary_color);
    </script>
</head>
<body>
    <div class="hero">
        <h1>CONTENT_HEADLINE_HERE</h1>
        <p>CONTENT_SUBHEADING_HERE</p>
        <button class="cta">CONTENT_CTA_HERE</button>
    </div>
    <div class="content">
        <p>CONTENT_BODY_HERE</p>
    </div>
</body>
</html>
EOF

# Add and commit
git add -A
git commit -m "[Auto] Update theme for trend: $TREND_ID" || true

# Push to GitHub
if [ -n "$GITHUB_TOKEN" ] && [ -n "$GITHUB_REPO" ]; then
    git push origin main
    echo "[$(date)] Successfully pushed to GitHub"
else
    echo "[$(date)] GitHub token/repo not configured. Skipping push."
fi

echo "[$(date)] Website deployment complete!"
