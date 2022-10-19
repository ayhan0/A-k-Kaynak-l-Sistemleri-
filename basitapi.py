# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:06:09 2022

@author: adana
"""
import requests
URL = "https://fakerapi.it/api/v1/companies?_quantity=5"

sonuc = requests.get(URL)
veri = sonuc.json()
print(veri)
