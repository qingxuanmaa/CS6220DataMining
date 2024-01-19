def total_unique_users(filenames):
  user_ids = set()
  for filename in filenames:
    with open(filename, 'r') as file:
        for row in file:
            if '-' in row: 
                user_id = row.split(',')[0]
                user_ids.add(user_id)

  print("The number of total unique users is: ", len(user_ids))
  
filenames = ['combined_data_1.txt', 'combined_data_2.txt', 'combined_data_3.txt', 'combined_data_4.txt']
total_unique_users(filenames)