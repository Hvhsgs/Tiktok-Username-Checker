from user_agent import generate_user_agent
from colorama import Fore, init
from datetime import datetime
import requests
import aiohttp
import asyncio
import json
import time
import os
import random
from colorama import Fore, Back, Style

os.system('clear')
 



user = 'abcdefghijklmnopkrstuvwxyz1234567890'



print (Fore.RED + '''     By

 ______     ______     ______    
/\  == \   /\  __ \   /\  __ \   
\ \  __<   \ \ \/\ \  \ \ \/\ \  
 \ \_____\  \ \_____\  \ \_____\ 
  \/_____/   \/_____/   \/_____/ 
                                 
a simple Tiktok username checker.

''')







def numf():
  while True:
  	us = str(''.join(random.choice(user)for i in range (4)))
  	s = requests.Session()
  	r = s.get("https://www.tiktok.com/@"+us+"")
  	check = r.status_code
  	if check == 404:
  		print(Fore.GREEN + "Available ! :", us)
  	elif check == 200 or 204:
  		print(Fore.RED + "unavailable", us)
  	elif check == 429:
  		print(Fore.YELLOW + "wait, ")








   	
   	
   	
   	
def numff():
  while True:
  	us = str(''.join(random.choice(user)for i in range (5)))
  	s = requests.Session()
  	r = s.get("https://www.tiktok.com/@"+us+"")
  	check = r.status_code
  	if check == 404:
  		print(Fore.GREEN + "Available ! :", us)
  	elif check == 200 or 204:
  		print(Fore.RED + "unavailable", us)
  	elif check == 429:
  		print(Fore.YELLOW + "wait, ")







def nums():
  while True:
  	us = str(''.join(random.choice(user)for i in range (6)))
  	s = requests.Session()
  	r = s.get("https://www.tiktok.com/@"+us+"")
  	check = r.status_code
  	if check == 404:
  		print(Fore.GREEN + "Available ! :", us)
  	elif check == 200 or 204:
  		print(Fore.RED + "unavailable", us)
  	elif check == 429:
  		print(Fore.YELLOW + "wait, ")
  		
  		
def numss():
  while True:
  	us = str(''.join(random.choice(user)for i in range (7)))
  	s = requests.Session()
  	r = s.get("https://www.tiktok.com/@"+us+"")
  	check = r.status_code
  	if check == 404:
  		print(Fore.GREEN + "Available ! :", us)
  	elif check == 200 or 204:
  		print(Fore.RED + "unavailable", us)
  	elif check == 429:
  		print(Fore.YELLOW + "wait, ")
  		

  		
  		
  		
  		
      	
  	
been = input('{01} Tiktok Username Checker\n{02} About\nChoose :  ')
if been == '1':
	roll = input('username length (from 4 to 7) : ')
	if roll == '4':
		os.system('clear')
		numf()
	elif roll == '5':
		os.system('clear')
		numff()
	elif roll == '6':
		os.system('clear')
		nums()
	elif roll == '7':
		os.system('clear')
		numss()
elif been ==  '2':
	print('''
	by boo271
	join my discord !
	https://discord.com/invite/dvNPRfGh
	
	''')
	
	
	



	

 	
	
	
	
	
