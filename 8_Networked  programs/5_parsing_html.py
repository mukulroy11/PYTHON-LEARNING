# What is Web Scraping?
# Web scraping is writing a program that pretends to be a web browser to retrieve web pages, parse the HTML, and extract specific data from them.

# Why Scrape the Web?
# Data Extraction: Extract structured data (prices, weather, contact info) from sites that don't provide an official API.

# Automation: Automate repetitive web tasks (e.g., checking for updates or collecting research).

# Data Mining: Gather massive datasets across multiple sites for analysis
# Basic Scraping Code (Using urllib & BeautifulSoup)
# To scrape HTML, you use Python's built-in urllib to download the page and an external library called BeautifulSoup (bs4) to parse the HTML tags.

import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.dr-chuck.com/page1.htm'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

for tag in tags:
    print(tag.get('href', None))