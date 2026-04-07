import requests
from bs4 import BeautifulSoup
import json
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class JobSearcher:
    def __init__(self, skills, locations=None):
        self.skills = skills
        self.locations = locations or ["Remote", "India"]
        self.seen_file = "data/seen_jobs.json"
        self.seen_jobs = self._load_seen()

    def _load_seen(self):
        if os.path.exists(self.seen_file):
            try:
                with open(self.seen_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return []

    def _save_seen(self):
        os.makedirs("data", exist_ok=True)
        with open(self.seen_file, 'w') as f:
            json.dump(self.seen_jobs[-500:], f)

    def search_indeed(self, limit=15):
        jobs = []
        for skill in self.skills[:5]:
            for location in self.locations[:2]:
                try:
                    url = f"https://www.indeed.com/jobs?q={skill.replace(' ', '+')}&l={location.replace(' ', '+')}&sort=date"
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                    resp = requests.get(url, headers=headers, timeout=10)
                    
                    if resp.status_code == 200:
                        soup = BeautifulSoup(resp.text, 'html.parser')
                        cards = soup.find_all('div', class_='job_seen_beacon')[:3]
                        
                        for card in cards:
                            title_tag = card.find('h2', class_='jobTitle')
                            company_tag = card.find('span', class_='companyName')
                            location_tag = card.find('div', class_='companyLocation')
                            link_tag = title_tag.find('a') if title_tag else None
                            
                            if title_tag and link_tag:
                                job_id = title_tag.get_text(strip=True) + company_tag.get_text(strip=True) if company_tag else ""
                                if job_id not in self.seen_jobs:
                                    self.seen_jobs.append(job_id)
                                    jobs.append({
                                        'source': 'Indeed',
                                        'title': title_tag.get_text(strip=True),
                                        'company': company_tag.get_text(strip=True) if company_tag else 'N/A',
                                        'location': location_tag.get_text(strip=True) if location_tag else 'N/A',
                                        'url': f"https://www.indeed.com{link_tag.get('href')}",
                                        'skill': skill,
                                        'posted': 'Recently',
                                        'match_score': self._calc_match(skill),
                                    })
                except Exception as e:
                    logger.error(f"Indeed search error for {skill}: {str(e)}")
        
        self._save_seen()
        return jobs[:limit]

    def search_linkedin_jobs(self, limit=10):
        jobs = []
        for skill in self.skills[:3]:
            url = f"https://www.linkedin.com/jobs/search/?keywords={skill.replace(' ', '%20')}&location={self.locations[0].replace(' ', '%20')}&sortBy=DD"
            jobs.append({
                'source': 'LinkedIn',
                'title': f'{skill} positions',
                'company': 'Various',
                'location': self.locations[0],
                'url': url,
                'skill': skill,
                'posted': 'Recently',
                'match_score': self._calc_match(skill),
            })
        return jobs[:limit]

    def _calc_match(self, skill):
        score = 50
        skill_lower = skill.lower()
        preferred = ['python', 'javascript', 'react', 'node', 'ml', 'data', 'java', 'aws']
        for p in preferred:
            if p in skill_lower:
                score += 30
                break
        return min(score, 100)

    def search_all(self):
        logger.info("Searching jobs across all platforms...")
        all_jobs = []
        all_jobs.extend(self.search_indeed())
        all_jobs.extend(self.search_linkedin_jobs())
        all_jobs = sorted(all_jobs, key=lambda x: x.get('match_score', 0), reverse=True)
        logger.info(f"Found {len(all_jobs)} jobs")
        return all_jobs

    def get_high_match(self, jobs, min_score=60):
        return [j for j in jobs if j.get('match_score', 0) >= min_score]
