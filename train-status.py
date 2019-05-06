from bs4 import BeautifulSoup
import datetime as dt
import requests
import time

def send(toPhone, message, authkey, senderName):
  message91URL = "http://api.msg91.com/api/sendhttp.php?route=4&sender="+sender+"+&mobiles="+toPhone+"&authkey="+authkey+"&message="+message+"&country=91"
  requests.request('GET',message91URL)

def getLiveStatus(trainNumber,startDate):
  trainStatusURL = "https://trainstatus.info/running-status/20816-vskp-tata-exp-"
  date = dt.datetime.now()
  if startDate!=date.day:
    response = requests.request('GET',trainStatusURL+"yesterday") 
  else:
    response = requests.request('GET',trainStatusURL+"today")

  html = response.text  
  soup = BeautifulSoup(html,'html.parser')
  return soup.find(class_="alert alert-warning").text.strip()

i = 0
startDate = dt.datetime.now()
toPhone = 0 #Recipient's phone number
authkey = "string" #Get your autkey from msg91.com
senderName = "STRING" #The messages will be recieved by: DM-BOOFOO if sender id is BOOFOO
while i<10: 
  message = getLiveStatus(20816,startDate)
  send(toPhone,message,authkey,senderName)
  print i+ " MESSAGE SENT: "+message
  i = i+1
  time.sleep(1200)