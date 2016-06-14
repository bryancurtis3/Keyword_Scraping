import requests
import sys, os
from bs4 import BeautifulSoup

path = str(sys.argv[0])
path = path.replace("scraping.py", '')

now = "names.txt"
now = path + now
file = open(now, 'r')
f = file.read()
domains = f.split("\n")

keyfile = "key.txt"
keyfile = path + keyfile
file = open(keyfile, 'r')
lines = file.read()
lines = lines.lower()
key = lines.split("\n")

agent = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

for d in range(len(domains)):
    hits = 0
    try:
        response = requests.get('http://' + domains[d], headers = agent)
        
        blue = response.text
        blue = BeautifulSoup(blue, 'html.parser')
        blue = blue.get_text()
        blue = blue.lower()
        red = blue
        
        
        for n in range(len(key)):
            hits = 0
            loc = 0
            hits = red.count(key[n])
            loc = red.find(key[n])


            if hits > 0:
                print(domains[d], "\t", key[n] + ":", hits)
                
            if loc != -1:
                for j in range(hits):
                    num = j+1
                    surround = red[loc-100:loc+100]
                    surround = surround.replace("\n", '')
                    surround = surround.replace("\t", '')
                    print("Hit %d:" % num)
                    print(surround, "\n----------------------------------------")
                    loc = red.find(key[n], loc + len(key[n]))
                                
    except:
        print(domains[d], "unretrievable")
