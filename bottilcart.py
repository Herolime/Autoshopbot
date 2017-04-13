import requests
from bs4 import BeautifulSoup as soup
import re

ming = "https://yeezysupply.com/cart/add.js"
ing0 = "https://yeezysupply.com/"
ing1 = "https://yeezysupply.com/collections/"


def getPrefix(url, tags):
    r = requests.get(url)
    s = soup(r.content, 'html.parser')
    t = s.find_all(tags)
    u = str(t[2])
    v = re.findall(r'[a-z]*1', u)[0]
    return v


def getTagFromURL(url, tags):
    r = requests.get(url)
    souping = soup(r.content, 'html.parser')
    return souping.find_all(tags)


def getID(url, tags):
    r = requests.get(url)
    s = soup(r.content, 'html.parser')
    t = s.find_all(tags)
    u = str(t)
    v = re.findall(r'\bid\s*:\s(\d{11}),\s*parent_id', u)[0]
    return v


ing2 = getPrefix("http://yeezysupply.com", "script")
mix1 = ing1 + ing2
ing3 = str(getTagFromURL(mix1, "a"))
mix2 = re.findall(r'/products/[a-z0-9]*', ing3)
fmix2 = mix2[0]
truemix2 = ing0 + fmix2
ing4 = getID(truemix2, "script")

payload = {"quantity": "1", "id": ing4}
pming = requests.post(ming, json=payload)
print(pming.text)
