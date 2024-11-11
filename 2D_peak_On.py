def find_2D_peak_linear(arr):
    def find_max_in_column(col, start_row, end_row):
        max_val = arr[start_row][col]
        max_row = start_row
        for i in range(start_row + 1, end_row + 1):
            if arr[i][col] > max_val:
                max_val = arr[i][col]
                max_row = i
        return max_row

    n = len(arr)
    if n == 0:
        return -1, -1

    # 先找中間列的最大值
    mid_col = n // 2
    curr_row = find_max_in_column(mid_col, 0, n-1)
    curr_col = mid_col

    while True:
        # 當前值
        curr_val = arr[curr_row][curr_col]
        is_peak = True
        max_val = curr_val
        next_row = curr_row
        next_col = curr_col

        # 檢查四個方向
        # 上
        if curr_row > 0 and arr[curr_row-1][curr_col] > max_val:
            max_val = arr[curr_row-1][curr_col]
            next_row = curr_row-1
            next_col = curr_col
            is_peak = False
        # 下
        if curr_row < n-1 and arr[curr_row+1][curr_col] > max_val:
            max_val = arr[curr_row+1][curr_col]
            next_row = curr_row+1
            next_col = curr_col
            is_peak = False
        # 左
        if curr_col > 0 and arr[curr_row][curr_col-1] > max_val:
            max_val = arr[curr_row][curr_col-1]
            next_row = curr_row
            next_col = curr_col-1
            is_peak = False
        # 右
        if curr_col < n-1 and arr[curr_row][curr_col+1] > max_val:
            max_val = arr[curr_row][curr_col+1]
            next_row = curr_row
            next_col = curr_col+1
            is_peak = False

        if is_peak:
            return curr_row, curr_col

        # 移動到最大值的位置
        curr_row = next_row
        curr_col = next_col

# 測試
arr = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [8, 9, 10, 0, 0, 0, 0],
    [7, 1, 11, 0, 0, 0, 0],
    [6, 2, 3, 0, 0, 0, 0],
    [5, 4, 0, 0, 0, 0, 0]
]
# arr = [
#     [10, 9, 10, 9, 11, 66],
#     [22, 12, 13, 11, 13, 55],
#     [16, 7, 10, 13, 14, 44],
#     [13, 21, 20, 23, 25, 17],
#     [19, 33, 17, 18, 30, 19],
#     [29, 24, 15, 20, 23, 33]
# ]
i, j = find_2D_peak_linear(arr)
print(f"Peak found at position ({i}, {j}) with value {arr[i][j]}")