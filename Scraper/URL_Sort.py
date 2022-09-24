import os, csv

f = open("C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Links_Cache.txt", "r")


complete_clear = open("C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Links_Cache_ORG.csv" , 'w').close()
complete = open("C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Links_Cache_ORG.csv", "w")


for x in f:
    finder = x.find("/gp/slredirect/picassoRedirect")
    if finder == -1:
        complete.write(x)

URL_Sort_Done = True