"""
We have an N*M grid, grid have one element named bob. Bob can travel diagonally blocks only
The grid has some blocked blocks on which bob can not travel. Write a function that returns on how.
"""


import sys
sys.setrecursionlimit(10**6)


def get_neighbors(m, n, position):
    neighbors = []
    position_m = position[0]
    position_n = position[1]
    if position_m < m and position_n > 0:
        neighbors.append([position_m+1, position_n-1])
    if position_n < n and position_m > 0:
        neighbors.append([position_m-1, position_n+1])
    if position_m < m and position_n < n:
        neighbors.append([position_m + 1, position_n + 1])
    if position_m > 0 and position_n > 0:
        neighbors.append([position_m - 1, position_n - 1])

    return neighbors


def bfs(m, n, blocked_list, position, visited=[], queue=[]):

    visited.append(position)
    neighbors = get_neighbors(m-1, n-1, position)
    for neighbor in neighbors:
        if neighbor not in queue and neighbor not in visited and neighbor not in blocked_list:
            queue.append(neighbor)
    position = queue.pop(0)
    if len(queue) > 0:
        return bfs(m, n, blocked_list, position, visited=visited, queue=queue)
    return len(visited)-1


blocked_items = [[1,1], [1,5], [2,4], [4,3], [4,6], [6,6], [7,2], [7,5], [9,4]]

current_position = [9, 3]

a = bfs(10, 8, blocked_items, current_position)

print(a)

