import io
import sys

_INPUT = """\
3 3
...
...
...
0 0
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

H, W = map(int, input().split())

graph = [list(map(str, input())) for _ in range(H)]
x, y = map(int, input().split())


if graph[x][y] == "#":
    graph[x][y] = "."
else:
    graph[x][y] = "#"

for i in range(H):
    for j in range(W):
        print(graph[i][j], end=" ")
    print()
