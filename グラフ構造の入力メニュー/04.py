import io
import sys

_INPUT = """\
5 10
0 1 1 0 0
1 0 0 1 1
1 0 0 0 0
0 1 0 0 1
0 1 0 1 0
1 2
1 3
1 4
1 5
2 3
4 2
5 2
4 3
5 3
5 4
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの辺の存在確認
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
N, Q = map(int, input().split())
# A, B = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]

G = [list(map(int, input().split())) for _ in range(N)]


for i in range(Q):  # M
    a, b = map(int, input().split())
    if G[a - 1][b - 1] == 1:
        print(1)  # 存在する
    else:
        print(0)  # 存在しない
