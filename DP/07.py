import io
import sys

_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

n = int(input())

ans = [0] * (40 + 1)

ans[0] = 1
ans[1] = 1

for i in range(2, 40 + 1):
    ans[i] = ans[i - 1] + ans[i - 2]

print(ans[n])
