# coding: utf-8

from nose.tools import eq_
from main import compare_complex_string


class TestCompareComplexString(object):
    """Documentation for TestCompareComplexString

    """

    def __init__(self):
        super(TestCompareComplexString, self).__init__()

    def test_error_string(self):
        eq_(compare_complex_string(r"B\\1", "B2"), -2)
        eq_(compare_complex_string(r"B1\\", "B2"), -2)
        eq_(compare_complex_string(r"B\*1", "B2"), -2)

    def test_cmp_by_number(self):
        eq_(compare_complex_string("B1", "B2"), -1)
        eq_(compare_complex_string("B1", "B01"), -1)
        eq_(compare_complex_string("B01", "B2"), -1)
        eq_(compare_complex_string("B01", "B01"), 0)
        eq_(compare_complex_string(r"1\A0", "750"), 0)

    def test_cmp_by_empty(self):
        eq_(compare_complex_string("", ""), 0)

    def test_cmp_empty_and_string(self):
        eq_(compare_complex_string("", "B"), -1)
        eq_(compare_complex_string(r"\1", ""), 1)

    def test_cmp_string_and_number(self):
        eq_(compare_complex_string("B", "1"), 1)
        eq_(compare_complex_string("1", "B"), -1)
        eq_(compare_complex_string("B", r"\B"), 1)
        eq_(compare_complex_string(r"\B", "B"), -1)
        eq_(compare_complex_string(r"B1\A0B", "B750B"), 0)
        eq_(compare_complex_string(r"B1\A0B", "B750"), 1)
        eq_(compare_complex_string(r"B1\A0", "B750B"), -1)
        eq_(compare_complex_string(r"B1\A0B\1\2345", r"B750B\1\2345"), 0)
        eq_(compare_complex_string(r"B1\A0B\1\23405", r"B750B\1\2345"), 1)
        eq_(compare_complex_string(r"B1\A0B\1\234\A", r"B750B\1\23465"), -1)
