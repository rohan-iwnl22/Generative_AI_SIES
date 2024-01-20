import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://getstream.io/blog/android-developer-roadmap/"
r = requests.get(url)
# print(r.status_code)

soup = BeautifulSoup(r.content,'html.parser')

div_elements = soup.find_all("div",class_="col-span-full lg:col-span-8")
div_contents = [div.text.strip() for div in div_elements]
# print(div_contents)

df1 = pd.DataFrame(columns=div_contents)
df1.to_csv("Site2.txt",index=None)

