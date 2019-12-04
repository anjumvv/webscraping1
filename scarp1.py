import requests as req
import re
from bs4 import BeautifulSoup as bs

res=req.get ("http://www.expertzlab.com/contact.php")
#data = res.text
#nums= re.findall(r"[0-9]{10}", data)
#print (nums)


soup = bs(res.text)
contacts = soup.findAll('div', attrs={'class': 'contact-info'})
data=  contacts[2].text
print (data)
nums= re.findall(r"[0-9]{10}", data)
print (nums)

