import os, csv

f = open("masterList2.csv", "r")

complete = open("complete_files.csv", "w")
needsAttention = open("needsAttention.csv", "w")

for x in f:
    finder = x.find("[Needs Human]")
    finder2 = x.find("[NEEDS HUMAN]")
    if finder == -1:
        complete.write(x)
    elif finder2 == -1:
        complete.write(x)
    else:
        needsAttention.write(x)



f.close
complete.close
needsAttention.close




