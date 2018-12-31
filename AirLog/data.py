import datetime

def toHeadings(data):
	output = []
	for heading in data:
		output.append(heading)
	return output

def write(heading, data):
	line = ""
	for point in data:
		line += f"{data[point]},"
	line += str(datetime.datetime.now().time()).split(".")[0][:-3]+","
	with open("./logs/"+ str(datetime.datetime.today().strftime('%Y-%m-%d')) + ".csv", "w") as f:
		f.writelines(line[:-1]+"\n")
		f.close()
		print("Log updated.")