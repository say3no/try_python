# vim: set fileencoding=utf-8:
from urlparse import parse_qs


def main():
    # 案1
    my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
    print(repr(my_values))

    # 案2
    print('Red:     ', my_values.get('red'))
    print('Green:   ', my_values.get('green'))
    print('Opacity: ', my_values.get('opacity'))

    # 案3
    """
    値が取れなかったり、空白だったりした場合は、デフォルト値を0にしたほうがよい。
    if文やヘルパー巻数を使うほどのロジックではないから、論理式を選択することもできる。 
    Pythonではどうするか？ から文字列、カラリスト、ゼロが全て暗黙にFalseとして評価される点に注目する。
    
    値が取れない場合には dict.get の第二引数 default で対応する
    
    さらに、それをintでラップする。
    """
    red = int(my_values.get("red", [''])[0] or 0)
    green = int(my_values.get('green', [''])[0] or 0)
    opacity = int(my_values.get('opacity', [''])[0] or 0)

    print('Red:     %s' % red)
    print('Green:   %s' % green)
    print('Opacity: %s' % opacity)

    # 案4
    """
    コードを初めて読む人は大変。短くすることはよいことだが、これらすべてを１行に収めるほどの価値はない。
    """
    red = my_values.get("red", [''])  # 必ず値を取得し(Key Errorにならない)
    red = int(red[0]) if red[0] else 0 # その後、値に応じて処理を行う


if __name__ == "__main__":
    main()
