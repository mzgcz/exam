from sub import SubStr, cmp


def test_cmp_two_str():
    s1 = SubStr("ab", "string", "ab", 2)
    s2 = SubStr("ab", "string", "ab", 2)

    assert cmp(s1, s2) == 0

    s1 = SubStr("abc", "string", "abc", 3)
    s2 = SubStr("ab", "string", "ab", 2)

    assert cmp(s1, s2) == 1

    s1 = SubStr("ab", "string", "ab", 2)
    s2 = SubStr("abc", "string", "abc", 3)

    assert cmp(s1, s2) == -1


def test_cmp_num_str():
    s1 = SubStr("01", "number", 1, 2)
    s2 = SubStr("ab", "string", "ab", 2)

    assert cmp(s1, s2) == -1, cmp(s1, s2)

    s1 = SubStr("ab", "string", "ab", 2)
    s2 = SubStr("01", "number", 1, 2)

    assert cmp(s1, s2) == 1, cmp(s1, s2)


def test_cmp_two_num():
    s1 = SubStr("1", "number", 1, 1)
    s2 = SubStr("1", "number", 1, 1)

    assert cmp(s1, s2) == 0, cmp(s1, s2)

    s1 = SubStr("01", "number", 1, 2)
    s2 = SubStr("1", "number", 1, 1)

    assert cmp(s1, s2) == 1, cmp(s1, s2)

    s1 = SubStr("1", "number", 1, 1)
    s2 = SubStr("01", "number", 1, 2)

    assert cmp(s1, s2) == -1, cmp(s1, s2)

    s1 = SubStr("1", "number", 1, 1)
    s2 = SubStr("2", "number", 2, 1)

    assert cmp(s1, s2) == -1, cmp(s1, s2)

    s1 = SubStr("2", "number", 2, 1)
    s2 = SubStr("1", "number", 1, 1)

    assert cmp(s1, s2) == 1, cmp(s1, s2)

    s1 = SubStr("1\A0", "number", 750, 3)
    s2 = SubStr("750", "number", 750, 3)

    assert cmp(s1, s2) == 0, cmp(s1, s2)
