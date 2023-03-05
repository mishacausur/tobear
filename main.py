class Counter:
    def count(element, silier):
        return  (element * 2, silier * 3)

    def smallest(items):
        return min(items)

assert Counter.count(2, 2) == (4, 6)
assert Counter.smallest([-1, 3, 17, 21]) == -1
assert Counter.smallest([6, 4, 2, 8]) == 2
