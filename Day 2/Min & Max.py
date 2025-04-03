rows = int(input(" number of rows: "))
cols = int(input(" number of columns"))
matrix = [list(map(int, input().split())) for s in range(rows)]
max_value = max(max(col) for col  in matrix)
min_value = min(min(col) for col in matrix)
print(max_value)
print(min_value)
