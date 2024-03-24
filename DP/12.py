import io
import sys

_INPUT = """\
4 2 110 5 200
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

n, x, a, y, b = map(int, input().split())

ans = [1000000000000] * (n + a + b)

ans[0] = 0

for i in range(1, n + a + b):
    if i >= x:
        ans[i] = min(ans[i], ans[i - x] + a)
    if i >= y:
        ans[i] = min(ans[i], ans[i - y] + b)

print(min(ans[n:]))
