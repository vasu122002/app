import requests

from bs4 import BeautifulSoup

import pandas as pd 


base_url = 'https://www.google.com/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}


def get_coordinates(sector):
    search_term = f"sector {sector} gurgaon longitude & latitude"
    response = requests.get(base_url + search_term, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        coordinates_div = soup.find("div", class_="Z0LcW t2b5Cf")
        if coordinates_div:
            return coordinates_div.text
    return None
    
# Create a DataFrame
df = pd.DataFrame(columns=["Sector", "Coordinates"])

# Iterate over sectors and fetch coordinates
for sector in range(1, 116):
    coordinates = get_coordinates(sector)
    df = df.append({"Sector": f"Sector {sector}", "Coordinates": coordinates}, ignore_index=True)

# Save DataFrame
df.to_csv("gurgaon_sectors_coordinates.csv", index=False)