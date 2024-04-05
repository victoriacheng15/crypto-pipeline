import requests, re
from bs4 import BeautifulSoup

def get_data():
  URL = "https://www.coindesk.com/data/"
  page = requests.get(URL).text
  soup = BeautifulSoup(page, "html.parser")

  return soup.find_all(class_=re.compile(r'price-liststyles__ListCardWrapper-sc-ouhin1-2'))