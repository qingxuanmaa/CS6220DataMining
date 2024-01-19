import csv

def unique_names(filename):
	movies = set()
	with open(filename, 'r', encoding='ISO-8859-1') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			name = row[2]
			movies.add(name)

	print("The number of movies with unique names is: ", len(movies))
 
unique_names("movie_titles.csv")