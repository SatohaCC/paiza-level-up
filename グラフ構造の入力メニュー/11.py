import io
import sys

_INPUT = """\
5
0 1 1 0 0
0 0 0 1 0
0 0 0 0 0
0 0 0 0 1
0 1 0 0 0
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 多重辺・有向グラフの判定
#  G[i][j] > 1 でi→jで２本以上あるケース
# G[i][j] > 0 and G[j][i] > 0でi→jとj→iで合わせて２本以上あるケース
# ---------------------------------------------------------------------------------------------------------

N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]


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
