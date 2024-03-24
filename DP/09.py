import io
import sys

_INPUT = """\
10 2 3 4
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

n, a, b, c = map(int, input().split())

ans = [0] * (30 + 1)

ans[0] = 1

for i in range(1, 30 + 1):
    if i - a >= 0:
        ans[i] += ans[i - a]
    if i - b >= 0:
        ans[i] += ans[i - b]
    if i - c >= 0:
        ans[i] += ans[i - c]

print(ans[n])
