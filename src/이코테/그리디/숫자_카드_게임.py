cnt_row, cnt_col = map(int, input().split())

_max = -1
max_idx = -1

for r in range(cnt_row):
    row = list(map(int, input().split()))
    min_in_row = min(row)

    if _max < min_in_row:
        _max = min_in_row
        max_idx = r

print(max_idx + 1)
