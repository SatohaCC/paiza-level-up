import io
import sys

_INPUT = """\
3 4 1
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

H, W, D = map(int, input().split())

count = 1
ans = [[0]*W for _ in range(H)]

if D == 1:
    ans[0][0] = 1
    count += 1

    for i in range(1, H):
        for j in range(min(i, W - 1) + 1):
            ans[i - j][j] = count
            count += 1
            print(ans)

    for i in range(1, W):
        for j in range(min(H, W - i)):
            ans[H - 1 - j][i + j] = count
            count += 1

elif D == 2:
    for i in range(H):
        for j in range(W):
            ans[i][j] = count
            count += 1

elif D == 3:
    for i in range(W):
        for j in range(H):
            ans[j][i] = count
            count += 1

elif D == 4:
    ans[0][0] = 1
    count += 1

    for i in range(1, W):
        for j in range(min(i, H - 1) + 1):
            ans[j][i - j] = count
            count += 1

    for i in range(1, H):
        for j in range(min(H - i, W)):
            ans[i + j][W - 1 - j] = count
            count += 1

for row in ans:
    print(" ".join(map(str, row)))