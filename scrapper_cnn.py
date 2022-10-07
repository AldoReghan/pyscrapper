import requests
from bs4 import BeautifulSoup
import re

keywords = {
    "Pemilu",
    "Pemilu2019",
    "Jokowi",
    "Prabowo",
    "Nyoblos",
    "Ayo Nyoblos",
    "Ayo ke TPS",
    "Pemilu bersih",
}

for keyword in keywords:
    for page in range(1,10):
        pages = requests.get("https://www.cnnindonesia.com/search/?query=" + keyword + "&page="+ str(page))
        soup = BeautifulSoup(pages.content, 'html.parser')
        links = soup.findAll("a")
        for l in links:
                print(l.get('href'))
                # for link in soup.find_all("a",href=re.compile("(?<=/url\?query=)(htt.*://.*)")):
                #     print(re.split(":(?=http)",link["href"].replace("/url?query=","")))
                with open("result.txt", "a") as f:
                    f.write(l["href"] + "\n")