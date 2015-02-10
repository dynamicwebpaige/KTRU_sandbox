#! /usr/bin/python

import urllib2
import re

from bs4 import BeautifulSoup

html_page = urllib2.urlopen("http://noise.ktru.org/ktru/sheet.nsf/WebByDJ?OpenView&Start=398&Count=67&Expand=398#398")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
	print "http://noise.ktru.org" + str(link.get('href'))
