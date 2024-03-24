import io
import sys

_INPUT = """\
5 7
1 2
1 3
2 2
2 4
4 4
4 5
5 2
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 自己ループ・有向グラフ (辺入力)
# 辺の入力を0で初期化して、+1していくのに注意
# 模範解答：隣接リストを頂点の番号順に見ていき、i == g[i][j] (辺の出ている元の頂点 == 辺の向かっている先の頂点) であれば loops に i + 1 を追加します。
# ---------------------------------------------------------------------------------------------------------


N, M = map(int, input().split())


G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    # 辺の入力を+1していくのに注意
    G[a - 1][b - 1] += 1


edges = []
for i in range(N):
    for j in range(N):
        if G[i][j] > 0 and i == j:
            edges.append(i + 1)

print(len(edges))
for i in range(len(edges)):
    print(edges[i])
