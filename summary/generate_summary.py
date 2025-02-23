from transformers import GPT2LMHeadModel, GPT2Tokenizer
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
    summarize_text(clean_text)

def preprocess_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Remove leading and trailing whitespace
    return text.strip()

def summarize_text(clean_text):
    model_name = 'gpt2'
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokens = tokenizer(clean_text, return_tensors='pt')
    # for i in range(len(clean_text.split())): 
    #     tokens[str(id(clean_text.split()[i]))] = clean_text.split()[i]
    #print("good here1")
    #token_ids = [model.config.pad_token_id for word in tokens] 
    #input_tensor = torch.tensor([tokens])
    #print("good here2")
    #print("good here3")
    print(tokens)
    #print("good here4")
    output = model.generate(**tokens, max_length= 50, temperature=0.7)
    summary = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Summary:", summary )



# if os.path.exists(file_path):
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# else:
#     print(f"Error: The file {file_path} does not exist.")

file_path = "summary/popup.html"
with open(file_path, "r") as file:
    html_content = file.read()
    generate_summary(html_content)
