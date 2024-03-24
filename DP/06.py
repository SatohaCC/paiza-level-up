import io
import sys

_INPUT = """\
5
1
2
3
4
3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの入力
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())

Q = int(input())

ans = [0] * (40 + 1)

ans[1] = 1
ans[2] = 1

for i in range(2, 40 + 1):
    ans[i] = ans[i - 2] + ans[i - 1]


for i in range(Q):
    k = int(input())
    print(ans[k])
