#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    d = {}

    # create a dictionary with the key as the source and destination as the value
    for t in tickets:
        if t not in d:
            d[t.source] = t.destination 

    # create a routes list with the first flight starting from where source is "NONE"
    route = []
    route.append(d['NONE'])

    # from the destination of where source was "NONE", find the next destination
    next_dest = d[d['NONE']]
    route.append(next_dest)

    # continue finding the next destination until we reach "NONE"
    while d[next_dest] is not "NONE":
        next_dest = d[next_dest]
        route.append(next_dest)

    route.append("NONE")
    return route