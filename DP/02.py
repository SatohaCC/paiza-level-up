import io
import sys

_INPUT = """\
0 7
5
1
2
3
4
5

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

x, d = map(int, input().split())

Q = int(input())

ans = [0] * (1000 + 1)

ans[0] = 0
ans[1] = x

for i in range(2, 1000 + 1):
    ans[i] = ans[i - 1] + d

for i in range(Q):
    n = int(input())
    print(ans[n])
