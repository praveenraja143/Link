# IPG - LinkedIn AI Agent

Complete AI-powered LinkedIn automation agent. Auto-posts daily, posts certificates, searches jobs, and sends WhatsApp notifications.

## Features
- Daily auto-post to LinkedIn with AI-generated content
- Certificate posting with professional formatting
- Smart hashtag engine for maximum reach
- Job/Internship search across Indeed and LinkedIn
- WhatsApp notifications for job alerts
- Resume parsing (PDF/DOCX)
- Auto-update skills from certificates
- Scheduled posting at optimal times (IST)
- 100% Free - Uses Qwen AI via OpenRouter

## Setup

### 1. Install Dependencies
```bash
cd IPG-Agent
pip install -r requirements.txt
```

### 2. Configure
Edit `config.json` with your details:
```json
{
  "linkedin_email": "your_email@example.com",
  "linkedin_password": "your_password",
  "openrouter_api_key": "sk-or-your-key",
  "whatsapp_phone": "+91XXXXXXXXXX",
  "skills": ["Python", "JavaScript", "React", "Node.js"],
  "locations": ["Chennai", "Bangalore", "Remote"]
}
```

### 3. Get Free API Keys
- **OpenRouter**: https://openrouter.ai (free tier available)
- **WhatsApp**: Send "I allow callmebot" to +34 644 51 94 59

## Usage

### Run Once (Full Cycle)
```bash
python main.py --once
```
Does: Login → Daily Post → Job Search → Engage → Post Certificates

### Scheduled Mode (24/7)
```bash
python main.py --daemon
```
Posts at 9:00 AM, 12:30 PM, 6:00 PM IST automatically

### Post Certificate
```bash
python main.py --post-cert certificates/my_cert.png --cert-name "Python Course" --cert-org "Coursera" --cert-skills "Python,ML,Data Science"
```

### Search Jobs Only
```bash
python main.py --search-jobs
```

### Parse Resume
```bash
python main.py --parse-resume my_resume.pdf
```

## Schedule (Default IST)
| Time | Task |
|------|------|
| 09:00 | Morning LinkedIn post |
| 10:00 | Job search + WhatsApp alert |
| 11:00 | Engagement activity |
| 12:30 | Afternoon LinkedIn post |
| 15:00 | Job search + WhatsApp alert |
| 16:00 | Engagement activity |
| 18:00 | Evening LinkedIn post |

## Folder Structure
```
IPG-Agent/
├── main.py              # Main orchestrator
├── config.json          # Your configuration
├── requirements.txt     # Dependencies
├── modules/
│   ├── linkedin.py      # LinkedIn bot (Selenium)
│   ├── ai_content.py    # AI content (Qwen/OpenRouter)
│   ├── hashtag_engine.py # Smart hashtags
│   ├── job_searcher.py  # Job search (Indeed, LinkedIn)
│   ├── whatsapp.py      # WhatsApp notifications
│   ├── resume_parser.py # Resume parsing
│   └── scheduler.py     # Task scheduler
├── certificates/        # Drop cert images here
└── data/               # Logs and state
```

## How It Works
1. **Resume Upload** → Extracts skills automatically
2. **Daily Post** → AI generates content + optimal hashtags → Posts to LinkedIn
3. **Certificate** → Upload image → AI creates professional post → Posts with image → Updates resume skills
4. **Job Search** → Searches Indeed + LinkedIn → Filters by skill match → Sends WhatsApp with apply links
5. **WhatsApp Alerts** → Job alerts, post confirmations, error notifications

## App Name: IPG
## GitHub: https://github.com/praveenraja143/Link
