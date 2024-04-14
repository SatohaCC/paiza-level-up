import io
import sys

_INPUT = """\
3 1 2
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 完全無向グラフ
# 自己ループと多重辺は考えません。
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
# N, X, Y = map(int, input().split())
n, s, k= map(int, input().split())

G = [[] for _ in range(n)]

for i in range(n):
    b = [a for a in range(n) if a != i]
    G[i]=b

current = s

ans=[current]

for _ in range(k):    
    current = G[current][0]
    ans.append(current+1)

print(*ans)