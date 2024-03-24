import io
import sys

_INPUT = """\
3 3 3
1 2 3
4 5 6
7 8 9
1 1
2 2
3 3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())
H, W, N = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(H)]

ans = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        ans[i][j] = ans[i - 1][j] + ans[i][j - 1] - ans[i - 1][j - 1] + A[i - 1][j - 1]

for j in range(N):
    y, x = map(int, input().split())
    print(ans[y][x])
