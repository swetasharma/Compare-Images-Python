import math, operator
from pathlib import Path
from PIL import Image
# importing csv module
import csv

# list of images to be compared csv file name
inputfilename = Path("Images_To_Be_Compared.csv")

# Compared images name of csv file
outputfilename = Path("Compared_Images_Result.csv")

def compare(image1, image2):
	h1 = Image.open("image1").histogram()
	h2 = Image.open("image2").histogram()

	return math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

# Creating an empty list of Dictionary
dict_list = []

try:
	with open(inputfilename, 'r') as csvfile: 
		# creating a csv reader object
		reader = csv.DictReader(csvfile)
		for row in reader:
			# get total number of columns
			columns = len(row)
			#print(columns)
			if columns != 2:
				print("There must be exactly 2 number of columns with column name as image1 and image2")
			row['similar'] = compare(row['image1'], row['image2'])
			row['elapsed'] = 0
			dict_list.append(row)
			print(row)
			
			#print(dict_list)
				
except IOError:
  print("File not found or path is incorrect")

# writing to csv file
with open(outputfilename, "w") as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames = ["image1", "image2", "similar", "elapsed"])# writing headers(field names)
	writer.writeheader()
	# writing data rows
	writer.writerows(dict_list)
