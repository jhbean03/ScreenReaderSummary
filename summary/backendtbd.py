import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
url = "https://patorjk.com/games/snake/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

# Create a request with headers
req = urllib.request.Request(url, headers=headers)

# Open the URL
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, features = "html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
text = '\n'.join(chunk for chunk in chunks if chunk)
print(text)

