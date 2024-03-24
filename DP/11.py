import io
import sys

_INPUT = """\
4 110 200
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())
n, a, b = map(int, input().split())

dp = [10000000] * (n + 5)

dp[0] = 0

for i in range(2, n + 5):
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + a)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + b)

print(min(dp[n:]))
print(dp[4])
