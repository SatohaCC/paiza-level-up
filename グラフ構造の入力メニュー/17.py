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
# 準オイラーグラフ・無向グラフ
# 連結な無向グラフにおいて、すべての辺を一筆書きすることができるための必要十分条件
# 次数が奇数(Odd)である頂点の個数が、ちょうど 0 または 2 である。
# ---------------------------------------------------------------------------------------------------------

N, M = map(int, input().split())

G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] += 1
    G[b - 1][a - 1] += 1

check_odd = 0
for i in range(N):
    c = 0
    for j in range(N):
        if G[i][j]:
            c += G[i][j]
    if c % 2 != 0:
        check_odd += 1

if check_odd == 0 or check_odd == 2:
    print(1)
else:
    print(0)
