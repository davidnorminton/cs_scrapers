#!/bin/bash env python
from bs4 import BeautifulSoup
import urllib2
import re
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


website = 'https://www.cs-catering-equipment.co.uk/attributes/bundles/all/index.php'
openSite = urllib2.urlopen(website)

found = []
error_sites = []

soup = BeautifulSoup(openSite, 'html.parser')
for link in soup.findAll('a'):
    found.append(link.get('href'))



for link in found:
    content = urllib2.urlopen(link)
    soup = BeautifulSoup(content, 'html.parser')   
    
    buy_btn = soup.findAll('button', class_='cart-btn')
    
    if(not buy_btn):
         if(not soup.findAll(text='out of Stock')):
          
            error_sites.append(link)
            print link
         
         
if error_sites:
    message = ', '.join(str(x) for x in error_sites)
else:
    message = "No errors to report!"    
            
print message           
        



 
 
fromaddr = "cscateringerrors@gmail.com"
toaddr = "marketing@caffesociety.co.uk"
msg = MIMEMultipart('alternative')
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Bundles with no buy button"
 
body = "<html><head></head><body><h1>Bundles with no buy buttons</h1>" + message + "</body></html>"
msg.attach(MIMEText(body, 'html'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "F1ft33np3nc3")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print(body)
