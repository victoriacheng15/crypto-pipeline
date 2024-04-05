from bs4 import BeautifulSoup
import requests, re

def get_data():
  URL = "https://www.coindesk.com/data/"
  page = requests.get(URL).text
  soup = BeautifulSoup(page, "html.parser")

  # return soup.find_all(class_="price-liststyles__ListCardWrapper-sc-ouhin1-2")
  return soup.find_all(class_=re.compile(r'price-liststyles__ListCardWrapper-sc-ouhin1-2'))


def main():
  items = get_data()
  print(items[0])


if __name__ == "__main__":
  print("\nstarting the process...\n")
  main()
  print("\nthe process is complete...\n")