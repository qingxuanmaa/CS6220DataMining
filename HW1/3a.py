def count_total_ratings(filenames):
    count = 0
    for filename in filenames:
        with open(filename, 'r') as file:
            for row in file:
                if '-' in row: 
                    count += 1
                
    print("Total records of movie ratings is: ", count)


filenames = ['combined_data_1.txt', 'combined_data_2.txt', 'combined_data_3.txt', 'combined_data_4.txt']
count_total_ratings(filenames)