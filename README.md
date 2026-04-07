# 🤖 LinkedIn Job Agent

> AI-powered job skill matcher + LinkedIn post generator. **100% Free** using OpenRouter (Llama 3.3 70B).

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/linkedin-job-agent)

## ✨ Features

- 🎯 **Job Skill Matching** — Paste any job description, get AI match score
- ✍️ **LinkedIn Post Generator** — Auto-generate posts for your job search
- 💰 **100% Free** — Uses OpenRouter free tier (Llama 3.3 70B)
- ⚡ **Serverless** — Deployed on Vercel, no server costs

## 🚀 Setup

### 1. Get Free API Key
1. Go to [openrouter.ai](https://openrouter.ai)
2. Sign up (no credit card needed)
3. Create API Key

### 2. Add Environment Variable in Vercel
```
OPENROUTER_API_KEY = your_key_here
```
Go to: Vercel → Project → Settings → Environment Variables

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Status check |
| POST | `/api/match` | Job skill matching |
| POST | `/api/generate-post` | LinkedIn post generation |

### POST /api/match
```json
{
  "skills": ["JavaScript", "Node.js", "React"],
  "jobTitle": "Full Stack Developer",
  "jobDescription": "...",
  "company": "Infosys"
}
```

### POST /api/generate-post
```json
{
  "skills": ["JavaScript", "Node.js"],
  "role": "Full Stack Developer",
  "tone": "professional"
}
```

## 🏗️ Tech Stack
- **Frontend**: Vanilla HTML/CSS/JS
- **Backend**: Vercel Serverless Functions (Node.js)
- **AI**: OpenRouter → Llama 3.3 70B (Free)
- **Hosting**: Vercel (Free)

Built by Chance 🚀
