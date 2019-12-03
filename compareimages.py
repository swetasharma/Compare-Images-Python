import math, operator
from PIL import Image
from pathlib import Path
# importing csv module
import csv


# csv file name
inputfilename = Path("input.csv")

# name of csv file 
outputfilename = Path("theresult.csv")

def compare(image1, image2):
	h1 = Image.open("image1").histogram()
	h2 = Image.open("image2").histogram()

	rms = math.sqrt(reduce(operator.add,
			map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
	return rms
	
# Creating an empty Dictionary 
dictObj = {} 

try:
	with open(inputfilename, 'r') as csvfile:
		# creating a csv reader object 
		reader = csv.DictReader(csvfile)
		# get total number of rows
		columns = len(row)
		print(columns)
		if columns != 2:
			print("There must be exactly 2 number of columns with column name as image1 and image2")
		#for row in reader:
    #  print(row)
      # Create a new dictionary - data rows as dictionary objects
      dictObj = {'image1':rows[0], 'image2':rows[1], 'similar':compare(rows[0], rows[1]), 'elapsed':'0' for rows in reader}
			
except IOError:
		print("File not found or path is incorrect")
		
# writing to csv file 	
with open(outputfilename, "w") as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames = ["image1", "image2", "similar", "elapsed"])
	# writing headers (field names) 
	writer.writeheader()
	# writing data rows 
	writer.writerows(dictObj)
