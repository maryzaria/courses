def chislo(x):
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    val = [i for i in range(1, 27)]
    d = dict(zip(key, val))
    s = 0
    for b in x:
        s += d[b]
    return s


tringle = [i * (i + 1) / 2 for i in range(50)]

with open('words1.txt') as file:
    lst = file.read().split(',')
    words = [word.replace('"', '') for word in lst]

print(len(list(filter(lambda w: chislo(w) in tringle, words))))
