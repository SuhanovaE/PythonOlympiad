a =[list(range(i, i+8) if i%16 else reversed(range(i, i+8))) for i in range(0, 63, 8)]
b = zip(*[list(reversed(i)) for i in a])
[print(*i) for i in b]
print()
[print(*i) for i in a]
print()


def snake(n, m):
    matrix = [[0] * m for _ in range(n)]
    val = -1

    for k in range(n + m):
        tmp = min(k, max(n - 1, m - 1))
        for j in range(tmp, -1, -1):
            if k % 2:
                row = k - j
                col = j
            else:
                row = j
                col = k - j

            if row < n and col < m:
                val += 1
                matrix[row][col] = val

    return matrix


res = snake(8, 8)  # snake(int(input('rows = ')), int(input('columns = ')))
for row in res:
    print(*row)