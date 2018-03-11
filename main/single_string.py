# coding: utf-8


class SingleString(object):
    """Documentation for SingleString

    """

    TYPE_NUMBER = 1
    TYPE_STRING = 2

    def __init__(self, _str, _type):
        super(SingleString, self).__init__()
        self.str = _str
        self.type = _type

    def __eq__(self, other):
        return (self.str == other.str) and (self.type == other.type)

    def __cmp__(self, other):
        result = cmp(self.type, other.type)
        if result != 0:
            return result

        if self.type == self.TYPE_STRING:
            return cmp(self.str, other.str)

        result = cmp(self.calculate_number(), other.calculate_number())
        if result != 0:
            return result
        else:
            return cmp(len(self.str), len(other.str))

    def calculate_number(self):
        value = 0
        digital = len(self.str) - 1
        for c in self.str:
            if c.isdigit():
                value += int(c) * (10 ** digital)
            else:
                value += ord(c) * (10 ** digital)

            digital -= 1

        return value
