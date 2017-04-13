import requests
from bs4 import BeautifulSoup as soup
import re


ming= "https://yeezysupply.com/cart/add.js"
ing0 = "https://yeezysupply.com/"
ing1= "https://yeezysupply.com/collections/"

def secondtest3b(url, tags):
          r = requests.get(url)
          s = soup(r.content)
          t = s.find_all(tags)
          u = str(t[2])
          v = (re.findall(r'[a-z]*1', u))
          return v[0]
          
def test5(url, tags):
         r = requests.get(url)
         souping = soup(r.content)
         return souping.find_all(tags)

ing2 = secondtest3b("http://yeezysupply.com","script")
mix1 = ing1 + ing2
ing3 =str(test5(mix1, "a"))
mix2= (re.findall(r'/products/[a-z0-9]*',ing3))
fmix2 = mix2[0]
truemix2= ing0 + fmix2

def secondtest3d1(url, tags):
                r = requests.get(url)
                s = soup(r.content)
                t = s.find_all(tags)
                u = str(t)
                v = (re.findall(r'\d{11}', u))
                return v
     
def secondtest4(item):
        for item in ing4:
          if item != ing4[0]:
              return item

ing4 = secondtest3d1(truemix2, "script")
ing5 = (re.findall(r'id:/s*/d{11}', ing4))
mix3 = secondtest4(item)
fmix3 = mix3[:11]
payload = {"quantity": "1", "id": fmix3}
pming = requests.post(ming, json =payload)








     
     
