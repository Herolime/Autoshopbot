import requests
from bs4 import BeautifulSoup as soup
import re


class YeezySupply:
    name = ""
    customer_info = {}

    ming = "https://yeezysupply.com/cart/add.js"
    ing0 = "https://yeezysupply.com/"
    ing1 = "https://yeezysupply.com/collections/"

    def __init__(self, cust_info):
        self.customer_info = cust_info

    def getPrefix(self, url, tags):
        r = requests.get(url)
        s = soup(r.content, 'html.parser')
        t = s.find_all(tags)
        u = str(t[2])
        v = re.findall(r'[a-z]*1', u)[0]
        return v

    def getTagFromURL(self, url, tags):
        r = requests.get(url)
        souping = soup(r.content, 'html.parser')
        return souping.find_all(tags)

    def getID(self, url, tags):
        r = requests.get(url)
        s = soup(r.content, 'html.parser')
        t = s.find_all(tags)
        u = str(t)
        v = re.findall(r'\bid\s*:\s(\d{11}),\s*parent_id', u)[0]
        return v

    def add_to_cart(self, url):
        ing2 = self.getPrefix("http://yeezysupply.com", "script")
        mix1 = self.ing1 + ing2
        ing3 = str(self.getTagFromURL(mix1, "a"))
        mix2 = re.findall(r'/products/[a-z0-9]*', ing3)
        fmix2 = mix2[0]
        truemix2 = self.ing0 + fmix2
        ing4 = self.getID(truemix2, "script")

        payload = {"quantity": "1", "id": ing4}
        pming = requests.post(self.ming, json=payload)
        print(pming.text)

if __name__ == '__main__':
    bot = YeezySupply({})

    bot.add_to_cart("")

