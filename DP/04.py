import io
import sys

_INPUT = """\
3 7 -4
5
1
2
3
4
10
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

x, d_1, d_2 = map(int, input().split())

Q = int(input())

ans = [0] * (1000 + 1)

ans[0] = 0
ans[1] = x

for i in range(2, 1000 + 1):
    if i % 2 == 0:
        ans[i] = ans[i - 1] + d_2
    else:
        ans[i] = ans[i - 1] + d_1

for i in range(Q):
    k = int(input())
    print(ans[k])
