# from bs4 import BeautifulSoup
# import requests

import data as csv

__version__ = "0.1"
callsign_endpoint = "http://hamcall.net/call?callsign="

print(f"AirLog Version: {__version__}")

questions = ["Callsign", "Name", "Location", "Comm type", "Notes"]

data = {}

while 0 < len(questions):
	for question in questions:
		print(question + "?")
		answer = input(">")
		if len(answer) != 0:
			data[question] = answer
			questions.remove(question)

headings = csv.toHeadings(data)
csv.write(headings, data)




# print("Callsign?")
# callsign = input(">")

# data = BeautifulSoup(requests.get(callsign_endpoint + callsign).text, "lxml")

# names = []
# loactions = []
# licenses = []

# location = data.find("b")
# for i,tg in enumerate([str(tag) for tag in data.find_all()]):
# 	if "<b>License Class:" in tg:
# 		#licences
# 		licenses.append(tg.split(">")[2])
		
# 		# name
# 		if len([str(tag) for tag in data.find_all()][i-5].strip("<b>").strip("<br/>")) < 50:
# 			names.append([str(tag) for tag in data.find_all()][i-5].strip("<b>").strip("<br/>"))
		
# 		# address
# 		address = [str(tag) for tag in data.find_all()][i-4]
# 		print(address)
# 	# 	break
		
# 	# if tg[1] == "b":
# 	# 	[print(tg)]
		
# print(f"Licenses: {licenses}")
# print(f"Name: {names}")