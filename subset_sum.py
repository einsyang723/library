def subsetSum(S, t):
    n = len(S)
    dp = [[False]*(t+1) for _ in range(n+1)]
    
    # 初始化：空集合可以湊出和為0
    for i in range(n+1):
        dp[i][0] = True
        
    for i in range(1, n+1):
        for j in range(1, t+1):
            if S[i-1] <= j:
                dp[i][j] = dp[i-1][j-S[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
            print(i, j, dp[i][j])
                
    return dp[n][t]

S = [1, 2, 3, 4, 5]
t =  7
print(subsetSum(S, t))

# def subsetSum(nums, target):
#     n = len(nums)
#     dp = [[False]*(target+1) for _ in range(n+1)]
    
#     # 初始化
#     for i in range(n+1):
#         dp[i][0] = True
        
#     # 填表
#     for i in range(1, n+1):
#         for j in range(target+1):
#             if j < nums[i-1]:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
#     # 如果沒有解
#     if not dp[n][target]:
#         return False, []
    
#     # 反向追蹤找出選擇的數字
#     selected = []
#     i, j = n, target
    
#     while i > 0 and j > 0:
#         # 如果不選nums[i-1]也能達成，就不選
#         if dp[i-1][j]:
#             i -= 1
#         # 否則就要選nums[i-1]
#         else:
#             selected.append(nums[i-1])
#             j -= nums[i-1]
#             i -= 1
            
#     return True, selected[::-1]  # 反轉列表使其按照正向順序

# # 測試
# nums = [1,2,3,4,5]
# target = 7
# exist, selected = subsetSum(nums, target)
# if exist:
#     print(f"result: {selected}, sum: {sum(selected)}")
# else:
#     print("no answer")