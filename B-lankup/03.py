import io
import sys

_INPUT = """\
5 12
#.#...######
#...##..#.##
###.##.....#
.......####.
#.#..##..##.
1 0
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------


H, W = map(int, input().split())
graph = [list(map(str, input())) for _ in range(H)]
y, x = map(int, input().split())


def change(graph, y, x):
    if graph[y][x] == "#":
        graph[y][x] = "."
    else:
        graph[y][x] = "#"


def add_target(y, x, dy, dx):
    while 0 <= y + dy < H and 0 <= x + dx < W:
        y += dy
        x += dx
        change(graph, y, x)


# 指定された座標を反転
change(graph, y, x)

# 上下左右の座標を反転
for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
    add_target(y, x, dy, dx)

# 斜めの座標を反転
for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
    add_target(y, x, dy, dx)

for row in graph:
    print("".join(row))
