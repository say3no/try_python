# vim: set fileencoding=utf-8:
import random

"""
重み付きインデックスのリストをソートしたい。
"""


def main():
    # numbers = [random.randint(1, 20) for _ in xrange(10)]
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    priority_group = {2, 3, 5, 7}

    sort_priority(numbers, priority_group)
    print(numbers)


def sort_priority(values, group):
    def helper(x):
        print(x)
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


if __name__ == "__main__":
    main()
