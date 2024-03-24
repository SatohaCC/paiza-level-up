import io
import sys

_INPUT = """\
5 5
1 2
1 3
2 4
4 5
5 2
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#  入出次数・有向グラフ
#
# ---------------------------------------------------------------------------------------------------------

n, m = map(int, input().split())


G = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] += 1


fromC = [0 for _ in range(n)]
toC = [0 for _ in range(n)]

# iから出てjに入る
for i in range(n):

    for j in range(n):
        if G[i][j] > 0:
            fromC[j] += G[i][j]
            toC[i] += G[i][j]

print(*fromC)
print(*toC)
