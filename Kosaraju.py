def compute_SCCs(graph):
    # 步驟 1: 第一次 DFS，獲得完成順序
    def dfs_first(node, visited, finish_order):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs_first(neighbor, visited, finish_order)
        finish_order.append(node)

    # 步驟 2: 第二次 DFS，找 SCCs
    def dfs_second(node, visited, scc, reversed_graph):
        visited[node] = True
        scc.append(node)
        for neighbor in reversed_graph[node]:
            if not visited[neighbor]:
                dfs_second(neighbor, visited, scc, reversed_graph)

    # 獲得完成順序
    visited = {node: False for node in graph}
    finish_order = []
    for node in graph:
        if not visited[node]:
            dfs_first(node, visited, finish_order)
    print('finish_order', finish_order)

    # 反轉圖
    reversed_graph = {node: [] for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)

    # 找 SCCs
    visited = {node: False for node in graph}
    sccs = []
    for node in reversed(finish_order):
        if not visited[node]:
            current_scc = []
            dfs_second(node, visited, current_scc, reversed_graph)
            sccs.append(current_scc)
            print('current_scc', current_scc)

    return sccs

# 使用例子：處理上一題的 2-SAT implication graph
# graph = {
#     'X1': ['X3'],
#     'X2': [],
#     'X3': ['X1', '¬X3'],
#     '¬X1': ['X2', '¬X3'],
#     '¬X2': ['X1', 'X2'],
#     '¬X3': ['¬X1']
# }

graph = {
    'X1': ['¬X2', 'X3'],
    'X2': ['¬X1', '¬X2'],
    'X3': ['¬X3'],
    '¬X1': ['X2'],
    '¬X2': ['X1'],
    '¬X3': ['¬X1']
}
# graph = {
#     'X1': ['X2'],
#     'X2': ['X3'],
#     'X3': ['¬X3', 'X2'],
#     '¬X1': ['X1'],
#     '¬X2': ['¬X1', '¬X3'],
#     '¬X3': ['¬X2']
# }

sccs = compute_SCCs(graph)
print("Strongly Connected Components:")
for i, scc in enumerate(sccs, 1):
    print(f"SCC {i}: {scc}")

# 檢查是否有解-
def has_solution(sccs, variables):
    # 檢查每個 SCC 是否包含變數和其否定
    for scc in sccs:
        for var in variables:
            if var in scc and f'¬{var}' in scc:
                return False
    return True

variables = ['X1', 'X2', 'X3']
print(f"\nHas solution: {has_solution(sccs, variables)}")