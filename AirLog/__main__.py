import csv
import datetime
import os
import argparse

# Program constants
LOG_FILE_BASE_PATH = os.path.join("..", "logs")
PROMPT_PROGRESSION = ["Callsign", "Name", "Location", "Comm type", "signal ( x/10 )"]

def writeCSVHeader(data: dict, output_file_path: str) -> None:
	"""Write the keys of a dict as CSV col headers to a file

	Args:
		data (dict): Data dict
		output_file_path (str): Output file
	"""

	output = []
	row_count = 0
	for heading_names, values in data.items():
		output.append(heading_names)

	# Check if logfile exists
	if os.path.exists(output_file_path):
		with open(output_file_path, "r") as f:
			row_count = sum(1 for line in f)

	if row_count == 0 or not os.path.exists(output_file_path):
		with open(output_file_path, "w") as f:
			writer = csv.writer(f)
			writer.writerow(output)


def writeCSVContents(data: dict, output_file_path: str) -> None:
	"""Write the contents of a dict as a row of a CSV file

	Args:
		data (dict): Data dict
		output_file_path (str): Output file
	"""
	
	line = ""
	for point in data:
		line += f"{data[point]},"
	line += str(datetime.datetime.now().time()).split(".")[0][:-3]+","
	with open(output_file_path, "a") as f:
		f.writelines(line[:-1]+"\n")
		f.close()
		print("Log updated.")

def main() -> None:
	"""Main CLI app"""

	# Prompt log directory from user
	ap = argparse.ArgumentParser()
	ap.add_argument("logdir", help="Directory to store log files")
	args = ap.parse_args()

	# Define output path
	output_file_path = os.path.join(args.logdir, str(datetime.datetime.today().strftime('%Y-%m-%d')) + ".csv")

	# Iterate through list of prompts until they all have been completed
	data = {}
	while 0 < len(PROMPT_PROGRESSION):
		for prompt in PROMPT_PROGRESSION:
			answer = input(f"{prompt}>")
			if len(answer) != 0:
				data[prompt] = answer
				PROMPT_PROGRESSION.remove(prompt)

	# Finally, ask for any notes
	data["Notes"] = input("notes>")

	# Write out log file
	writeCSVHeader(data, output_file_path)
	writeCSVContents(data, output_file_path)
