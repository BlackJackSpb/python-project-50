#!/usr/bin/env python3

from gendiff import generate_diff, cli_pars


def main():
    first_file, second_file = cli_pars()
    diff = generate_diff(first_file, second_file)
    print(diff)


if __name__ == '__main__':
    main()
