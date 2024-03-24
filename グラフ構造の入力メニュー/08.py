import io
import sys

_INPUT = """\
5
0 1 1 0 0
1 0 0 1 1
1 0 0 0 0
0 1 0 0 1
0 1 0 1 0
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 無向グラフの自己ループの数を出力
#
# ---------------------------------------------------------------------------------------------------------
N = int(input())
# N, X, Y = map(int, input().split())
# A, B = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]


G = [list(map(int, input().split())) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 1 and i == j:
            ans.append(i + 1)

# 自己ループの数
print(len(ans))

# 自己ループがある頂点
for i in range(len(ans)):
    print(ans[i])
