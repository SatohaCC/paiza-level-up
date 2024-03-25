import io
import sys

_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())


A = [int(input()) for _ in range(10000)]

ans = [-1] * 100

for i in range(100):
    start, end = 100 * i, 100 * (i + 1)
    
    ans[i] = max(A[start:end])

for val in ans:
    print(val)
