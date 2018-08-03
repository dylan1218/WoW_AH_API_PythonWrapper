import socket
import json
import requests

#Note to self, remove IP argument and check impact on class

#This iniatializes the attributes of the class
class AuctionHouse(object):	
	def __init__(self, Realmname, APICode, IP):
		self.Realmname = Realmname
		self.APICode = APICode
		self.IP = IP
	
	#Class function which obtains the users IP adress which is fed to the Blizzard endpoint as a required API argument
	def get_Host_name_IP(self):
		try:
			host_ip = requests.get('http://ip.42.pl/raw').text
			return host_ip
		except:
			print("Unable to get Hostname and IP")
	
	#The first step of the Blizzard API is to get the latest realm upload. This gets the latest upload URL and and returns it in this function 
	def Get_Data_URL(self):
		try:
			Realm = self.Realmname
			API = self.APICode
			baseurl =f'https://us.api.battle.net/wow/auction/data/{Realm}?locale=en_US&apikey={API}'
			headers = {'X-Originating-IP': str(AuctionHouse.get_Host_name_IP('self'))}
			r = requests.get(baseurl, headers=headers)
			JsonData = r.json()
			for files in JsonData['files']:
				return files['url']
		except:
			print(r)
	#This class function utilizes the URL obttained from Get_Data_URL. All of the selected realms AH data is loaded to a Json dictionary 
	#If there is an error the URL status is returned (i.e. 404 or whatever is applicable)
	def GetFullAH(self):
		try:
			url = str(self.Get_Data_URL())
			r = requests.get(url)
			JsonData = r.json()
			return JsonData
		except:
			print(r)
		
			
	
