import argparse


def main():
    _parser = argparse.ArgumentParser(description='hogehoge')
    _parser.add_argument('--option', required=True)
    p = _parser.parse_args()
    print(p.option)


if __name__ == "__main__":
    main()
