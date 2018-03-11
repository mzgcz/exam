# coding: utf-8

from nose.tools import eq_, raises
from single_string import SingleString
from complex_string import ComplexString


class TestComplexString(object):
    """Documentation for TestComplexString

    """

    def __init__(self):
        super(TestComplexString, self).__init__()

    @raises(ValueError)
    def test_end_with_escapes(self):
        ComplexString("B\\")

    @raises(ValueError)
    def test_double_escapes(self):
        ComplexString(r"B\\1")

    def test_split_empty_string(self):
        result = ComplexString("").split()
        eq_(result, [])

    def test_split_only_string(self):
        result = ComplexString("B").split()
        eq_(result, [SingleString("B", SingleString.TYPE_STRING)])

    def test_split_only_number(self):
        result = ComplexString("1").split()
        eq_(result, [SingleString("1", SingleString.TYPE_NUMBER)])

    def test_split_string_and_number(self):
        result = ComplexString("B1").split()
        eq_(result, [SingleString("B", SingleString.TYPE_STRING),
                     SingleString("1", SingleString.TYPE_NUMBER)])

        result = ComplexString("B01").split()
        eq_(result, [SingleString("B", SingleString.TYPE_STRING),
                     SingleString("01", SingleString.TYPE_NUMBER)])

    def test_split_string_and_escape_number(self):
        result = ComplexString(r"B\1").split()
        eq_(result, [SingleString("B1", SingleString.TYPE_STRING)])

        result = ComplexString(r"B\123B").split()
        eq_(result, [SingleString("B123B", SingleString.TYPE_STRING)])

        result = ComplexString(r"\1B").split()
        eq_(result, [SingleString("1B", SingleString.TYPE_STRING)])

    def test_split_string_escape_numbers_and_number(self):
        result = ComplexString(r"B\1234").split()
        eq_(result, [SingleString("B123", SingleString.TYPE_STRING),
                     SingleString("4", SingleString.TYPE_NUMBER)])

        result = ComplexString(r"B\1B1").split()
        eq_(result, [SingleString("B1B", SingleString.TYPE_STRING),
                     SingleString("1", SingleString.TYPE_NUMBER)])

        result = ComplexString(r"B\1234\1B").split()
        eq_(result, [SingleString("B123", SingleString.TYPE_STRING),
                     SingleString("4", SingleString.TYPE_NUMBER),
                     SingleString("1B", SingleString.TYPE_STRING)])

        result = ComplexString(r"B\1\2345\1B").split()
        eq_(result, [SingleString("B1234", SingleString.TYPE_STRING),
                     SingleString("5", SingleString.TYPE_NUMBER),
                     SingleString("1B", SingleString.TYPE_STRING)])

    def test_split_escape_string_and_number(self):
        result = ComplexString(r"\B1").split()
        eq_(result, [SingleString("B1", SingleString.TYPE_NUMBER)])

        result = ComplexString(r"1\B1").split()
        eq_(result, [SingleString("1B1", SingleString.TYPE_NUMBER)])

        result = ComplexString(r"1\B\B1").split()
        eq_(result, [SingleString("1BB1", SingleString.TYPE_NUMBER)])

    def test_split_string_escape_string_and_number(self):
        result = ComplexString(r"B\B1").split()
        eq_(result, [SingleString("B", SingleString.TYPE_STRING),
                     SingleString("B1", SingleString.TYPE_NUMBER)])
