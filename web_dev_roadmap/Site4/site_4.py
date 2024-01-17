import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "https://www.knowledgehut.com/blog/web-development/front-end-developer-roadmap"
r = requests.get(url)


print(r.status_code)
soup = BeautifulSoup(r.content,'html.parser')



div_elements = soup.find_all('div', class_="blog-editor-content")
div_contents = [div.text.strip() for div in div_elements]
# print(div_contents)

df1 = pd.DataFrame(columns=div_contents)
df1.to_csv("Site_4_Scrapped.txt", index=None)
