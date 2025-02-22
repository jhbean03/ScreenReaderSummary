import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def generate_summary(html):

    # Create 
    soup = BeautifulSoup(html, features = "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    print(text)
    file = open("trainingstuff.txt", 'r')
    with file as file:
        file_content = file.read()
    print(file_content)
    # tokenizer = T5Tokenizer.from_pretrained("google-tf/tf-small")
    # model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")
    # input = tokenizer("Summarize this text:" + text, return_tensors="pt").input
    # answer = tokenizer(file_content, return_tensors="pt").input
    # loss = model(input=input, answer=answer).loss
    # loss.item()


