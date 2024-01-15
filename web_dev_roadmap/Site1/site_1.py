import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.browserstack.com/guide/web-development-roadmap"


r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')


# THIS CONTAINS THE MAIN HEADING FOR EACH STEPS OF ROADMAP
h4_elements = soup.find_all('h4')
h4_contents = [h4.text for h4 in h4_elements]
# print(h4_contents)    #success


# THIS CONTAINS BASIC INFORMATION REGARDING EACH STEPS 
p_elements = soup.find_all('span')
p_contents = [p.text for p in p_elements]
# print(p_contents)


# THIS CONTAINS HOW TO APPROACH EACH STEPS IN ROADMAP
li_elements = soup.find_all('li')
span_contents = [li.find('span').text if li.find('span') else '' for li in li_elements]
# print(span_contents)



# THIS CONTAINS {THIS PART} : ----
b_elements = soup.find_all('b')
b_contents = [b.text for b in b_elements]
# print(b_contents)

