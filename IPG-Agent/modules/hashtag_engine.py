import random
from datetime import datetime

class HashtagEngine:
    def __init__(self):
        self.trending = {
            'tech': ['#TechTrends', '#Innovation', '#Technology', '#DigitalTransformation', '#TechCommunity'],
            'programming': ['#Coding', '#Programming', '#SoftwareDevelopment', '#DevLife', '#CodeNewbie'],
            'ai_ml': ['#AI', '#MachineLearning', '#DeepLearning', '#ArtificialIntelligence', '#DataScience'],
            'career': ['#CareerGrowth', '#JobSearch', '#Hiring', '#OpenToWork', '#CareerAdvice'],
            'webdev': ['#WebDevelopment', '#Frontend', '#Backend', '#FullStack', '#JavaScript'],
            'data': ['#DataAnalytics', '#BigData', '#DataVisualization', '#DataDriven', '#Analytics'],
            'cloud': ['#CloudComputing', '#AWS', '#Azure', '#DevOps', '#CloudNative'],
            'general': ['#LinkedIn', '#ProfessionalDevelopment', '#Networking', '#Growth', '#Success'],
        }
        self.time_tags = {
            'morning': ['#MorningMotivation', '#NewDay', '#Productivity', '#MorningRoutine'],
            'afternoon': ['#LunchAndLearn', '#AfternoonVibes', '#WorkLife', '#MiddayMotivation'],
            'evening': ['#EveningThoughts', '#WrapUp', '#DailyWins', '#Reflection'],
        }
        self.day_tags = {
            0: ['#MondayMotivation', '#NewWeek', '#Goals'],
            1: ['#TuesdayThoughts', '#TechTuesday', '#Transformation'],
            2: ['#WednesdayWisdom', '#MidweekMotivation', '#HumpDay'],
            3: ['#ThursdayThoughts', '#ThrowbackThursday', '#Progress'],
            4: ['#FridayFeeling', '#WeekendVibes', '#FridayMotivation'],
            5: ['#Saturday', '#WeekendLearning', '#SideProject'],
            6: ['#Sunday', '#SundayFunday', '#Preparation'],
        }
        self.cert_tags = ['#Certified', '#Certification', '#NewCertification', '#ContinuousLearning', '#Achievement', '#Milestone', '#ProfessionalCertification', '#LifelongLearning', '#SkillDevelopment', '#Upskilling']

    def get_hashtags(self, topic, skills=None, max_count=15):
        tags = set()
        topic_lower = topic.lower()
        
        for key, tag_list in self.trending.items():
            if key in topic_lower or any(w in topic_lower for w in key.split('_')):
                tags.update(random.sample(tag_list, min(4, len(tag_list))))
        
        if skills:
            for skill in skills[:3]:
                tags.add(f'#{skill.replace(" ", "")}')
        
        hour = datetime.now().hour
        if hour < 12:
            tags.update(random.sample(self.time_tags['morning'], 2))
        elif hour < 17:
            tags.update(random.sample(self.time_tags['afternoon'], 2))
        else:
            tags.update(random.sample(self.time_tags['evening'], 2))
        
        day = datetime.now().weekday()
        tags.update(random.sample(self.day_tags[day], 2))
        
        tags.update(random.sample(['#LinkedIn', '#Professional', '#Growth', '#Learning'], 3))
        
        return ' '.join(list(tags)[:max_count])

    def get_certificate_hashtags(self, cert_name, skills=None, org=None, max_count=15):
        tags = set()
        tags.update(random.sample(self.cert_tags, 6))
        
        if skills:
            for skill in skills[:3]:
                tags.add(f'#{skill.replace(" ", "")}')
        
        if org:
            tags.add(f'#{org.replace(" ", "")}')
        
        hour = datetime.now().hour
        if hour < 12:
            tags.update(random.sample(self.time_tags['morning'], 2))
        elif hour < 17:
            tags.update(random.sample(self.time_tags['afternoon'], 2))
        else:
            tags.update(random.sample(self.time_tags['evening'], 2))
        
        day = datetime.now().weekday()
        tags.update(random.sample(self.day_tags[day], 2))
        
        return ' '.join(list(tags)[:max_count])

    def get_trending_now(self):
        hour = datetime.now().hour
        if hour < 9:
            return '#MorningMotivation #TechNews #DailyGoals #Productivity #Innovation'
        elif hour < 12:
            return '#TechTrends #Coding #AI #WebDevelopment #CareerGrowth'
        elif hour < 15:
            return '#LunchAndLearn #DevCommunity #OpenSource #Programming #TechLife'
        elif hour < 18:
            return '#AfternoonVibes #SoftwareEngineering #DataScience #CloudComputing #DevOps'
        else:
            return '#EveningThoughts #TechCommunity #Learning #ProfessionalDevelopment #Networking'
