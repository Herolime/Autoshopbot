import requests
from bs4 import BeautifulSoup as soup
import re


ming= "https://yeezysupply.com/cart/add.js"
ing0 = "https://yeezysupply.com/"
ing1= "https://yeezysupply.com/collections/"
testingdictionary= {'checkout[shipping_address][phone]': '646-667-6061', 'checkout[shipping_address][province]': 'New+York', 'checkout[shipping_address][first_name]': 'Kelli', 'checkout[shipping_address][last_name]': 'Fultz', 'utf8': '%E2%9C%93', 'authenticity_token': 'hBGHzgql2taTbhk+MeEm+avvTfT0Jx+bgHf11SFDLmfke+DJVenoQCnU+dTGX7uIsICrr0fM32E1J9WTJtVprg==', 'checkout[shipping_address][zip]': '10013', 'checkout[shipping_address][city]': 'New+York', "'checkout[shipping_address][province]": 'New+York', 'checkout[shipping_address][country]': 'United+States', 'checkout[email]': 'Kelli@outlook.com', 'checkout[remember_me]': '0', 'step': 'contact_information', 'previous_step': 'contact_information', 'checkout[shipping_address][address1]': '2666+Cantebury+Drive', 'checkout[shipping_address][address2]': '', '_method': 'patch'}

def getpage(url, tags):
          r = requests.get(url)
          s = soup(r.content, 'html.parser')
          t = s.find_all(tags)
          u = str(t[2])
          v = (re.findall(r'[a-z]*1', u))
          return v[0]
          
def getproduct(url, tags):
         r = requests.get(url)
         souping = soup(r.content, 'html.parser')
         return souping.find_all(tags)

ing2 = getpage(ing0,"script")
mix1 = ing1 + ing2
ing3 =str(getproduct(mix1, "a"))
mix2= (re.findall(r'/products/[a-z0-9]*',ing3))[0]
truemix2= ing0 + mix2

def getid(url, tags):
                r = requests.get(url)
                s = soup(r.content, 'html.parser')
                t = s.find_all(tags)
                u = str(t)
                v = (re.findall(r'\d{11},', u))
                return v
     
def getcart():
        for item in ing4:
          if item != ing4[0]:
              return item

ing4 = getid(truemix2, "script")
mix3 = getcart()
fmix3 = mix3[:11]
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
ing8= ses.get(mix6[1])
""" parte del codigo que necesita revision"""
ingcookies= ing8.cookies
ing9= soup(ing8.content, 'html.parser')
mix7= ing9.find_all("input")
ing10= str(mix7)
mix8=str(re.findall('\S{60,}', ing10))
ing11= re.split('"',mix8)
mix9=list(filter(lambda x: len(x) > 60, ing11))
testingdictionary["authenticity_token"] = mix9[2]
ingcookiesB= {"_secure_session_id": ingcookies["_secure_session_id"], "_shopify_s":ingcookies["_shopify_s"], "_shopify_y": ingcookies["_shopify_y"], "checkout": ingcookies["checkout"], "checkout_token": ingcookies["checkout_token"]}
"""session no se mantiene, por lo cual puse las cookies manualmente, aun asi al cargar r6.text, parece que los parametros que envie en el r4 no se mantienen"""
r4=s.post(peace[1], data= testingdictionary, allow_redirects = True,cookies=ingcookiesB )
r5=s.get(peace[1], params= testingdictionary)
r6=s.get(peace[1], params= {"previous_step": "contact_information", "step": "shipping_method"})
r6.text
