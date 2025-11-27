# quiz:
# 1. Look at the following code, it searches through a file and prints out the lines that
# have some text that matches the regular expression in the variable regex.
# In this case it will print out the entire file quiz.txt



# code 

'''
import re 

regrex = ".*"
filemame = "./sample-files/quiz.txt"

with open(filemame) as quizfile:
    for line in quizfile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingline = line
        print (matchingline, end = "")
'''

# What lines will be printed out for the following regular expressions? Note that regular expressions in python are case sensitive

# input 
'''
1. hello
2. Hello
3. Hello World
4. Helo John
5.        Hello mary
6. Helllllllllllo Anamaniacs
7. var = 123
8. change this #this will change
9. what [about] this.
'''
# output , I could only fidn the anwsers to a - e
'''
a. hello >> line 1
b. Hello >> line 2, 3 & 5
c. ^Hello >> line 2 & 3 ( ^ referts to the first charchter, here the first character is Hello)
d. ^Hell*o >> line 2 , 3, 4 & 6 () * is any character repeated 0 or more times. )
e. ^Hell+o >> line 2 , 3 & 6 ( starts with Hell  + letter o )
f. ^Hell?o >> line 2 , 3 & 6 ( starts with Hell  ? letter o in any order  )
g. ^hello [A-Z]
h. ^Hello [A-Z]
i. =
j. #
k. [
l. ^$
'''

# quizz result in Lab

'''
Answers to quiz
a. hello Line 1
b. Hello Lines 2,3,5 (not 4 or 6)
c. ^Hello Lines 2, 3 (not 5 because it does not start with Hello)
d. ^Hell*o Lines 2,3,4,6 (* is 0 or more times)
e. ^Hell+o Lines 2,3,6 (plus is 1 or more times)
f. ^Hell?o Lines 2, 3,4 (? Is 1 or more times)
g. ^hello [A-Z] No lines (there is not a hello with a capital after.)
h. ^Hello [A-Z] Line 3
i. = Line 7
j. # Line 8
k. [ Error [ is special it should have been escaped \[
l. ^$ Line 10 it contains nothing
... 