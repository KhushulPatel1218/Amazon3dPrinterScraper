#script to get links for each product from page list
#step 2
from bs4 import BeautifulSoup
import requests
import time

fname = "C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Page_Cache.txt"
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1
AMZ = "https://www.amazon.com"

open("C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Links_Cache.txt" , 'w').close()

q = open(fname)
i = 0
while i < count: 
    url = q.readline()

    # add header
    headers = {
        "User-Agent": 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    file = open(r"C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Links_Cache.txt", "a")

    links = soup.find_all('a', {'class': 'a-link-normal a-text-normal'})

    for link in links:
        fullLink = AMZ + link.get('href')
        file.write(fullLink)
        file.write('\n')
    i += 1
f.close()

URLextractor_Done = True