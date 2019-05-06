from bs4 import BeautifulSoup
import datetime as dt
import requests
import time

def send(toPhone, message, authkey, senderName):
  #Get your autkey from msg91.com
  #Sender name should be a alpha-numeric of 6 characters
  #The messages will be recieved by: DM-BOOFOO if sender id is BOOFOO
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
while i<10:
  message = getLiveStatus(20816,startDate)
  send(9122517027,message)
  print "MESSAGE SENT: "+message
  i = i+1
  time.sleep(1200)