import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send an HTTP request to the website
url = 'https://roadmap.sh/frontend'  # Replace with the URL of the website you want to scrape
response = requests.get(url)

# Step 2: Check if the request was successful (status code 200)
if response.status_code == 200:
    # Step 3: Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract data from HTML elements
    # Replace this with your own logic based on the structure of the webpage
    data_list = []
    for item in soup.find_all('div', class_='example-class'):
        title = item.find('h2').text.strip()
        description = item.find('p').text.strip()
        data_list.append({'Title': title, 'Description': description})

    # Step 4: Create a pandas DataFrame
    df = pd.DataFrame(data_list)

    # Step 5: Convert DataFrame to CSV
    csv_file = 'output_data.csv'
    df.to_csv(csv_file, index=False)

    print(f'The data has been successfully written to {csv_file}.')
else:
    print(f'Error: Unable to fetch the webpage. Status code: {response.status_code}')
