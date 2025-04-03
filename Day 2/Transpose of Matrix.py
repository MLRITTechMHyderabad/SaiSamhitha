rows = int(input(" number of rows: "))
col = int(input(" number of columns"))
matrix = [list(map(int, input().split())) for s in range(rows)]
transpose = [[matrix[j][i] for j in range(rows)] for i in range(col)]
for row in transpose:
    print(*row)
