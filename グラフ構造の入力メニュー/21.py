import io
import sys

_INPUT = """\
3 2
1 2
2 3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 準オイラーグラフ・有向グラフ
# 弱連結な有向グラフにおいて、すべての辺を一筆書きすることができるための必要十分条件
# １ すべての頂点において、入次数と出次数が一致する。
# ２以下の条件をすべて満たす。
# ・(入次数) = (出次数 + 1) となる頂点がちょうど 1 つ存在する。
# ・(入次数 + 1) = (出次数) となる頂点がちょうど 1 つ存在する。
# ・残りのすべての頂点について、入次数と出次数が一致する。
# ---------------------------------------------------------------------------------------------------------


N, M = map(int, input().split())

G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] += 1

leftC = [0 for _ in range(N)]
rightC = [0 for _ in range(N)]

for i in range(N):
    for j in range(N):
        if G[i][j]:
            # +=1ではないので注意
            leftC[i] += G[i][j]
            rightC[j] += G[i][j]


if leftC == rightC:
    print(1)
    exit()

check1 = 0
check2 = 0
check3 = 0

for i in range(N):
    if leftC[i] == rightC[i] + 1:
        check1 += 1
    elif leftC[i] + 1 == rightC[i]:
        check2 += 1
    elif leftC[i] == rightC[i]:
        check3 += 1

if check1 == 1 and check2 == 1 and check3 == N - 2:
    print(1)

else:
    print(0)
