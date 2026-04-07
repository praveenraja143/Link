import os
import re
import logging

logger = logging.getLogger(__name__)

class ResumeParser:
    def __init__(self):
        self.common_skills = [
            'Python', 'JavaScript', 'TypeScript', 'Java', 'C++', 'C#', 'Go', 'Rust', 'Ruby', 'PHP',
            'React', 'Angular', 'Vue.js', 'Node.js', 'Express', 'Django', 'Flask', 'FastAPI', 'Spring Boot',
            'SQL', 'MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'SQLite',
            'AWS', 'Azure', 'GCP', 'Docker', 'Kubernetes', 'Terraform', 'CI/CD', 'Git',
            'HTML', 'CSS', 'SASS', 'Tailwind', 'Bootstrap',
            'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'Scikit-learn', 'Pandas', 'NumPy',
            'Data Analysis', 'Data Science', 'Data Visualization', 'Tableau', 'Power BI',
            'REST API', 'GraphQL', 'Microservices', 'Serverless',
            'Agile', 'Scrum', 'JIRA', 'TDD', 'BDD',
            'Linux', 'Windows', 'MacOS', 'Networking', 'Security',
            'React Native', 'Flutter', 'Android', 'iOS', 'Mobile Development',
            'Testing', 'Jest', 'Pytest', 'Selenium', 'Cypress',
            'Webpack', 'Vite', 'Babel', 'npm', 'yarn',
            'OOP', 'Functional Programming', 'Design Patterns', 'System Design',
        ]

    def parse_text(self, text):
        found_skills = []
        text_upper = text.upper()
        
        for skill in self.common_skills:
            if skill.upper() in text_upper:
                found_skills.append(skill)
        
        logger.info(f"Extracted {len(found_skills)} skills from resume")
        return found_skills

    def parse_pdf(self, pdf_path):
        try:
            import PyPDF2
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            return self.parse_text(text)
        except Exception as e:
            logger.error(f"PDF parse error: {str(e)}")
            return []

    def parse_docx(self, docx_path):
        try:
            from docx import Document
            doc = Document(docx_path)
            text = "\n".join([p.text for p in doc.paragraphs])
            return self.parse_text(text)
        except Exception as e:
            logger.error(f"DOCX parse error: {str(e)}")
            return []

    def parse_file(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            return self.parse_pdf(file_path)
        elif ext in ['.docx', '.doc']:
            return self.parse_docx(file_path)
        else:
            logger.error(f"Unsupported file type: {ext}")
            return []

    def merge_skills(self, existing, new_skills):
        existing_lower = [s.lower() for s in existing]
        added = []
        for skill in new_skills:
            if skill.lower() not in existing_lower:
                added.append(skill)
                existing.append(skill)
        return existing, added
