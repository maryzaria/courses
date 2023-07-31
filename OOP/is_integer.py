def is_integer(string):
    try:
        s = int(string)
        return True
    except ValueError:
        return False


# TEST_7:
print(is_integer('5.5'))
