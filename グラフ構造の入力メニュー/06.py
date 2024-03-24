import io
import sys

_INPUT = """\
5 5
1 2
1 3
2 4
4 5
5 2
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# STEP: 2 隣接リストの出力・有向グラフ
# 有向グラフのiに対して、辺のある頂点を出力
# 配列を作ってそこに追加していく。空の場合は-1を出力
# 辺の入力を0で初期化して、+1していくのに注意
# ---------------------------------------------------------------------------------------------------------

N, M = map(int, input().split())
# A, B = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]


G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] += 1


for i in range(N):
    a = []
    for j in range(N):
        if G[i][j] == 1:
            a.append(j + 1)
    if a:
        print(*a)
    else:
        print(-1)
