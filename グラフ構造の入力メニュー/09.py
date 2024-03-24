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
# 多重辺・無向グラフ
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]


edges = set()
for i in range(N):
    for j in range(N):
        if G[i][j] > 1 and G[j][i] > 1:
            tmp = [i + 1, j + 1]
            tmp.sort()
            edges.add(tuple(tmp))

print(len(edges))

for i in edges:
    print(*i)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

N = int(input())



G = [list(map(int, input().split())) for j in range(N)]
Ans = []
for i in range(N):
    for j in range(N):
        if G[i][j] > 1:
            a = [i + 1, j + 1]
            a.sort()
            if a not in Ans:
                Ans.append(a)

print(len(Ans))
for i in range(len(Ans)):
    print(*Ans[i])
