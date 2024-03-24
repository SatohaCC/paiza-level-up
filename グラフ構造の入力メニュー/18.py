import io
import sys

_INPUT = """\
5 5 2
1 2
1 3
2 4
4 5
5 2
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 頂点の出現回数・有向グラフ
# 辺の出ている頂点 a_1, a_2, ..., a_m と、
# 辺の向かう先の頂点 b_1, b_2, ..., b_m それぞれについて、
# 指定された頂点 v に等しいものの個数を求めてください。
# ---------------------------------------------------------------------------------------------------------

n, m, v = map(int, input().split())
v -= 1

G = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] += 1


toC = 0
fromC = 0

for i in range(n):
    for j in range(n):
        if G[i][j] > 0:
            
            if j == v:
                toC += G[i][j]
            if i == v:
                fromC += G[i][j]

print(fromC, toC)
