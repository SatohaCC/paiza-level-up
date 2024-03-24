import io
import sys

_INPUT = """\
11 3 4
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

n, a, b = map(int, input().split())


ans = [0] * (n + 1)

ans[0] = 1

for i in range(1, n + 1):
    if i - a >= 0:
        ans[i] += ans[i - a]
    if i - b >= 0:
        ans[i] += ans[i - b]

print(ans[n])
