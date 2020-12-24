#!/bin/env python3
# code by : Termux Professor

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	
	           Version : 1.01
	{re}Subscribe Termux Professor on Youtube
	{cy}www.youtube.com/c/TermuxProfessorYT
	""")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()

arrID = ["2595129","2702860","2571773","2099015","2820582","2774760","2105180","2135062","2493830","2956409"]
arrHash = ["87cfcd74afe6f5426d12688255e7fa5b","965baa755f16ff404ab7085e395cd6fa","55af1d3cc9fae3acf2d41f501a86dc1d","0cd4851463ff8fbe324a75262219e5cd","608467942ca6327024b2064464ba099b","ee41572c05390c23c33da5e9fd3056f3","a96238e419ed32156470fab327fa7a65","7d7fdbd6b2d51f58986caa49ad2c46f2","2d0db19d37ea32795713ec0a5a08ad1e","09fcc94d68e11eba09032d37164dcae6"]
arrPhone = ["+923317664323","+13859882097","+923117141422","+923000686958","+18018767206","+13372452783","+12282804404","+923017969700","+923135739957","+13366076682"]

for x in range(0, 11):
	a = "touch config"
	b = str(x)+".data"
	c = a+b
	os.system(c)
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = arrID[x]
	cpass.set('cred', 'id', xid)
	xhash = arrHash[x]
	cpass.set('cred', 'hash', xhash)
	xphone = arrPhone[x]
	cpass.set('cred', 'phone', xphone)
	setup = open("config"+b, 'w')
	cpass.write(setup)
	setup.close()
print(gr+"[+] setup complete !")
print(gr+"[+] now you can run any tool !")
print(gr+"[+] make sure to read docs 4 installation & api setup")
print(gr+"[+] https://github.com/termuxprofessor/TeleGram-Scraper-Adder/blob/master/README.md")
