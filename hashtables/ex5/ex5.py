def finder(files, queries):
    d = {}
    result = []

    for path in files:
        # split path into names seperated by "/"
        names = path.split('/')

        if names[-1] not in d.keys():
            # store the path to the actual file as a value
            d[names[-1]] = [path]
        else:
            # else if the file exists, add path into possible locations
            d[names[-1]].append(path)

    # return the dictionary values that match the queries
    for q in queries:
        if q in d.keys():
            result += d[q]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
