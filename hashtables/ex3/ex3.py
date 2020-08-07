def intersection(arrays):
    d = {}
    result = []

    # create a dictionary for the list of lists
    for a in arrays:
        for i in a:
            # for all numbers in the array, add to dictionary
            if i not in d:
                d[i] = 0
            d[i] += 1

    # if number shows up as many times as len(arrays)
    for k, v in d.items():
        if v == len(arrays):
            # append it to the results
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
