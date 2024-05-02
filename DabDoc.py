import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

data = []
url = "https://www.dabadoc.com/recherche?country=MA&search%5Bdoctor_speciality_id%5D=51d6e1f4ef96750d4d00002d&search%5Btype%5D=0&search%5Bbooking_type%5D=0&search%5Bcity_id%5D=5225c16122814f1518000005&button="
page = requests.get(url)

if page.status_code == 404:
    print("The URL is not found.")
else:
    soup = BeautifulSoup(page.text, "html.parser") 
    all_cards = soup.find_all("div", class_="result-box rounded")
    
    for card in all_cards:
        item = {}
        link_elem = card.find("a", class_='profile_url')
        if link_elem:
            item['Link'] = link_elem.attrs.get("href", "Link not found") 
        else:
            print("Link element not found for a card.")
            continue 
        
        img_elem = card.find("img", class_='doctor-profile-pic picture_url')
        if img_elem:
            img_url = img_elem.get('data-src', '')
            item['image'] = img_url
        else:
            print("Image element not found for a card.")
            continue

        title_elem = card.find("a", class_='profile_url').text
        if title_elem:
            item['DoctorName'] = title_elem.strip()
        else:
            item['DoctorName'] = 'Not Found'
            print("Title element not found for a card.")
            continue

        span_elem = card.find("span")
        if span_elem:
            item['Location'] = span_elem.text.strip()
        else:
            item['Location'] = " Not Found"
            print("Span element not found for a card.")

        
        url_parts = link_elem['href'].split('/')
        if len(url_parts) >= 2:
            item['City'] = url_parts[-2]
        else:
            item['City'] = 'Not Found'

        item['Specialiter'] = 'Pneumologue'

        data.append(item)
        # Sleep for 2 seconds before making the next request
        # time.sleep(2)

# Create DataFrame
df = pd.DataFrame(data)
# df.to_csv("DabDoc.csv", mode='a', index=False, header=not os.path.exists("DabDoc.csv"))
df.to_csv("TAYSIR.csv", index=False)
