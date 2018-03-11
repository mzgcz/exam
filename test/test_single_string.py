# coding: utf-8

from nose.tools import eq_
from single_string import SingleString


class TestSingleString(object):
    """Documentation for TestSingleString

    """

    def __init__(self):
        super(TestSingleString, self).__init__()

    def test_cmp_same_string(self):
        s1 = SingleString("ab", SingleString.TYPE_STRING)
        s2 = SingleString("ab", SingleString.TYPE_STRING)
        eq_(cmp(s1, s2), 0)

    def test_cmp_different_string(self):
        s1 = SingleString("abc", SingleString.TYPE_STRING)
        s2 = SingleString("ab", SingleString.TYPE_STRING)
        eq_(cmp(s1, s2), 1)

        s1 = SingleString("ab", SingleString.TYPE_STRING)
        s2 = SingleString("abc", SingleString.TYPE_STRING)
        eq_(cmp(s1, s2), -1)

    def test_cmp_number_and_string(self):
        s1 = SingleString("01", SingleString.TYPE_NUMBER)
        s2 = SingleString("ab", SingleString.TYPE_STRING)
        eq_(cmp(s1, s2), -1)

        s1 = SingleString("ab", SingleString.TYPE_STRING)
        s2 = SingleString("01", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), 1)

        s1 = SingleString("01", SingleString.TYPE_NUMBER)
        s2 = SingleString("01", SingleString.TYPE_STRING)
        eq_(cmp(s1, s2), -1)

        s1 = SingleString("01", SingleString.TYPE_STRING)
        s2 = SingleString("01", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), 1)

    def test_cmp_same_number(self):
        s1 = SingleString("1", SingleString.TYPE_NUMBER)
        s2 = SingleString("1", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), 0)

    def test_cmp_different_number(self):
        s1 = SingleString("01", SingleString.TYPE_NUMBER)
        s2 = SingleString("1", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), 1)

        s1 = SingleString("1", SingleString.TYPE_NUMBER)
        s2 = SingleString("01", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), -1)

        s1 = SingleString("1", SingleString.TYPE_NUMBER)
        s2 = SingleString("2", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), -1)

        s1 = SingleString("2", SingleString.TYPE_NUMBER)
        s2 = SingleString("1", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), 1)

        s1 = SingleString("1A0", SingleString.TYPE_NUMBER)
        s2 = SingleString("750", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), 0)

        s1 = SingleString("A", SingleString.TYPE_NUMBER)
        s2 = SingleString("65", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), -1)

        s1 = SingleString("65", SingleString.TYPE_NUMBER)
        s2 = SingleString("A", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), 1)

        s1 = SingleString("B", SingleString.TYPE_NUMBER)
        s2 = SingleString("65", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), 1)

        s1 = SingleString("65", SingleString.TYPE_NUMBER)
        s2 = SingleString("B", SingleString.TYPE_NUMBER)
        eq_(cmp(s1, s2), -1)
