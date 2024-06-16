# by aritrasa 
# instagram [0aritrasa1]

import time , os , sys


try:
	import requests

except:
	os.system('pip3 install requests')
	time.sleep(1)
	os.system('clear')
			



DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'


def hello():
	os.system('clear')
	print("Checking required pakages to install")
	time.sleep(2)

while True:
	link = input(f"{GREEN}• The link [ :  {END}") 
	if  'https://' in link or 'http://' in link :
		print(f"{DARKCYAN}Processing...{END}")
		break
		
		
	else:
		os.system('clear')
		print(f"{BOLD}{RED}Start with\n[http://]     or        [https://]{END}")
		continue


x = f'{link}'
try:
	data = requests.get(x)
	html = data.text
	
except requests.exceptions.InvalidURL as e:
    print(f"{RED}! Invalid URL error: {e}{END}")
    sys.exit()
except requests.exceptions.HTTPError as e:
    print(f"{RED}! HTTP error: {e}{END}")		
    sys.exit()

while True:
	cont = input(f"\n{GREEN}Do you wanna continue [Y/n] : {END}")
	
	if cont =='y' or cont =='Y' or cont=='':
		break
		
	elif cont =='n' or cont =='N':
		sys.exit()
			
	else:
		print(f"{BOLD}{RED}! Wrong input{END}")
		os.system('clear')
	continue
	
	
while True:
	filename  = input(f"{GREEN}¥ filename  [: {END}").strip()
	if filename == "":
		print(f"{RED}filename cannot be blank{END}")
		time.sleep(1)
		os.system('clear')
		continue 
		
	else:
		break	

with open (f"{filename}.html", "a") as file:
	file.write(f"{html}")
	file.close()
	
	
time.sleep(2)
		
os.system('clear')
print(f"{DARKCYAN}▪︎ ¥ [{filename}.html] saved in storage {END}")

if __name__ == "__main__":
		hello()
