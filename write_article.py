import anthropic
import os
from datetime import date
import re

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

TOPICS = [
    "how AI is transforming cancer diagnosis and treatment",
    "large language models in medical research and healthcare",
    "AI ethics in clinical decision making",
    "machine learning for drug discovery and development",
    "AI tools every data scientist should know in 2026",
    "how AI is personalising cancer chemotherapy",
    "responsible AI in healthcare systems",
    "the role of AI in predicting patient outcomes",
    "AI and mathematical modelling in precision oncology",
    "how neural networks are being used in medical imaging",
    "AI regulation in healthcare — what researchers need to know",
    "the future of AI-assisted surgery and treatment planning",
    "mathematical oncology and cancer modelling",
    "AI in healthcare and medicine",
    "life as a woman in STEM and mathematics",
    "data science tools and techniques",
    "phase-field modelling and computational biology",
    "personalised medicine and mathematical models",
    "uncertainty quantification in research",
    "Bayesian methods in biomedical research",
]

week = date.today().isocalendar()[1]
topic = TOPICS[week % len(TOPICS)]

print("Writing article about: " + topic)

prompt = "You are writing for the personal website of Maryam Alka, an AI researcher and Applied Mathematician at the University of Birmingham working on AI-driven mathematical models for cancer treatment. Write a high quality 500-word blog article about: " + topic + ". IMPORTANT: This article must lead with AI and technology as the primary focus. Mathematics and oncology are supporting context only. The reader should finish the article thinking of the author as an AI expert in healthcare. Use clear accessible language. Tone: neutral and factual. First person where natural. Format your response EXACTLY like this with no extra text before or after. TITLE: [title here] SLUG: [url-friendly-title-with-hyphens] DESCRIPTION: [one sentence summary] ARTICLE: [article content in markdown]"

response = client.messages.create(
    model="claude-opus-4-20250514",
    max_tokens=1500,
    messages=[{"role": "user", "content": prompt}]
)

text = response.content[0].text
title = text.split("TITLE:")[1].split("SLUG:")[0].strip()
slug = text.split("SLUG:")[1].split("DESCRIPTION:")[0].strip()
description = text.split("DESCRIPTION:")[1].split("ARTICLE:")[0].strip()
article = text.split("ARTICLE:")[1].strip()

slug = re.sub(r'[^a-z0-9-]', '', slug.lower().replace(' ', '-'))

today = date.today().isoformat()
filename = "content/posts/" + today + "-" + slug + ".md"

content = "---\ntitle: \"" + title + "\"\ndate: " + today + "\ndescription: \"" + description + "\"\ntags: [\"" + topic.split()[0] + "\"]\n---\n\n" + article

os.makedirs("content/posts", exist_ok=True)
with open(filename, "w") as f:
    f.write(content)

print("Article saved: " + filename)
print("Title: " + title)
