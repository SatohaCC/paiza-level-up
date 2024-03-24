import io
import sys

_INPUT = """\
5
0 1 1 0 0
0 1 0 1 0
0 0 0 0 0
0 0 0 1 1
0 1 0 0 0
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 自己ループ・有向グラフ
# i==jを確認する
# ---------------------------------------------------------------------------------------------------------

N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]


edges = []
for i in range(N):
    for j in range(N):
        if G[i][j] > 0 and i == j:
            edges.append(i + 1)

print(len(edges))
for i in range(len(edges)):
    print(edges[i])
