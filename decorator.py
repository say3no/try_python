# vim: set fileencoding=utf-8:
"""
Decoraterは関数・メソッド・クラスを装飾する。
Decoraterは所詮 糖衣構文(Syntax Sugar)に過ぎない。

実際にやっているのは、「関数を引数とするような関数は、それを実行する前に
デコレータで表現できる。」ってこと
"""


def deco(func):
    def wrapper(*args, **kwargs):
        """
        *argsは可変長位置引数、
        **kwargsは可変長キーワード専用引数
        要するに無限に引数をうけとりまっせ〜ということなのだ
        """
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result

    return wrapper


@deco
def main():
    print("I'm at main function")


if __name__ == "__main__":
    main()
