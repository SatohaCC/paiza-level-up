import io
import sys

_INPUT = """\
5 5 3
1 2
1 3
2 4
2 5
4 5
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#  準オイラーグラフ・無向グラフ
#
# ---------------------------------------------------------------------------------------------------------

n, m, v = map(int, input().split())


G = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1

ans = 0

for i in range(n):
    if G[v - 1][i]:
        ans += 1

print(ans)
