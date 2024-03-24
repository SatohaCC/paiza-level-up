import io
import sys

_INPUT = """\
3 2
1 2
2 3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# オイラーグラフ・有向グラフ,一筆書き,弱連結
# 有向グラフを無向グラフとしてみたときに、
# の 2 つの頂点間も辺をたどって行き来ができるような場合は、弱連結なグラフといいます。
# 弱連結な有向グラフにおいて、
# ある頂点から始めてすべての辺を一筆書きして最初の頂点に戻ってくることができるための必要十分条件は以下のようになります。
# ・すべての頂点において、入次数と出次数が一致する。
# ---------------------------------------------------------------------------------------------------------

n, m = map(int, input().split())

G = [[0 for _ in range(n)] for _ in range(n)]
# 入次数、出次数を表す配列 indegree, outdegree を 0 で初期化します。
indegree = [0 for _ in range(n)]
outdegree = [0 for _ in range(n)]
for i in range(m):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] += 1

    indegree[b - 1] += 1
    outdegree[a - 1] += 1


ans = True
for i in range(n):
    if indegree[i] == outdegree[i]:
        ans = True
    else:
        ans = False
        break

if ans:
    print(1)
else:
    print(0)
