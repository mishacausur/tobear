def counter(element, silier):
    return (element * 2, silier * 3)

assert counter(2, 3) == (4, 9)

def smallest(items):
    return min(items)

assert smallest([-1, 3, 17, 21]) == -1
assert smallest([6, 4, 2, 8]) == 2
