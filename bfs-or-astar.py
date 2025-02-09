# Input:
#  ______________
# |x             |
# |              |
# |   |   |      |
# |   |   |      |
# |   |   |______|
# |   |          |
# |   |  X       |
# |   |_______   |
# |              |
# |______________|

# Output:
#  ______________
# |x             |
# |xxxxxxx       |
# |   |  x|      |
# |   |  x|      |
# |   |  x|______|
# |   |  x       |
# |   |  X       |
# |   |_______   |
# |              |
# |______________|


def convert_to_matrix(maze: list[str]) -> list[list[bool]]:
    pass


def add_path_to_maze(maze: list[str], path: list[tuple[int, int]]) -> list[str]:
    pass


def shortest_path(maze: list[str]) -> list[str]:
    matrix = convert_to_matrix(maze)

    path: list[tuple[int, int]] = []

    # start implementing here

    return add_path_to_maze(maze, path)
