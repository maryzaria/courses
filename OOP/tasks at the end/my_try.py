for i in range(1000, 10000):
    i = str(i)
    if i[0] == i[3] and i[1] == i[2] and sum(int(num) for num in i) == int(i[:2]):
        print(i)

s = 0
n = 0
while not s >= 50:
    s += 10
    n += 1
    if s < 50:
        s -= 4

print(n)