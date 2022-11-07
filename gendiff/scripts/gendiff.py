#!/usr/bin/env python3


from gendiff.parser_args import parser_args
from gendiff.generate_diff import generate_diff


def main():
    args = parser_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
