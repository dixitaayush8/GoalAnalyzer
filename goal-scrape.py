import requests
from bs4 import BeautifulSoup
import os
import urllib
import re
import sys

def get_data(goal_one):
	goal = 'how to ' + goal_one
	goal += ' wikihow'
	name = urllib.parse.quote_plus(goal)
	url = 'http://www.google.com/search?q='+name
	result = requests.get(url).text
	link_start=result.find('wikihow.com')
	link_end=result.find('&',link_start)
	link = 'https://' + result[link_start:link_end]
	if link_start == -1 or link_end == -1:
		data = "Go for it! Unfortunately, there is no advice I can give you on the goal \'" + goal_one + "' for now. :/"
	else:
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

		#data = data.split("\n")
	print(data)
	print("\n")


def get_option():
	someIn = str(input('[1] Name a goal you\'d like to accomplish\n[0] Quit\nPress 0 or 1: '))
	if (someIn == '0' or someIn == '1'):
		return someIn
	else:
		while(someIn != '0' or someIn != '1'):
			if (someIn == '0' or someIn == '1'):
				return someIn
			someIn = str(input('[1] Name a goal you\'d like to accomplish\n[0] Quit\nPress 0 or 1: '))
	return someIn

def get_string():    
	try:
		someIn = str(input('Name of the goal: '))
	except:
		someIn = str(input('Try again: '))
	return someIn

def main():
	while(True):
		option = get_option()
		if(option == '0'):
			print('Have a nice day!')
			sys.exit(0)
		elif (option == '1'):
			the_string = get_string()
			get_data(the_string)

main()
