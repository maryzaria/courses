n = int(input())

matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i <= j and i <= n - 1 - j:
            matrix[i][j] = i + 1
        if i > j and i < n - 1 - j:
            matrix[i][j] = j + 1
        if i >= j and i >= n - 1 - j:
            matrix[i][j] = n - i
        if i < j and i > n - 1 - j:
            matrix[i][j] = n - j

for line in matrix:
    print(' '.join(map(str, line)).ljust(2))