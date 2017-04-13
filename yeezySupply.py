import requests
from bs4 import BeautifulSoup as soup
import re


class YeezySupply:
    name = ""
    customer_info = {}

    def __init__(self, cust_info):
        self.customer_info = cust_info
