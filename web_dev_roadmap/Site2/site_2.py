import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.guvi.in/blog/web-development-roadmap-for-beginners/"
r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

# EK DIV TARGET KARTE HE POORA BLOG SCRAPPED LMFAO 💪
div_elements = soup.find_all('div', class_='elementor-widget-wrap elementor-element-populated')
div_contents = [div.text.strip() for div in div_elements]
# print(div_contents)

df3 = pd.DataFrame(columns=div_contents)
df3.to_csv('Details.txt', index=None)

