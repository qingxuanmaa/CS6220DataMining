from collections import defaultdict

def rated_200(filenames):
  num_of_ratings = defaultdict(int)
  for filename in filenames:
    with open(filename, 'r') as file:
        for row in file:
            if '-' in row: 
                user_id = row.split(',')[0]
                num_of_ratings[user_id] += 1
                
    count = 0
    
    for value in num_of_ratings.values():
        if value == 200:
            count += 1

  print("The number of users who rated exactly 200 movies is: ", count)

                    
  
filenames = ['combined_data_1.txt', 'combined_data_2.txt', 'combined_data_3.txt', 'combined_data_4.txt']
rated_200(filenames)