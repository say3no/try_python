# vim: set fileencoding=utf-8:
"""
項目14: Noneを返すよりは例外を選ぶ

"""


def main():
    print(divide_dame.__doc__)
    res = divide_dame(0, 1)
    print(res if res else "invalid inputs")  # pythonはint(0)をFalseと解釈するから, "invalid inputs"

    print(divide_madamashi.__doc__)
    suc, res = divide_madamashi(0, 1)
    print(res if suc else "invalid inputs")  # ちゃんと 0 を返す

    print(divide_good.__doc__)

    try:
        res = divide_good(3, 1)
    except ValueError:
        print('Invalid inputs')
    else:
        print('Result is %.1f' % res)


def divide_dame(a, b):
    """
    None を返すと、if文で明示的に is None を使わないといけない？
    :param a: int
    :param b: int
    :return: a/b if a/b != ZeroDivionError else None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def divide_madamashi(a, b):
    """
    成否を返すことで、 divide_dame よりはユーザは利便性は工場した、しかし…
    :param a: int
    :param b: int greater than 0
    :return: ???, ans
    """
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


def divide_good(a, b):
    """
    そもそもNoneを返すな。エラーを返せ
    :param a:
    :param b: int greater than 0
    :return: a /b
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs'), e


if __name__ == "__main__":
    main()
