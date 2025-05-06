# Begin by importing requests and BeautifulSoup. Most of this is related to in Project 2, so comments will be on the important parts rather than every minute detail.

import requests
from bs4 import BeautifulSoup

class HeadlineScraper:
    def __init__(self, urls_file):
        self.urls_file = urls_file

    # Grab the URLs from the urls.txt file.
    def load_urls(self):
        with open(self.urls_file, "r") as infile:
            return infile.read().splitlines()

    def extract_headings(self, url):
        # Let the user know scraping has started and on what URL it is on.
        print(f"Scraping: {url}")
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            headings = []
            blocked_phrases = ["most viewed across the guardian", "most viewed in business"]

            # Grab out all elements from the raw HTML that is between <h3> tags. Put it into a headings array.
            for tag in ['h3']:
                for element in soup.find_all(tag):
                    text = element.get_text(strip=True)
                    if text and text.lower() not in (h.lower() for h in headings) and text.lower() not in blocked_phrases:
                        headings.append(text)

            # Let the user know how many headings were found.
            print(f"Found {len(headings)} headings at {url}")
            return headings

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return []

    def scrape_all(self):
        urls = self.load_urls()
        all_headings = []
        for url in urls:
            all_headings.extend(self.extract_headings(url))

        return sorted(set(all_headings))