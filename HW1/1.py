import csv
def cardinality_items(filename):
    items = set()
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            l = row.split(',')
            for item in l:
                items.add(item)
    print("The cardinality is: ", len(items))
