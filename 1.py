from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/606191/convert-bytes-to-a-string"
# url = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"
r = requests.get(url)
# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())
content = soup.prettify()

f = open("./webscrapping/index.html", "w", encoding="utf-8")
# f.write((r.content).decode("utf-8"))
f.write(content)
f.close()