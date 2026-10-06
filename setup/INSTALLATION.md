# Setup & Installation Guide

## Prerequisites

- AWS Account with EC2 access
- Git installed locally
- Docker installed on EC2
- API keys for:
  - X (Twitter) API v2
  - Meta (Instagram/Facebook) Graph API
  - Reddit API (optional)
  - OpenAI API
  - GitHub Personal Access Token (for deployments)
  - (Optional) Notion, Airtable, or Supabase for trend storage

## Step 1: Launch EC2 Instance

```bash
# AWS Console or CLI
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t3.medium \
  --key-name your-key-pair \
  --security-groups default \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=n8n-trend-updater}]'
```

## Step 2: SSH into EC2

```bash
ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>
```

## Step 3: Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker
```

## Step 4: Clone the Repository

```bash
git clone https://github.com/Sudhansu-12/n8n-auto-web-updater-ec2.git
cd n8n-auto-web-updater-ec2
```

## Step 5: Set Up Environment Variables

```bash
cp .env.example .env
# Edit .env with your API keys
nano .env
```

Fill in:
```
X_API_KEY=your_x_api_key
X_BEARER_TOKEN=your_x_bearer_token
META_ACCESS_TOKEN=your_meta_token
OPENAI_API_KEY=your_openai_key
GITHUB_TOKEN=your_github_token
SUPABASE_URL=your_db_url
SUPABASE_KEY=your_db_key
```

## Step 6: Start n8n with Docker

```bash
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  --env-file .env \
  n8nio/n8n
```

Access at: `http://<EC2_PUBLIC_IP>:5678`

## Step 7: Import n8n Workflow

1. Open n8n UI
2. Go to "Workflows"
3. Click "Import"
4. Upload `n8n/main-trend-loop-workflow.json`
5. Configure credentials for each API node

## Step 8: Set Up Database (Supabase Example)

```bash
# Create a Supabase project
# Get connection string from Supabase console

# Create tables:
sql/init.sql
```

## Step 9: Configure Your Website Repository

In `.env`, set:
```
SITE_REPO_PATH=/var/www/html
GITHUB_REPO=your-username/your-website-repo
GITHUB_TOKEN=your_personal_access_token
```

## Step 10: Start the Loop

1. In n8n, click "Activate" on the workflow
2. It will run every 15-60 minutes automatically
3. Watch logs in n8n dashboard
4. Website updates should appear in your Git repository

## Monitoring

```bash
# View n8n logs
docker logs <container_id> -f

# Check website git updates
cd /var/www/html && git log --oneline -10
```

## Next Steps

- [ ] Set up Slack/Discord alerts
- [ ] Configure content moderation review
- [ ] Add analytics tracking to measure trend impact
- [ ] Set up CI/CD pipeline for auto-deployment
- [ ] Add backup and rollback procedures
