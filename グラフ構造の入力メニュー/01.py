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
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())
N, M = map(int, input().split())


# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]

G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1

for i in range(N):
    print(*G[i])
