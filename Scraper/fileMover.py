import shutil

color = "Yellow"

final_file = f'C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\{color}.csv'
f = open(final_file , 'w')
temp_file = 'C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Temp.csv'


shutil.copy2(temp_file, final_file)

#open(temp_file, 'w').close()

fileMover_Done = True