import csv
def cardinality_items(filename):
    items = set()
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            for item in row:
                items.add(item.strip())
    print("The cardinality is: ", len(items))
    
cardinality_items("basket_data.csv")
