import data as csv
import datetime

__version__ = "0.2"
callsign_endpoint = "http://hamcall.net/call?callsign="
output_file_path = "../logs/" + str(datetime.datetime.today().strftime('%Y-%m-%d')) + ".csv"

print(f"AirLog Version: {__version__}")

questions = ["Callsign", "Name", "Location", "Comm type", "signal ( x/10 )"]

data = {}

while 0 < len(questions):
	for question in questions:
		print(question + "?")
		answer = input(">")
		if len(answer) != 0:
			data[question] = answer
			questions.remove(question)


print("Notes?")
data["Notes"] = input(">")

headings = csv.toHeadings(data, output_file_path)
csv.write(data, output_file_path)
