#!/bin/bash env python

import urllib2
import urllib
from bs4 import BeautifulSoup
import csv


origin = "https://www.cs-catering-equipment.co.uk/brands"
get_origin = urllib2.urlopen(origin)
soup = BeautifulSoup(get_origin, 'html.parser')   

brands = soup.findAll('li', class_='list_1')

pages = []
subcat_urls = []
no_cats = []

for brand in brands:
    category = brand.find('a')['href']
    if category not in pages:
        pages.append(category)
  
for page in pages:
    print page
    try:
      #print page
      get_page = urllib2.urlopen(page)
    except:
        print "cant"   
    soup = BeautifulSoup(get_page, 'html.parser')
    subs = soup.find('a', class_='categories-list-products')['href']
    print "number of cats " + len(subs)
    if not subs:
      no_cats.append(page)
 
        
for cat in no_cats:
    print cat           
