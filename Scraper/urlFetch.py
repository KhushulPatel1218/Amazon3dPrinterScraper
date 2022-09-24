#Script to get table data
#Step 3
import requests
from bs4 import BeautifulSoup
import os
import csv
import sys
from progress.bar import Bar

filamentData = "C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Links_Cache_ORG.csv"

fname = filamentData #Open file containg all of the product links
count = 0
with open(fname, 'r') as f: #gets number of links in the file stores it as count
    for line in f:
        count += 1
AMZ = "https://www.amazon.com" #Amazon URL

q = open(filamentData) #Opens file again

clear = open("C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Temp.csv" , 'w').close()
r = open("C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Temp.csv", 'a') 

bar = Bar('Procesing', max = count)
filList = []
i = 0 
while i < count: #while loop to loop through all the links
    URL = q.readline() #gets all the URLs

    headers = {
        "User-Agent": 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.findAll(True, {'class':["a-keyvalue" , "a-keyvalue" ]})

    colorFound = False
    materialFound = False
    brandFound = False
    weightFound = False
    diameterFound = False

    color = "[     ]"
    material = "[     ]"
    brand = "[     ]"
    weight = "[     ]"
    diameter = "[     ]"
    
    for x in title:
    
        table_rows = x.findAll('tr')
        
        for tr in table_rows: #for loop to translate table from html to csv file
            th = tr.find_all('th')
            row1 = [i.text for i in th]
            row1 = [item.replace("\n", "") for item in row1]

            td = tr.find_all('td')
            row2 = [i.text for i in td]
            row2 = [item.replace("\n", "") for item in row2]

            if colorFound == False:
                if row1[0].strip() == "Color":
                    color = row2[0].strip()
                    colorFound = True
                else:
                    pass
            
            if materialFound == False:
                if row1[0].strip() == "Material":
                    material = row2[0].strip()
                    materialFound = True
                else:
                    pass

            if brandFound == False:
                if row1[0].strip() == "Brand Name":
                    brand = row2[0].strip()
                    brandFound = True
                elif row1[0].strip() == "Manufacturer":
                    brand = row2[0].strip()
                    brandFound = True
                else:
                    pass

            
            if weightFound == False:
                if "Weight" in row1[0]:
                    weight = row2[0].strip()
                    weightFound = True
                else:
                    pass
            
            if diameterFound == False:
                if row1[0].strip() == "Outside Diameter":
                    diameter = row2[0].strip()
                    if "millimeters millimeters" in diameter:
                        diameter = diameter.split()
                        diameter = diameter[0:2]
                        diameter = ' '.join(diameter)
                        diameterFound = True
                    diameterFound = True
                else:
                    pass
    
    r = open("C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Temp.csv" , 'a')
    #filametentAttr = (brand + ", " + color.upper() + ", " + material.upper() + ", " + weight + ", " + diameter)
    y = (brand + ", " + color.upper() + ", " + material.upper() + ", " + weight + ", " + diameter + ", " + URL)
    #writes all the data to a master file

    
    filList.append(y)
    bar.next()
                
    i += 1
filList = list(dict.fromkeys(filList))
r.writelines(filList)
print("Done")
urlFetch_Done = True
bar.finish()
