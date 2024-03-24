import io
import sys

_INPUT = """\
6
apple
clang
csharp
gcc
paiza
python
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# しりとり
# 準オイラーグラフ・有向グラフ
# 弱連結な有向グラフにおいて、すべての辺を一筆書きすることができるための必要十分条件
# １ すべての頂点において、入次数と出次数が一致する。
# ２以下の条件をすべて満たす。
# ・(入次数) = (出次数 + 1) となる頂点がちょうど 1 つ存在する。
# ・(入次数 + 1) = (出次数) となる頂点がちょうど 1 つ存在する。
# ・残りのすべての頂点について、入次数と出次数が一致する。
# ---------------------------------------------------------------------------------------------------------
N = 26
M = int(input())
# N = int(input())
# N, X, Y = map(int, input().split())
# A, B = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]
abcd = "abcdefghijklmnopqrstuvwxyz"

G = [[0 for _ in range(N)] for _ in range(N)]

# 入力
# アルファベット２６文字を数字に置き換える
for i in range(M):  # M
    s = input()
    a = abcd.index(s[0])
    b = abcd.index(s[-1])
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
