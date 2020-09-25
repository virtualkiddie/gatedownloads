#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import subprocess

year = str(input("Enter year :"))
Q = int(input("Enter question no :"))

for qn in range(1,Q):
    qs = "0"+str(qn)
    url = "https://unitoperation.com/Gate/Gate%s/Gate%sSolution/%sq%s.htm" % (year,year,year,qs)
    url1 ="https://unitoperation.com/Gate/Gate%s/Gate%sSolution/" % (year,year)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
    cookies = {"PHPSESSID": "fbd6978203272251d6de8db75d627544"}

    response = requests.get(url, cookies=cookies, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    aas = soup.find_all("img")

#print(aas)

    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))

#print(url1+str(images[0]),url1+str(images[1]))
    for a in images:
        b = url1+str(a)
        subprocess.call(['wget',b,'-P',qs])
    #print(b)