#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import csv
import ssl
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def write_category(cat):
    category = cat
    url = 'https://www.dawn.com/{cat}'.format(cat=category)
    html = urlopen(url, context=ctx).read()
    fetch_soup = BeautifulSoup(html,'html.parser')
    
    fetch_headlines = fetch_soup.find_all("article", class_="story")
    fetch_array = [];
    
    for f in fetch_headlines:
        cur_soup = f
        cur_head = cur_soup.find("div", class_="story__excerpt")
        if cur_head:
            value = cur_head.text
            fetch_array.append([value.strip()])
            
    print(*fetch_array, sep='\n')
    print("Headlines_Fetched : "+str(len(fetch_array)))
    with open("output.txt", "w",encoding='utf-8') as txt_file:
        for i in fetch_array:
            txt_file.write(''.join(i)+"\n") 

write_category('latest-news')

