# vim: set fileencoding=utf-8 :
"""
項目17: 引数に対してイテレータを使うときには確実さを尊ぶ

関数の引数がオブジェクトのリストのとき、そのリストに対して何度も繰り返し処理することが重要な場合がよくあります。
そんな時…？

"""


def main():
    # 小さく有限な配列を一つ一つ演算したい場合
    visits = [15, 35, 80]
    percentages = normalize(visits)
    print(percentages)

    """
    データ総数が巨大なN担った時どうするか？ 外部ファイルを１行ずつ読み込んで返し続けるyieldを考える。
    動くけど、巨大なlistが必要になる場合がある。そうするとメモリを圧迫し、yieldの旨味が消えてしまっている
    """
    it = read_visits('hogehoge.txt')
    percentages = normalize_copy(it)
    print(percentages)

    """
    期待通りに動作をするが、lamdbaを使わないと行けないのはいただけない。
    っつーかこれでどうしてうまくいくのかわかっていない
    """
    percentages = normalize_func(lambda: read_visits('hogehoge.txt'))
    print(percentages)

    """
    うえの実装について、
    > これは動きますが、このようにlamdba関数を渡さなければならないのは面倒なことです。
    >同じ結果が得られるより良い方法は、iterator protocolを実装した新たなコンテナクラスを提供することです。
    
    """

    visits = ReadVisits('hogehoge.txt')
    p = normalize(visits)
    print("\n\nby using Container Class contain __iter__ ")
    print(p)

    p = normalize_defensive(visits)  # ただのiterではだめ、コンテナ型じゃないとだめ
    print("\n\nby normalize_defensive")
    print(p)

    p = normalize_defensive([1, 2, 3, 4, 5])  # listはコンテナ型
    print("\n\n [1,2,3,4,5] by normalize_defensive")
    print(p)


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * float(value) / total
        result.append(percent)

    return result


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * float(value) / total
        result.append(percent)

    return result


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


def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * float(value) / total
        result.append(percent)

    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


if __name__ == "__main__":
    main()
