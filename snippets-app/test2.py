import csv

with open('snippets.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')

	for row in readcsv:
		print row