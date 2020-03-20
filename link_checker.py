#!/bin/bash env python


#check links within category page descriptions are working

import urllib2
import urllib
from bs4 import BeautifulSoup
import csv
import requests


origin = "https://www.cs-catering-equipment.co.uk/category_crawler"
get_origin = urllib2.urlopen(origin)
soup = BeautifulSoup(get_origin, 'html.parser')   

links = soup.findAll('a', class_='listcats')


for link in links:
    try:
      get_page = urllib2.urlopen(link['href'])
      soup = BeautifulSoup(get_page, 'html.parser')
      desc = soup.find('div', class_='category-description')
      desc.findAll('a')
      extra_links = desc.findAll('a')
    except:
      continue  
      
    for hyper in extra_links:
        if hyper['href'][0] == '/':
            try:
                r = requests.head('https://www.cs-catering-equipment.co.uk' + hyper['href'])
                if r.status_code == 404:
                    print "Found: " + link['href']
            except:
                continue        
        
        elif hyper['href'][0] != 'h' and hyper['href'][1] != 't':    
            try:
                if requests.head('https://www.cs-catering-equipment.co.uk/' + hyper['href']):
                    r = requests.head('https://www.cs-catering-equipment.co.uk/' + hyper['href'])
                    if r.status_code == 404:
                        print "Found: " + link['href']
            except:
                continue              
        else:              
            if requests.head(hyper['href']):
                try:
                    r = requests.head(hyper['href'])
                    if r.status_code == 404:
                        print "Found: " + link['href']
                except:
                    continue                 
