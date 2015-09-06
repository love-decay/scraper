from bs4 import BeautifulSoup
import requests
import filecmp
#import os


kimsufiIndex = requests.get("https://kimsufi.com/en/")
soup = BeautifulSoup(kimsufiIndex.content,"html5lib")
kimsufiList = soup.find_all("tr")
kimsufiSk10 = kimsufiList[7]
repr(kimsufiSk10)
file = open("update.txt","w")
file.write(repr(kimsufiSk10))
file.close()
#filecmp.cmp('update.txt','oldfile.txt')
if filecmp.cmp('oldfile.txt','update.txt') == True:
	print ('do nothing')
else:
    exec (sms.py)


