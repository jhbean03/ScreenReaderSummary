import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

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

def preprocess_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Remove leading and trailing whitespace
    return text.strip()

with open("../popup/popup.html", "r") as file:
    html_content = file.read()
    generate_summary(html_content)
