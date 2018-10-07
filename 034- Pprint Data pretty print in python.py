'''
    #### pprint data pretty print in python ####
    -The pprint module provides a capability to “pretty-print”
    -arbitrary Python data structures in a well-formatted and more readable way!
    

'''

# A python code with pprint
import requests
from pprint import pprint

def geocode(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    resp = requests.get(url, params = {'address': address})
    return resp.json()

# calling geocode function
data = geocode('google')

# pretty-printing json response
pprint(data)
