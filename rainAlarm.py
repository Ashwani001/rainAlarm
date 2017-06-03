#!/usr/bin/env python
from xml.etree import ElementTree as ET
import requests
import pygame, sys

#Usuage: ./rainAlarm.py key
#Idea is to have cron run this peridiocally btw certain times (4-6am for example)

#2-hour Nowcast
twoHrs="http://api.nea.gov.sg/api/WebAPI/?dataset=2hr_nowcast"

#Heavy Rain Warning
#http://api.nea.gov.sg/api/WebAPI/?dataset=heavy_rain_warning

#Key is passed in as arg
#Can replace sys.argv[1] with your key and simply run ./rainAlarm
keyref=sys.argv[1]


url = twoHrs + "&keyref=" + keyref;
r = requests.get(url)
root = ET.fromstring(r.content)


#TODO create different alert lvls, with diff songs
alert = ['DR','HG','HR','HS','HT','LR','LS','OC','PS','RA','SH','SK','SR','TL','WR','WS']

code= { 'BR' : 'Mist',
'CL' : 'Cloudy',
'DR' : 'Drizzle',
'FA' : 'Fair (Day)',
'FG' : 'Fog',
'FN' : 'Fair (Night)',
'FW' : 'Fair & Warm',
'HG' : 'Heavy Thundery Showers with Gusty Winds',
'HR' : 'Heavy Rain',
'HS' : 'Heavy Showers',
'HT' : 'Heavy Thundery Showers',
'HZ' : 'Hazy',
'LH' : 'Slightly Hazy',
'LR' : 'Light Rain',
'LS' : 'Light Showers',
'OC' : 'Overcast',
'PC' : 'Partly Cloudy (Day)',
'PN' : 'Partly Cloudy (Night)',
'PS' : 'Passing Showers',
'RA' : 'Moderate Rain',
'SH' : 'Showers',
'SK' : 'Strong Winds, Showers',
'SN' : 'Snow',
'SR' : 'Strong Winds, Rain',
'SS' : 'Snow Showers',
'SU' : 'Sunny',
'SW' : 'Strong Winds',
'TL' : 'Thundery Showers',
'WC' : 'Windy, Cloudy',
'WD' : 'Windy',
'WF' : 'Windy, Fair',
'WR' : 'Windy, Rain',
'WS' : 'Windy, Shower' }


for child in root.findall("./item/weatherForecast/"):
    #TODO pass in area as argv, once testing is complete
	if( child.attrib.get('name') == "Sengkang" ):
		print code[child.attrib.get('forecast')]
		if( child.attrib.get('forecast') )=='PN':
			pygame.mixer.init()
            #TODO pass song as arg or package one with script
			pygame.mixer.music.load("song.mp3")
			pygame.mixer.music.play()
            #TODO limit time it plays for
			while pygame.mixer.music.get_busy() == True:
				continue


