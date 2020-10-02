import csv
import datetime
from os import path


def toHeadings(data, output_file_path):
	output = []
	row_count = 0
	for heading_names, values in data.items():
		output.append(heading_names)

	# Check if logfile exists
	if path.exists(output_file_path):
		with open(output_file_path, "r") as f:
			row_count = sum(1 for line in f)

	if row_count == 0 or not path.exists(output_file_path):
		with open(output_file_path, "w") as f:
			writer = csv.writer(f)
			writer.writerow(output)


def write(data, output_file_path):
	line = ""
	for point in data:
		line += f"{data[point]},"
	line += str(datetime.datetime.now().time()).split(".")[0][:-3]+","
	with open(output_file_path, "a") as f:
		f.writelines(line[:-1]+"\n")
		f.close()
		print("Log updated.")
