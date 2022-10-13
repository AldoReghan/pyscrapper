import requests
from bs4 import BeautifulSoup
import re
from goose3 import Goose
from bs4 import BeautifulSoup
from matplotlib.style import available
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

keyword = open("wordlist/keywords.txt", "r").read().splitlines()
source = open("wordlist/web_loadmore.txt", "r").read().splitlines()
nextsource = open("wordlist/web_nextpage.txt", "r").read().splitlines()

def loadmore():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for key in keyword:
        for src in source:
            driver.get("{}?s={}".format(src,key))
            while True:
                try:
                    load_more_button = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, "td_ajax_load_more"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
                    load_more_button.click()
                    #get all title
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    titles = soup.find_all("div", class_="tdb_module_loop")
                    for title in titles:
                        print(src)
                        print(title.find("h3").text)
                        with open("res.txt", "a") as f:
                            f.write("Title : "+title.find("h3").text + "\n")
                            f.write("Link : "+title.find("a")["href"] + "\n")
                            f.write("Source : "+src + "\n")
                            f.write("Keyword : "+key + "\n")
                            f.write("============================================="+ "\n")
                except:
                    break

def nextpage():
    for key in keyword:
        for src in nextsource:
            for page in range(1, 101):
                url = "{}/page/{}/?s={}".format(src,page,key)
                print("Scraping {}".format(url))
                r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                #get all link in search result
                titles = soup.find_all("div", class_="tdb_module_loop")
                #loop all link and get article
                for title in titles:
                    print(src)
                    print(title.find("h3").text)
                    with open("res.txt", "a") as f:
                        f.write("Title : "+title.find("h3").text + "\n")
                        f.write("Link : "+title.find("a")["href"] + "\n")
                        f.write("Source : "+src + "\n")
                        f.write("Keyword : "+key + "\n")
                        f.write("============================================="+ "\n")

nextpage()
loadmore()