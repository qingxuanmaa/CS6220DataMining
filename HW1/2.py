def all_itemsets(items, k):
    res = []
    helper(items, k, res, [])
    print("The list of all possible unique item sets: ", res)


def helper(items, k, res, temp):
    if k == 0:
        res.append(temp[:])
    for i, item in enumerate(items):
        temp.append(item)
        helper(items, k-1, res, temp)
        temp.pop()