#! /usr/bin/python

import urllib
from urllib2 import urlopen
from bs4 import  BeautifulSoup
import re

file = open('ian_playsheets.txt','r')

for line in file:
	soup = BeautifulSoup(urlopen(line))
	# print(soup.get_text())
	print(soup.find_all('font', face='Tahoma'))
