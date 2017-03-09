from __future__ import print_function
raw_input()

import urllib2
import sys
import bs4
import requests
import re
print("Do not put 'https://' in form below")
print()

while True:
    userinput = raw_input("select website: ")

    site = str(userinput).strip()

    hdr = {'User-Agent': 'Mozilla/5.0'}


    req = urllib2.Request("https://" + site,headers=hdr)





    try:
        page = urllib2.urlopen(req)
    except urllib2.URLError:
        print("website you enter is not valid")
        print("Now exiting")
        raw_input()
        break

    soup = bs4.BeautifulSoup(page,"html.parser")

    soup = soup.findAll("p")



    soup = re.sub('<[^>]+>', '', str(soup))
    soup = soup.replace("\\u2013","")
    soup = soup.replace("\\n","")
    soup = soup.replace(",","")
    soup = soup.strip("[")
    soup = soup.strip("]")
    soup = soup.split(" ")

    i = 0
    x = 0

    for each in soup:

        print (soup[i], end=' ')

        if x > 100:
            print ("\n")
            x = 0

        i = i + 1
        x = x + 1
    raw_input()