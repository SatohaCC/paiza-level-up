import io
import sys

_INPUT = """\
4 14
....#.###.####
.#.#.#..####..
..###..#....#.
..#.##....#.#.
3 7
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------


H, W = map(int, input().split())

graph = [list(map(str, input())) for _ in range(H)]

x, y = map(int, input().split())

target = [[x, y]]

if x - 1 >= 0:
    target.append([x - 1, y])

if x + 1 < H:
    target.append([x + 1, y])

if y - 1 >= 0:
    target.append([x, y - 1])

if y + 1 < W:
    target.append([x, y + 1])

print(target)


def change(graph, x, y):
    if graph[x][y] == "#":
        graph[x][y] = "."
    else:
        graph[x][y] = "#"


for tar in target:
    change(graph, tar[0], tar[1])

for row in graph:
    print("".join(row))
