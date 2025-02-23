from transformers import pipeline
import torch
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import os

def generate_summary(html):

    # Obtain text information from the HTML
    soup = BeautifulSoup(html, "html.parser")

    # Remove all of the scripts and styling information
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()

    # Clean up the text obtained from the file
    clean_text = preprocess_text(text)

    print(clean_text)
    return summarize_text(clean_text)

def preprocess_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Remove leading and trailing whitespace
    return text.strip()

def summarize_text(clean_text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(clean_text, maxlength=50, min_length=30, do_sample=False)
    return summary[0]['summary_text']
