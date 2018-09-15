# vim: set fileencoding=utf-8 :
"""
項目18: 可変長位置引数を使って、見た目をスッキリさせる
項目19: キーワード引数にオプションの振る舞いを与える
項目20: 動的なデフォルト引数は１度しか評価されない。関数定義のときのみ
項目21: キーワード専用引数で明確さを高める
"""


def main():
    log('My numbers are', [1, 2])
    log('Hi There', [])
    log2('My numbers are', "unn", [1, 2])
    log2('Hi There')
    log2('My numbers are')
    log2(message='Hi There')


def log2(message, default="hoge", *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

    print(default)


def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


if __name__ == "__main__":
    main()
