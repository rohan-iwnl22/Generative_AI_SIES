import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://javarevisited.blogspot.com/2023/01/the-2023-android-developer-roadmap.html#axzz8P5kyjF4D"
r = requests.get(url)

print(r.status_code)

soup = BeautifulSoup(r.content,'html.parser')


div_elements = soup.find_all("div",class_="post-body entry-content")
div_contents = [div.text.strip() for div in div_elements]
# print(div_contents)

df1 = pd.DataFrame(columns=div_contents)
df1.to_csv("Site3.txt",index=None)