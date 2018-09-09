# vim: set fileencoding=utf-8:
"""


"""


def main():
    address = 'Four score and seven years ago...'
    result = index_words(address)
    print(result)
    result = list(index_words_iter(text=address))
    print(result)


def index_words(text):
    """
    文字列 text が与えられた時、各単語の頭文字を示す添字が格納された配列を返す関数実装の悪例
    :param text:
    :return: list
    """
    result = []
    if text:
        result.append(0)

    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)

    return result


def index_words_iter(text):
    """
    yield を返すことでgeneraterとなり、本質的な実装だけか残ってスマートな index_words くん
    実装がかなりスッキリしている
    :param text:
    :return:
    """
    if text:
        yield 0

    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


if __name__ == "__main__":
    main()
