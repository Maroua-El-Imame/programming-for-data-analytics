# assignment02-bankholdiays.py
# Northern bank holidays
# 1st part of program prints out the dates of the bank holidays that happen in northern Ireland.

# Author: Maroua EL imame 

# Import requests module library used to send HTTP requests and interact with web resources. 
import requests
# The URL we want to send the request to, in other words, we retrieve the data needed from the url provided
url =" https://www.gov.uk/bank-holidays.json"
# Sent request to the website and get its data
response = requests.get(url)
# convert the website's json data to dictionary in Python
data = response.json()
# only get bank holidays specific to Northern Ireland
print(data['northern-ireland']) 


# 2nd part, is modified program that prints out the bank holidays which are unique to northern Ireland (i.e. do not happen elsewhere in the UK) 

