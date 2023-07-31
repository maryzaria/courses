import decimal


def is_decimal(string):
    try:
        # decimal.Decimal(string)
        float(string)
        return True
    # except decimal.InvalidOperation:
    except ValueError:
        return False

# TEST_1:
print(is_decimal('100'))

# TEST_2:
print(is_decimal('199.1'))

# TEST_3:
print(is_decimal('-0.2'))

# TEST_4:
print(is_decimal('.-95'))

# TEST_5:
print(is_decimal('-.95'))

# TEST_6:
print(is_decimal('.10'))

# TEST_7:
print(is_decimal('.'))

# TEST_8:
print(is_decimal(''))

# TEST_9:
print(is_decimal('10..1'))

# TEST_10:
print(is_decimal('--10.1'))

# TEST_11:
print(is_decimal('---1.1'))

# TEST_12:
print(is_decimal('1-.1'))

# TEST_13:
print(is_decimal('1.-1'))

# TEST_14:
print(is_decimal('1.1-'))

# TEST_15:
print(is_decimal('1.1.1'))

# TEST_16:
print(is_decimal('a.a'))

# TEST_17:
print(is_decimal('a'))

# TEST_18:
print(is_decimal('348209348203758348635465'))

# TEST_19:
print(is_decimal('3482093.48203758348635465'))

# TEST_20:
print(is_decimal('1-1'))

# TEST_21:
print(is_decimal('1-1-1'))

# TEST_22:
strings = ['100.', '349..', '-425.', '-1248..']
for string in strings:
    print(is_decimal(string))