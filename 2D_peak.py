def find_2D_peak(arr):
    def find_max_in_column(col):
        max_val = arr[0][col]
        max_row = 0
        for i in range(1, len(arr)):
            if arr[i][col] > max_val:
                max_val = arr[i][col]
                max_row = i
        return max_row, max_val

    def check_neighbors(i, j):
        val = arr[i][j]
        # 檢查上方
        if i > 0 and arr[i-1][j] >= val:
            return False, i-1, j
        # 檢查下方
        if i < len(arr)-1 and arr[i+1][j] >= val:
            return False, i+1, j
        # 檢查左方
        if j > 0 and arr[i][j-1] >= val:
            return False, i, j-1
        # 檢查右方
        if j < len(arr[0])-1 and arr[i][j+1] >= val:
            return False, i, j+1
        return True, i, j

    left = 0
    right = len(arr[0]) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # 找到中間列的最大值
        max_row, max_val = find_max_in_column(mid)
        
        # 檢查是否為峰值
        is_peak, new_i, new_j = check_neighbors(max_row, mid)
        if is_peak:
            return max_row, mid
            
        # 如果不是峰值，決定往哪個方向搜索
        if new_j < mid:
            right = mid - 1
        else:
            left = mid + 1

    return -1, -1  # 沒有找到峰值

# 測試

arr = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
# arr = [
#     [10, 9, 10, 9, 11, 66],
#     [22, 12, 13, 11, 13, 55],
#     [16, 7, 10, 13, 14, 44],
#     [13, 21, 20, 23, 25, 17],
#     [19, 33, 17, 18, 30, 19],
#     [29, 24, 15, 20, 23, 33]
# ]
i, j = find_2D_peak(arr)
print(f"Peak found at position ({i}, {j}) with value {arr[i][j]}")