import csv
from collections import defaultdict

def movie_names_four(filename):
    names = defaultdict(int)
    with open(filename, 'r', encoding='ISO-8859-1') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            name = row[2]
            names[name] += 1
            
    count = 0
    for value in names.values():
        if value == 4:
            count += 1
            
    print("The number of movie names refer to four different movies is: ", count)

movie_names_four("movie_titles.csv")