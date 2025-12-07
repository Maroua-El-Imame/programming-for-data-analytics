# assignment02-bankholdiays.py
# Northern bank holidays
# 1. first part of program prints out the dates of the bank holidays that happen in northern Ireland.
# 2. Second part, modified program that prints out the bank holidays which are unique to northern Ireland (i.e. do not happen elsewhere in the UK) 


# Author: Maroua EL imame 

# Part 1 : 
import requests
url =" https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print("\n")
print("=== ALL Northern Ireland Bank Holidays ===")
print("\n")


for event in data['northern-ireland']['events']:
    print(f"{event['title']} on {event['date']}")

# Part 1: Code explained
# Import requets module library which is used to send HTTP requests and interact with web resources. 
# assign a Url variable to the URL we want to send the request to, in other words, we send the request to the website and get its data the data.  
# convert the website's json data to dictionary in Python
# only get bank holidays specific to Northern Ireland
# I used a for-loop to iterate through each event in the Northern Ireland events list and printed both the title and date for every bank holiday.


# Part 2 : 
# https://realpython.com/python-sets/
# https://docs.python.org/3/library/stdtypes.html#set.add
# Chat GPT & Deep seek : AI provided conceptual explanations of SET operations, it was used as a learning aid to understand:
# Set operations (union, difference) in Python
# Set comprehension syntax


print("\n")
print("=== UNIQUE Northern Ireland Bank Holidays ")
print("\n")

# create sets (with .add() automatic duplicate removal)
england_set = set()
scotland_set = set()

for event in data['england-and-wales']['events']:
    england_set.add(event['date']) 

for event in data['scotland']['events']:
    scotland_set.add(event['date'])

# combine sets
all_other_dates = england_set | scotland_set  # | is the union operator

for event in data['northern-ireland']['events']:
    if event['date'] not in all_other_dates:
        print(f"{event['title']} on {event['date']}")