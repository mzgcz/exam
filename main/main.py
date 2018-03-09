#!/usr/bin/env python
# coding: utf-8

import sys


def split_complex_string(s):
    # B -> [B]
    # 1 -> [1]
    # B1 -> [B, 1]
    # B01 -> [B, 01]
    # B\1 -> [B1]
    # B\123B -> [B123B]
    # B\1234 -> [B123, 4]
    # B\1B1 -> [B1B, 1]
    # \1B -> [1B]
    # B\1234\1B -> [B123, 4, 1B]
    # \B1 -> [\B1]
    # B\B1 -> [B, B1]
    # 1\B1 -> [1B1]
    # \\1 -> string error
    # B\\1 -> string error
    # \B\\1 -> string error
    # B\ -> string error

    if s[-1] == "\\":
        raise Exception("string error")

    str_array = []

    status = ""
    escape = False
    escape_len = 0
    for c in enumerate(s):
        if status == "":
            if c[1].isalpha():
                status = "string"
            elif c[1].isdigit():
                status = "number"
            elif c[1] == "\\":
                escape = True
                i = c[0]
                if s[i + 1].isalpha():
                    status = "number"
                    escape_len = 1
                elif s[i + 1].isdigit():
                    status = "string"
                    escape_len = 3
                else:
                    raise Exception("string error")

            index_beg = c[0]
        elif status == "string":
            if escape:
                if c[1].isalpha():
                    escape_len = 0
                    escape = False
                else:
                    escape_len -= 1
                    if escape_len > 0:
                        pass
                    else:
                        escape = False
            else:
                if c[1].isdigit():
                    index_end = c[0]
                    str_array.append(s[index_beg:index_end])

                    status = "number"
                    index_beg = c[0]
                elif c[1] == "\\":
                    escape = True
                    i = c[0]
                    if s[i + 1].isalpha():
                        index_end = c[0]
                        str_array.append(s[index_beg:index_end])

                        status = "number"
                        index_beg = c[0]
                        escape_len = 1
                    elif s[i + 1].isdigit():
                        escape_len = 3
                    else:
                        raise Exception("string error")
        elif status == "number":
            if escape:
                if c[1].isalpha():
                    escape_len -= 1
                    if escape_len > 0:
                        pass
                    else:
                        escape = False
                else:
                    escape_len = 0
                    escape = False
            else:
                if c[1].isalpha():
                    index_end = c[0]
                    str_array.append(s[index_beg:index_end])

                    status = "string"
                    index_beg = c[0]
                elif c[1] == "\\":
                    escape = True
                    i = c[0]
                    if s[i + 1].isalpha():
                        escape_len = 1
                    elif s[i + 1].isdigit():
                        index_end = c[0]
                        str_array.append(s[index_beg:index_end])

                        status = "string"
                        index_beg = c[0]
                        escape_len = 3
                    else:
                        raise Exception("string error")
    else:
        str_array.append(s[index_beg:])

    return str_array


def compare_two_complex_string(s1, s2):
    # B1 < B2, B1 < B01, B01 < B2
    if s1 > s2:
        return 1
    elif s1 == s2:
        return 0
    else:
        return -1


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: main.py string1 string2")
        sys.exit(1)

    s1 = sys.argv[1]
    s2 = sys.argv[2]
