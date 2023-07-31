def hash_function(obj):
    s = str(obj)
    res1 = 0
    while len(s) > 1:
        res1 += ord(s[0]) * ord(s[-1])
        s = s[1:-1]
    s = str(obj)
    if len(s) % 2 != 0:
        res1 += ord(s[len(s) // 2])

    res2 = sum(ord(let) * i * (-1) ** (i-1) for i, let in enumerate(s, start=1))

    return (res1 * res2) % 123456791


def limited_hash(left, right, hash_function=None):
    def funk(item):
        if hash_function is None:
            res = hash(item)
        else:
            res = hash_function(item)

        if left <= res <= right:
            return res
        else:
            return (res - left) % (right - left + 1) + left
    return funk


# TEST_5:
def hash_function(obj):
    return sum(index * ord(character) for index, character in enumerate(str(obj), start=1))


hash_function = limited_hash(10, 15, hash_function)

array = [1366, -5502567186.7395, 'zZQyrjYzdgcabTZPATPl', False, {'монета': -671699723096.267, 'лететь': 5151},
         (False, True, 897, -844416.51017117, 1101),
         [True, 171664.794743347, True, False, 'UypAaBSjBWYWBYbmRTdN', 4044844490314.56]]

for item in array:
    print(hash_function(item))

