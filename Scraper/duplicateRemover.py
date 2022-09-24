# This program opens file bar.txt and removes duplicate lines and writes the
# contents to foo.txt file.
lines_seen = set()  # holds lines already seen
outfile = open('PLA_links3.txt', "w")
infile = open('C:\\Users\\kpat8\\Desktop\\Scraper\\Data_Files\\Temp.csv', "r")
print("The file bar.txt is as follows")
for line in infile:
    print(line)
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print("The file foo.txt is as follows")
for line in open('PLA_links3.txt', "r"):
    print(line)