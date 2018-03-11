#!/usr/bin/env python
# coding: utf-8

import sys
from complex_string import ComplexString


def compare_complex_string(s1, s2):
    try:
        result = cmp(ComplexString(s1), ComplexString(s2))
    except Exception:
        result = -2

    return result


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: main.py string1 string2")
        sys.exit(-2)

    exit_code = compare_complex_string(sys.argv[1], sys.argv[2])
    print(exit_code)

    sys.exit(exit_code)
