import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class WhatsAppNotifier:
    def __init__(self, phone_number):
        self.phone = phone_number
        self.api_url = "https://api.callmebot.com/whatsapp.php"

    def send_message(self, message):
        try:
            if not self.phone:
                logger.warning("No phone number configured")
                return False
            
            params = {
                'phone': self.phone,
                'text': message,
                'apikey': ''
            }
            
            resp = requests.get(self.api_url, params=params, timeout=10)
            
            if resp.status_code == 200:
                logger.info("WhatsApp message sent")
                return True
            else:
                logger.warning(f"WhatsApp API error: {resp.status_code}")
                return False
        except Exception as e:
            logger.error(f"WhatsApp send error: {str(e)}")
            return False

    def send_job_alert(self, jobs):
        if not jobs:
            return False
        
        msg = "🚀 *IPG Job Alerts*\n"
        msg += f"_{len(jobs)} matches found_\n\n"
        
        for i, job in enumerate(jobs[:5], 1):
            msg += f"*{i}. {job.get('title', 'N/A')}*\n"
            msg += f"   🏢 {job.get('company', 'N/A')}\n"
            msg += f"   📍 {job.get('location', 'N/A')}\n"
            msg += f"   🎯 {job.get('match_score', 0)}%\n"
            msg += f"   🔗 {job.get('url', '')}\n\n"
        
        msg += f"_Time: {datetime.now().strftime('%I:%M %p')}_\n💡 Click links to apply!"
        
        return self.send_message(msg)

    def send_post_confirmation(self, post_type="daily"):
        messages = {
            'daily': "✅ Daily LinkedIn post published!",
            'certificate': "🎓 Certificate posted to LinkedIn!",
            'engagement': "📈 Engagement activity done!",
        }
        msg = f"{messages.get(post_type, '✅ Task done!')}\n_Time: {datetime.now().strftime('%I:%M %p')}_"
        return self.send_message(msg)

    def send_error(self, error_msg):
        msg = f"⚠️ *IPG Agent Error*\n\n❌ {error_msg}\n\n_Time: {datetime.now().strftime('%I:%M %p')}_"
        return self.send_message(msg)
