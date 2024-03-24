import io
import sys

_INPUT = """\
5 5
1 2
1 3
2 4
2 5
4 5
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 2 次数・無向グラフ:入出次数とオイラーグラフについて学ぶ
#
# ---------------------------------------------------------------------------------------------------------


N, M = map(int, input().split())


G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] += 1
    G[b - 1][a - 1] += 1

ans = []
for i in range(N):
    c = 0
    for j in range(N):
        if G[i][j]:
            c += 1
    ans.append(c)

print(*ans)
