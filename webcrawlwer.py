import urllib.request,urllib.parse, urllib.error 
from bs4 import BeautifulSoup 
import ssl
import re
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input("Enter -")
position=input('enter position:')
count=input('Enterno:')
while float(count)>0:
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    print('Retrieving:',tags[(int(position)-1)].get('href',None))
    url=tags[(int(position)-1)].get('href',None)
    count=float(count)-1
    #for tag in tags:
        #if 
#print(tags[2])
#print(type(tags))