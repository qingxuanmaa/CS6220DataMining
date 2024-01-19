def range_of_years(filenames):
    years = set()  
    for filename in filenames:
        with open(filename, 'r') as file:
            for row in file:
                if '-' in row: 
                    years.add(row.split(',')[2])
    print("The range of years that this data is valid over is: ", min(years), "to", max(years))

filenames = ['combined_data_1.txt', 'combined_data_2.txt', 'combined_data_3.txt', 'combined_data_4.txt']
range_of_years(filenames)