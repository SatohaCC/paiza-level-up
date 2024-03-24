import io
import sys

_INPUT = """\
5
109
110
108
103
100
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())
import bisect

n = int(input())

seq = [int(input()) for _ in range(n)]
dp = [0]
dp[0] = seq[0]

for i in range(n):
    if dp[0] > seq[i]:
        dp.insert(0, seq[i])
    else:

        dp[bisect.bisect_left(dp, seq[i]) - 1] = seq[i]

print(dp)
