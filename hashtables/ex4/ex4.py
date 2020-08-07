def has_negatives(a):
    d = {}
    result = []

    for n in a:
        # get the absolute value of n
        n = abs(n)

        # if the number is not in the dictionary, add it
        if n not in d:
            d[n] = 0
        # increment the occurrence of n
        d[n] += 1
    
    # if n has occurred twice, append it to result
    for k, v in d.items():
        if v == 2:
            result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
