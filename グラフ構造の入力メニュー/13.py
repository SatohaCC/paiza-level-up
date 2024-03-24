import io
import sys

_INPUT = """\
5 7
1 2
1 3
2 1
2 4
2 4
4 5
5 2
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 多重辺・有向グラフ (辺入力)
#  G[i][j] > 1 でi→jで２本以上あるケース
# G[i][j] > 0 and G[j][i] > 0でi→jとj→iで合わせて２本以上あるケース
# ---------------------------------------------------------------------------------------------------------


N, M = map(int, input().split())


G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    # 辺の入力を0で初期化して、+1していくのに注意
    G[a - 1][b - 1] += 1


edges = set()
for i in range(N):
    for j in range(N):
        if G[i][j] > 1 or G[i][j] > 0 and G[j][i] > 0:
            tmp = [i + 1, j + 1]
            tmp.sort()
            edges.add(tuple(tmp))

# 多重辺の数を出力
print(len(edges))

for i in edges:
    print(*i)
