from collections import defaultdict
import csv

def ids_of_movies(filenames):
    min_user_id = 2649429
    user_id_200 = set()
    num_of_ratings = defaultdict(int)
    for filename in filenames:
        with open(filename, 'r') as file:
            for row in file:
                if '-' in row: 
                    user_id = row.split(',')[0]
                    num_of_ratings[user_id] += 1
    
    # get all user ids who reviewed 200 movies
    for key, value in num_of_ratings.items():
        if value == 200:
            if int(key) < min_user_id:
                min_user_id = int(key) 
            user_id_200.add(int(key))
    

    print(min_user_id)
    
    favorite_movie_ids = set()
    for filename in filenames:
        with open(filename, 'r') as file:
            movie_id = None
            for row in file:
                if ':' in row:
                    movie_id = row.split(":")[0].strip()
                    # print(movie_id)
                else:
                    user_id = row.split(',')[0]
                    rating = row.split(',')[1]
                    if int(user_id) == min_user_id and rating == '5':
                        favorite_movie_ids.add(movie_id)
    return favorite_movie_ids
    

def names_of_movies(filepath, movie_ids):
    movie_names = set()
    with open(filepath, 'r', encoding='ISO-8859-1') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            movie_id = row[0]
            movie_name = row[2]
            
            if movie_id in movie_ids:
                print(movie_name)
                movie_names.add(movie_name)

    print("Names of movies: ", movie_names)


filenames = ['combined_data_1.txt', 'combined_data_2.txt', 'combined_data_3.txt', 'combined_data_4.txt']
filepath = "movie_titles.csv"
movie_ids = ids_of_movies(filenames)
print(movie_ids)
names_of_movies(filepath, movie_ids)