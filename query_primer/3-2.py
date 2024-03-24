import io
import sys

_INPUT = """\
4 2
16
88
10
-65
2 4
1 2
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

n, k = map(int, input().split())

cuv = [0] * (n + 1)
for i in range(1, n + 1):
    a = int(input())
    cuv[i] = cuv[i - 1] + a

for j in range(k):
    l, r = map(int, input().split())
    print(cuv[r] - cuv[l - 1])
