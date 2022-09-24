#gets all the pages of an item
#Step 1

from bs4 import BeautifulSoup
import requests
import time

AMZ = "https://www.amazon.com/s?k=Black+filament&ref=nb_sb_noss_2"

file_Data = "C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Page_cache.txt"

# add header
headers = {
    "User-Agent": 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

file = open(file_Data, "w")
file.writelines(AMZ + '\n')


i = 0
while i < 20:
    
    r = requests.get(AMZ, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    file = open(r'C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Page_cache.txt', "a")
    AMZ = "https://www.amazon.com"


    links = soup.findAll(True, {'class':["a-last"]})

    for x in links:
        try:
            table_rows = x.find('a').get('href')
            AMZ += table_rows 
            file.writelines(AMZ + '\n')
        except AttributeError:
            pass
        
    i += 1
pageTurner_Done = True
file.close()