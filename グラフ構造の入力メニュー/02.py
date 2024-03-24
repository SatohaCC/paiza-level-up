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
# 有向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------

N, M = map(int, input().split())


# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]

G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1


for i in range(N):
    print(*G[i])
