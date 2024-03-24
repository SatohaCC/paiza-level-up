import io
import sys

_INPUT = """\
5 5
1 2 30
1 3 20
2 4 10
4 5 25
5 2 5
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 重みつき有向グラフ
# 辺があればその重みを出力
# ---------------------------------------------------------------------------------------------------------


# N, M = map(int, input().split())

# G = [[0 for _ in range(N)] for _ in range(N)]
# for i in range(M):  # M
#     a, b, c = map(int, input().split())
#     G[a - 1][b - 1] = c

# for i in range(N):
#     ans = []
#     for j in range(N):
#         if G[i][j]:
#             ans.append(G[i][j])
#     if ans:
#         print(*ans)
#     else:
#         print(-1)


# ---------------------------------------------------------------------------------------------------------
# g[a - 1] に組 (b, c) を追加する解き方
# ---------------------------------------------------------------------------------------------------------

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(M):  # M
    a, b, c = map(int, input().split())
    G[a - 1].append((b, c))

for i in range(N):
    ans = []
    for g in G[i]:
        ans.append(g[1])
    if ans:
        print(*ans)
    else:
        print(-1)
