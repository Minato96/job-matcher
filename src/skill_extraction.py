import spacy
import fitz

nlp=spacy.load('en_core_web_sm')

def extract_text_from_pdf(pdf_path):
    """Extracts text from the PDF file"""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    '''Extract skills from text using spacy's NER and rule based matching'''
    doc=nlp(text=text)
    skills=set()

    SKILLS_DB = [
        'python', 'java', 'c++', 'sql', 'javascript', 'react', 'vue',
        'machine learning', 'deep learning', 'nlp', 'data analysis',
        'data visualization', 'tableau', 'power bi', 'aws', 'azure', 'gcp',
        'docker', 'kubernetes', 'git', 'scikit-learn', 'tensorflow', 'pytorch'
    ]

    for skill in SKILLS_DB:
        if skill in text.lower():
            skills.add(skill)
    
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'PRODUCT']: # Sometimes organizations and prducts can be technologies or skills
            skills.add(ent.text.lower())

    return list(skills)

