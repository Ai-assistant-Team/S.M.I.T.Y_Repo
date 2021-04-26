#https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/

import requests
from bs4 import BeautifulSoup

def create_list_with_links(list_of_links):
   urls = 'https://www.news.gr/'
   grab = requests.get(urls)
   soup = BeautifulSoup(grab.text, 'html.parser')
   for link in soup.find_all("a"):
      data = link.get('href')
      list_of_links.append(data)
   return list_of_links
