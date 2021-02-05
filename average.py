def average(items):
    if(not isinstance(items, (list, tuple, set, int, float))):
        raise Exception("average expects a list of items")

    if(isinstance(items, (int, float))):
        return items

    if(len(items) == 0):
        raise Exception("average expects a non-empty items")

    runningTotal = 0
    for i in items:
        if(not isinstance(i, (int, float))):
            raise Exception("average expects only numbers")

        runningTotal = runningTotal + i

    return runningTotal/len(items)