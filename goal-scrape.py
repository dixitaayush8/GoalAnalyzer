import requests
from bs4 import BeautifulSoup
import os
import urllib
import re

def get_data(goal_one):
	goal = 'how to ' + goal_one
	goal += ' wikihow'
	name = urllib.parse.quote_plus(goal)
	url = 'http://www.google.com/search?q='+name
	result = requests.get(url).text
	link_start=result.find('wikihow.com')
	link_end=result.find('&',link_start)
	link = 'https://' + result[link_start:link_end]
	if "%2522" in link:
		link = link.replace("%2522","\"")
	the_html = requests.get(link).text
	soup = BeautifulSoup(the_html, "html.parser")
	steps = soup.findAll("div",{'class':"step"})
	count = 1
	data = ""
	for s in steps:
		for p in s.findAll("b",{'class':"whb"}):
			if(len(p.get_text()) == 1):
				p.decompose()
				count = count - 1
			else:
				if p.get_text() is not None:
					data = data + "\n" + str(count) + ". " + p.get_text()
			count = count + 1
		for j in s.findAll("ul"):
			for r in j.findAll("li"):
				data = data + " " + r.get_text()

	data = data.split("\n")
	print(data)


get_data("sleep more")