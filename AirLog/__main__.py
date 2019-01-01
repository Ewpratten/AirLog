import data as csv

__version__ = "0.2"
callsign_endpoint = "http://hamcall.net/call?callsign="

print(f"AirLog Version: {__version__}")

questions = ["Callsign", "Name", "Location", "Comm type", "Notes", "signal ( x/10 )"]

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
