import sys


for s in sys.stdin:
    x, y = s.strip()[1:-1].split(', ')
    print(-90 <= float(x) <= 90 and -180 <= float(y) <= 180)

# for x, y in tuple(map(float, sys.stdin))