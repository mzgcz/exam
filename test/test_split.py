# coding: utf-8

from main import split_complex_string


class TestSplit(object):
    """Documentation for TestSplit

    """

    def __init__(self):
        super(TestSplit, self).__init__()

    def test_1(self):
        result = split_complex_string("B")
        assert result == ["B"], result

    def test_2(self):
        result = split_complex_string("1")
        assert result == ["1"], result

    def test_3(self):
        result = split_complex_string("B1")
        assert result == ["B", "1"], result

    def test_4(self):
        result = split_complex_string("B01")
        assert result == ["B", "01"], result

    def test_5(self):
        result = split_complex_string(r"B\1")
        assert result == [r"B\1"], result

    def test_6(self):
        result = split_complex_string(r"B\1234")
        assert result == [r"B\123", "4"], result

    def test_7(self):
        result = split_complex_string(r"B\123B")
        assert result == [r"B\123B"], result

    def test_8(self):
        result = split_complex_string(r"B\1B1")
        assert result == [r"B\1B", "1"], result

    def test_9(self):
        result = split_complex_string(r"\1B")
        assert result == [r"\1B"], result

    def test_10(self):
        result = split_complex_string(r"B\1234\1B")
        assert result == [r"B\123", "4", r"\1B"], result

    def test_11(self):
        result = split_complex_string(r"\B1")
        assert result == [r"\B1"], result

    def test_12(self):
        result = split_complex_string(r"B\B1")
        assert result == ["B", r"\B1"], result

    def test_13(self):
        result = split_complex_string(r"1\B1")
        assert result == [r"1\B1"], result

    def test_14(self):
        try:
            split_complex_string(r"\\1")
        except Exception, e:
            assert e.message == "string error", e.message

    def test_15(self):
        try:
            split_complex_string(r"B\\1")
        except Exception, e:
            assert e.message == "string error", e.message

    def test_16(self):
        try:
            split_complex_string(r"\B\\1")
        except Exception, e:
            assert e.message == "string error", e.message

    def test_17(self):
        try:
            split_complex_string("B\\")
        except Exception, e:
            assert e.message == "string error", e.message
