# vim: set fileencoding=utf-8:

"""
重み付きインデックスのリストをソートしたい。
"""
import random


def main():
    # numbers = [random.randint(1, 20) for _ in xrange(10)]
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    numbers2 = [(1, 1), (0, 2), (0, 3), (1, 4), (0, 5), (1, 6), (0, 7), (1, 8)]
    priority_group = {2, 3, 5, 7}
    sort_priority(numbers, priority_group)

    a = []
    for i in xrange(6):
        a.append(Unpoko(random.randrange(1, 100), i, i))

    for i in xrange(6):
        print(a[i].get_hoge())



def sort_priority(values, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)


def sort_priority2(values, group):
    found = [False]

    def helper(x):
        if x in group:
            found[0] = True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found


class Unpoko(object):

    def __init__(self, hoge, fuga, piyo):
        self.hoge = hoge
        self.fuga = fuga
        self.piyo = piyo

    def __iter__(self):
        yield

    def get_hoge(self):
        return self.hoge


if __name__ == "__main__":
    main()
