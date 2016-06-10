import requests
from bs4 import BeautifulSoup

file = open("names.txt", 'r')
f = file.read()

domains = f.split("\n")

file = open("key.txt", 'r')
lines = file.read()
lines = lines.lower()
key = lines.split("\n")
#print(lines)

blue = []


agent = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

for d in range(len(domains)):
    hits = 0
    try:
        response = requests.get('http://' + domains[d], headers = agent)

        blue = response.text
        blue = BeautifulSoup(blue, 'html.parser')
        blue = blue.get_text()
        blue = blue.lower()
        purple = blue.split(" ")
        red = blue
        
        #print(blue)
        
        #for x in range(len(purple)):
            
        for n in range(len(key)):
            
            hits += red.count(key[n])

        if hits > 0:
            print(domains[d], end = "\t")
            print(hits)
    except:
        #print(domains[d], "unretrievable")
        print('-')


# Model for single keyword
"""
wills = 0
for x in range(len(red)):
    if "will" in red[x]:
        wills += 1
        #print("will")
print(wills)
"""


