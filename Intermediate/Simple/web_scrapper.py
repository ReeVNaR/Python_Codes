import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

if soup.title and soup.title.string:
    print("Website Title:", soup.title.string)
else:
    print("Website Title: Not found")
