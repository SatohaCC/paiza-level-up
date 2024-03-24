import io
import sys

_INPUT = """\
9 2 100 3 125 5 200
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

n, x, a, y, b, z, c = map(int, input().split())

dp = [10000000000] * (n + c + 1)

dp[0] = 0

for i in range(1, n + z):
    if i >= x:
        dp[i] = min(dp[i], dp[i - x] + a)
    if i >= y:
        dp[i] = min(dp[i], dp[i - y] + b)
    if i >= z:
        dp[i] = min(dp[i], dp[i - z] + c)


print(min(dp[n:]))
