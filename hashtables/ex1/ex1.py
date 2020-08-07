def get_indices_of_item_weights(weights, length, limit):
    d = {}

    min_num = max_num = 0

    # check if there is only one weight
    if length <= 1:
        return None

    # fill dictionary with weights, with list index as the key
    for i, w in enumerate(weights):
        if w not in d:
            d[i] = w

        # if the limit - a weight is in the values: record the index of that weight
        if limit - w in d.values():
            limit -= w
            min_num = i

    # find the index of the remaining weight
    for k, v in d.items():
        if limit == v:
            max_num = k 

    # check if the min and max index are correct
    if min_num > max_num:
        min_num, max_num = max_num, min_num

    return (max_num, min_num)