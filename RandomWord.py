import random


def list_shuffle(s):
    for i in range(len(s)-1, 0, -1):
        pick = random.randint(0, i)
        s[pick], s[i] = s[i], s[pick]
    return s[0]


print(list_shuffle(input().split()))
