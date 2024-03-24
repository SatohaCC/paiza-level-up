import io
import sys

_INPUT = """\
10 3
45
74
-94
68
-63
19
-47
-69
38
60
9
5
5
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

n, k = map(int, input().split())

a = [0] * (n + 1)


for i in range(1, n + 1):
    a[i] = int(input()) + a[i - 1]

for j in range(k):
    tar = int(input())
    print(a[tar])
