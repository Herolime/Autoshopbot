import requests
from bs4 import BeautifulSoup as soup
import re

def getPrefix(url, tags):
    r = requests.get(url)
    s = soup(r.content, 'html.parser')
    t = s.find_all(tags)
    u = str(t[2])
    v = re.findall(r'[a-z]*1', u)
    return v[0]


def getTagFromURL(url, tags):
    r = requests.get(url)
    souping = soup(r.content, 'html.parser')
    return souping.find_all(tags)


def getID(url, tags):
    r = requests.get(url)
    s = soup(r.content, 'html.parser')
    t = s.find_all(tags)
    u = str(t)
    v = re.findall(r'\d{11},', u)
    return v
def getcart():
        for item in ing4:
          if item != ing4[0]:
              return item

ming = "https://yeezysupply.com/cart/add.js"
ing0 = "https://yeezysupply.com/"
ing1 = "https://yeezysupply.com/collections/"
ing2 = getPrefix("http://yeezysupply.com", "script")
mix1 = ing1 + ing2
ing3 = str(getTagFromURL(mix1, "a"))
mix2 = re.findall(r'/products/[a-z0-9]*', ing3)[0]
truemix2 = ing0 + mix2
ing4 = getID(truemix2, "script")
mix3= getcart()
fmix3= mix3[:11]
payload = {"quantity": "1", "id": fmix3}
ses= requests.Session()
ses.post(ming, json =payload)
ing5 = "https://yeezysupply.com/cart/"
ses.get(ing5, params={"addProduct": "true"}, allow_redirects= True)
ing6 = ses.post(ing5, json= {"updates[]": "1", "checkout": "CHECK+OUT"}, allow_redirects= False)
mix4= ing6.content
ing7 = soup(mix4, 'html.parser')
mix5 = str(ing7.find_all("a"))
mix6 = re.split(r'"*', mix5)
ing8 = ses.get(mix6[1])
