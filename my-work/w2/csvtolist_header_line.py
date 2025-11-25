# csvtolist.py
# This program reads in the data from 'data.csv' file and outputs each line as a list. 
# Author : Maroua EL imame


# 1) read data

import csv
FILENAME= "data.csv"
DATADIR =  '../w2/'
# locate the file location using cmd, then use the following format to locate directory 

# 3) Modify the program to deal with the header line separately


with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount: # first row ie header row
            print (f"{line}\n-------------------")
    else: # all subsequent rows
        print (line)
        linecount += 1




