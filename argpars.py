import argparse


def main():
    _parser = argparse.ArgumentParser(
        description='This script is Live migration tool.')

    # -d option
    _parser.add_argument('-d', '--dry-run',
                         type=int,
                         required=True,

    p = _parser.parse_args()
    print(p.dry_run)


if __name__ == "__main__":
    main()
