import glob, os, shutil, csv

color = "BLACK"

f = open("C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Temp.csv" , 'r')
q = open(f"C:\\Users\\kpat8\\Desktop\\Scraper\\Filament\\'{color}'.csv" , 'a')
g = open("C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\OverflowData.csv" , 'a')


for x in f:
    finder = x.find(color)
    if finder == -1:
        g.writelines(x)
    else:
        q.writelines(x)

fileSort_Done = True


    
    

