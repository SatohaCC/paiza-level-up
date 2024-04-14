import io
import sys

_INPUT = """\
5 5
2
2 5
3
1 3 5
3
2 4 5
2
3 5
4
1 2 3 4
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 隣接頂点の出力
# 自己ループと多重辺は考えません。
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())
n,s = map(int, input().split())

G = [[] for _ in range(n)]

for i in range(n):
    a = int(input())
    b = list(map(int, input().split()))

    for j in range(len(b)):
        G[i].append(b[j])

print(max(G[s-1]))
