def cmp(s1, s2):
    if s1.type == "string" and s2.type == "number":
        return 1

    if s1.type == "number" and s2.type == "string":
        return -1

    if s1.type == "string" and s2.type == "string":
        return (s1.value > s2.value) - (s1.value < s2.value)

    if s1.type == "number" and s2.type == "number":
        if s1.value == s2.value:
            return (s1.len > s2.len) - (s1.len < s2.len)
        else:
            return (s1.value > s2.value) - (s1.value < s2.value)


class SubStr(object):
    def __init__(self, str, type, value, len):
        super(SubStr, self).__init__()
        self.str = str
        self.type = type
        self.value = value
        self.len = len
