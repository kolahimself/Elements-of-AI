portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


# Test: with only 5 routes
def permute5(route, ports):
    a = 0
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    route = [b, c, d, e]
                    if all(elem in route for elem in ports):
                        route = [a, b, c, d, e]
                        print(' '.join([portnames[i] for i in route]))


permute5([0], list(range(1, len(portnames))))


#   Solution
def permutations(route, ports):
    # Write your recursive code here
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i] + ports[i + 1:])


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
