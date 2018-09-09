# vim: set fileencoding=utf-8 :
"""
項目17: 引数に対してイテレータを使うときには確実さを尊ぶ

関数の引数がオブジェクトのリストのとき、そのリストに対して何度も繰り返し処理することが重要な場合がよくあります。
そんな時…？

"""


def main():
    visits = [15, 35, 80]
    percentages = normalize(visits)
    print(percentages)


def normalize(numbers):
    """

    :param numbers:  req list.
    :return:
    """
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * float(value) / total
        result.append(percent)

    return result


if __name__ == "__main__":
    main()
