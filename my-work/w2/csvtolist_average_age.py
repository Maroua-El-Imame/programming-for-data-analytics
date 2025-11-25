# csvtolist.py
# This program reads in the data from 'data.csv' file and outputs each line as a list. 
# Author : Maroua EL imame


# 1) read data

import csv
FILENAME= "data.csv"
DATADIR =  '../w2/'
# locate the file location using cmd, then use the following format to locate directory 


with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row ie header row
            pass
        else: # all subsequent rows
            total += int(line[1]) # why 1
    linecount += 1
    print (f"average is {total/(linecount-1)}") # why -1 ?


# T-1 is like telling python not to cound header. The csv fiel counts 4 lines with header included, need to be removed so the age column is treated as integers.  