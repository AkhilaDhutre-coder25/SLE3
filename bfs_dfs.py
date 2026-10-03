import time
from collections import deque


# ================= BFS =================
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# ================= DFS =================
# Iterative DFS - NO RECURSION
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)


# ================= BEST CASE =================
def best_case(n):
    graph = {i: [] for i in range(n)}

    # Linear graph
    for i in range(n - 1):
        graph[i].append(i + 1)

    return graph


# ================= AVERAGE CASE =================
def average_case(n):
    graph = {i: [] for i in range(n)}

    # Each node connected to next 3 nodes
    for i in range(n):
        for j in range(1, 4):
            if i + j < n:
                graph[i].append(i + j)

    return graph


# ================= WORST CASE =================
def worst_case(n):
    graph = {i: [] for i in range(n)}

    # Dense graph
    for i in range(n):
        for j in range(i + 1, n):
            graph[i].append(j)

    return graph


# ================= TIME MEASUREMENT =================
def measure(algorithm, graph):
    start_time = time.perf_counter()

    algorithm(graph, 0)

    end_time = time.perf_counter()

    return end_time - start_time


# ================= MAIN =================

n = 2000

cases = {
    "BEST CASE": best_case(n),
    "AVERAGE CASE": average_case(n),
    "WORST CASE": worst_case(n)
}

print("\n===== BFS AND DFS TIME ANALYSIS =====")
print("Number of nodes:", n)

for case_name, graph in cases.items():

    bfs_time = measure(bfs, graph)
    dfs_time = measure(dfs, graph)

    print("\n", case_name)
    print("BFS Time:", bfs_time, "seconds")
    print("DFS Time:", dfs_time, "seconds")