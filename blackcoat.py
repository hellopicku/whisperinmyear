import requests
from random import choice
from string import ascii_uppercase
import time
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import threading
import re



s = requests.Session()
response = s.get('http://mpets.mobi/welcome', proxies={"https": "https://149.56.102.220:3128"})
d = s.cookies.get_dict()
payload = {"name":"Агент №7", "password":"59294"}
response = requests.post("http://mpets.mobi/login", payload, cookies=d, proxies={"https": "https://149.56.102.220:3128"})

#eat
for x in range(0,9000):
	processfood = 1
	while processfood <= 3:
		response = requests.get("http://mpets.mobi/?action=food&rand=8447", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/?action=food&rand=6460", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/?action=food&rand=6460", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/?action=food&rand=6460", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/?action=food&rand=6460", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/?action=play&rand=6951", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/?action=play&rand=6951", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/?action=play&rand=6951", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/?action=play&rand=6951", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/?action=play&rand=6951", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/show?start=1", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/show", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/show", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/show", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/show", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/show", cookies=d)
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/", cookies=d)
		#wakeup
		time.sleep(0.4)
		response = requests.get("http://mpets.mobi/wakeup", cookies=d)
		processfood = processfood + 1
	time.sleep(7300)

#################################################################
