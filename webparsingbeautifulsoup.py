import urllib.request,urllib.parse, urllib.error 
from bs4 import BeautifulSoup 
import ssl
import re
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input("Enter -")
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
su=0
lst=[]
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print(type(tag))
    #print(tag.contents[0])
    lst.append(tag.contents[0])
    su=su+float(tag.contents[0])
    #print('URL:', tag.get('span', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
#print(lst)
print(su)