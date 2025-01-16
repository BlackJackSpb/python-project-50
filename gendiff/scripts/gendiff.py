#!/usr/bin/env python3

from gendiff import generate_diff, cli_pars


def main():
    first_file, second_file, format = cli_pars()
    print(generate_diff(first_file, second_file, format))


if __name__ == '__main__':
    main()
