import requests
from bs4 import BeautifulSoup
import csv
import html5lib

URL = "https://facebook.com"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

