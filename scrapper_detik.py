import requests
from bs4 import BeautifulSoup
import re
from goose3 import Goose

keywords = {
    "Pemilu",
    "Pemilu2019",
    "Jokowi",
    "Prabowo",
    "Anies",
    "Ganjar",
    "Andika Perkasa",
    "Nyoblos",
    "TPS",
    "Pemilu bersih",
}

filter_path = {
    "Informasi Berita",
    "detikEdu",
    "Berita Terkini",
    "detiksearch",
    "Berita Terpopuler",
    "Daftar Lowongan Kerja",
    "Detikcom"
}

for keyword in keywords:
        url = "https://www.detik.com/search/searchall?query={}&siteid=2".format(keyword)
        print("Scraping {}".format(url))
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        #get all link in search result
        links = soup.find_all("a", href=re.compile("https://www.detik.com/"))
        #loop all link and get article
        for link in links:
            try:
                g = Goose()
                article = g.extract(url=link["href"])
                #create condition where article title contain filter path dont save
                if not any(x in article.title for x in filter_path):
                    print("Title: {}".format(article.title))
                    print("Publish Date: {}".format(article.publish_date))
                    print("Link: {}".format(link["href"]))
                    print("Keyword: {}".format(keyword))
                    print("=================================")
                    with open("result_detik.txt", "a") as f:
                            f.write("Title: {}\n".format(article.title))
                            f.write("Publish Date: {}\n".format(article.publish_date))
                            f.write("Link: {}\n".format(link["href"]))
                            f.write("Keyword: {}\n".format(keyword))
                            f.write("=================================\n") 
                    
            except:
                pass