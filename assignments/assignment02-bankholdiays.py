# assignment02-bankholdiays.py
# Northern bank holidays
# 1. first part of program prints out the dates of the bank holidays that happen in northern Ireland.
# 2. Second part, modified program that prints out the bank holidays which are unique to northern Ireland (i.e. do not happen elsewhere in the UK) 


# Author: Maroua EL imame 

# Part 1 : 
# Import requests module library, it is used to send HTTP requests and interact with web resources. 
import requests
# The URL we want to send the request to, in other words, we retrieve the data needed from the url provided
url =" https://www.gov.uk/bank-holidays.json"
# Sent request to the website and get its data
response = requests.get(url)
# convert the website's json data to dictionary in Python
data = response.json()
# only get bank holidays specific to Northern Ireland
for event in data['northern-ireland']['events']:
    print(f"{event['title']} on {event['date']}")

# Part  
