def all_itemsets(items, k):
    res = []
    helper(items, k, res, [], 0)
    print("The list of all possible unique item sets: ", res)


def helper(items, k, res, temp, index):
    if k == 0:
        res.append(temp[:])
    else:
        for i in range(index, len(items)):
            temp.append(items[i])
            helper(items, k-1, res, temp, i+1)
            temp.pop()
            
all_itemsets(["ham", "cheese", "bread", "milk"], 3)