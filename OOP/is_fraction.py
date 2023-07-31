import re


def is_fraction(string):
    pattern = r'-?\d+/[1-9]\d*'
    return bool(re.fullmatch(pattern, string))


print(is_fraction('1000/01'))
# TEST_9:
print(is_fraction('-987'))