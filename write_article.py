import anthropic
import os
from datetime import date
import re

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# Your topics — Claude rotates through these
TOPICS = [
    "mathematical oncology and cancer modelling",
    "AI in healthcare and medicine",
    "life as a woman in STEM and mathematics",
    "data science tools and techniques",
    "phase-field modelling and computational biology",
    "personalised medicine and mathematical models",
    "uncertainty quantification in research",
    "Bayesian methods in biomedical research",
]

# Pick topic based on current week number so it rotates automatically
week = date.today().isocalendar()[1]
topic = TOPICS[week % len(TOPICS)]

print(f"Writing article about: {topic}")

response = client.messages.create(
    model="claude-opus-4-20250514",
    max_tokens=1500,
    messages=[{
        "role": "user",
        "content": f"""You are writing for the personal website of Maryam Alka — an Applied Mathematician and PhD researcher at the University of Birmingham working on mathematical oncology, specifically phase-field modelling of tumour growth under hypoxia and chemotherapy.

Write a high quality 500-word blog article about: {topic}

The audience is a mix of general public and professionals. Use clear, accessible language. No jargon without explanation. Tone: neutral and factual. First person where natural.

Format your response EXACTLY like this with no extra text before or after:
TITLE: [compelling title here​​​​​​​​​​​​​​​​
