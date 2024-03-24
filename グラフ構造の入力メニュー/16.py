import io
import sys

_INPUT = """\
3 4
1 2
1 2
2 3
2 3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# STEP: 3 オイラーグラフ・無向グラフ
# 連結な無向グラフ:ある頂点から始めてすべての辺を一筆書きして最初の頂点に戻ってくることができるための必要十分条件。
#  すべての頂点の次数が偶数である。
# ---------------------------------------------------------------------------------------------------------

# N = int(input())
N, M = map(int, input().split())
# A, B = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]

G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] += 1
    G[b - 1][a - 1] += 1


for i in range(N):
    c = 0
    for j in range(N):
        if G[i][j]:
            c += G[i][j]
    if c % 2 != 0:
        print(0)
        exit()

print(1)
