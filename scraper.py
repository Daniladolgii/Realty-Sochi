import requests
from bs4 import BeautifulSoup
from config import SCRAPING_URL

def scrape_site():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    try:
        response = requests.get(SCRAPING_URL, headers=headers)
        response.raise_for_status()  # Проверяем на ошибки

        soup = BeautifulSoup(response.content, 'html.parser')
        listings = soup.find_all('div', class_='listing-item')

        scraped_data = []
        for listing in listings:
            title = listing.find('h2').get_text(strip=True)
            link = listing.find('a')['href']
            full_link = f"https://example-real-estate-website.com{link}"
            scraped_data.append({'title': title, 'link': full_link})

        return scraped_data
    except requests.RequestException as e:
        print(f"Ошибка при доступе к сайту: {e}")
        return []
