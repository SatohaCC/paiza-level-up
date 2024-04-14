import io
import sys

_INPUT = """\
10 2 7
1 2 3 4 5 6 7 8 9 10
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 区間の和 1
# 閉域、開域の違いに注意
# 数列 a の範囲を [left, right) としたとき、この範囲の総和は s[right] - s[left] で求めることができる
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
n,l,r= map(int, input().split())
nums = list(map(int, input().split()))

cuv = [0]*(n+1)

for i in range(1,n+1):
    cuv[i] = cuv[i-1] + nums[i-1]

print(cuv[r+1]-cuv[l])