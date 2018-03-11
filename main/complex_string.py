# coding: utf-8

from single_string import SingleString


class ComplexString(object):
    """Documentation for ComplexString

    """

    ESCAPES = "\\"

    def __init__(self, _str):
        super(ComplexString, self).__init__()
        if self.ESCAPES * 2 in _str:
            raise ValueError

        if len(_str) > 0 and _str[-1] == self.ESCAPES:
            raise ValueError

        self.str = _str
        self.len = len(_str)
        self.single_strings = []

    def __cmp__(self, other):
        for self_single, other_single in zip(self.split(), other.split()):
            result = cmp(self_single, other_single)
            if result != 0:
                return result

        return cmp(len(self.single_strings), len(other.single_strings))

    def _read_normal_string(self, begin):
        for i in range(begin + 1, self.len):
            if not self.str[i].isalpha():
                end = i
                break
        else:
            end = self.len

        return SingleString(self.str[begin:end], SingleString.TYPE_STRING), end

    def _read_normal_number(self, begin):
        for i in range(begin + 1, self.len):
            if not self.str[i].isdigit():
                end = i
                break
        else:
            end = self.len

        return SingleString(self.str[begin:end], SingleString.TYPE_NUMBER), end

    def _read_escape_string(self, begin):
        end = begin + 1
        return SingleString(self.str[begin:end], SingleString.TYPE_NUMBER), end

    def _read_escape_number(self, begin):
        max_len = 3

        for i in range(begin, self.len):
            if (not self.str[i].isdigit()) or (max_len == 0):
                end = i
                break
            else:
                max_len -= 1
        else:
            end = self.len

        return SingleString(self.str[begin:end], SingleString.TYPE_STRING), end

    def _read_escape(self, begin):
        if self.str[begin + 1].isalpha():
            return self._read_escape_string(begin + 1)
        elif self.str[begin + 1].isdigit():
            return self._read_escape_number(begin + 1)
        else:
            raise ValueError

    def _combine_single_strings(self, single_strings):
        self.single_strings = []

        single = None
        for s in single_strings:
            if single is None:
                single = SingleString(s.str, s.type)
            elif s.type == single.type:
                single.str += s.str
            else:
                self.single_strings.append(single)
                single = SingleString(s.str, s.type)
        else:
            if single is not None:
                self.single_strings.append(single)

    def split(self):
        i = 0
        single_strings = []
        while i < self.len:
            if self.str[i].isalpha():
                single_str, i = self._read_normal_string(i)
            elif self.str[i].isdigit():
                single_str, i = self._read_normal_number(i)
            elif self.str[i] == self.ESCAPES:
                single_str, i = self._read_escape(i)
            else:
                raise ValueError

            single_strings.append(single_str)

        self._combine_single_strings(single_strings)

        return self.single_strings
