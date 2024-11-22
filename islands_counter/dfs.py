import sys
sys.setrecursionlimit(3000)

from islands_counter.utils import (
    States,
    DIRECTIONS,
    calculate_coordinates_after_movement,
    is_inbound,
    read_input
)


def dfs_solution(world_map: list[list[int]], n: int, m: int) -> int:
    def perform_dfs(row_index, column_index, grid, number_of_rows, number_of_columns):
        for row_direction, column_direction in DIRECTIONS:
            new_row_index, new_column_index = calculate_coordinates_after_movement(
                row_index,
                row_direction,
                column_index,
                column_direction
            )

            if not is_inbound(new_row_index, new_column_index, number_of_rows, number_of_columns):
                continue

            if grid[new_row_index][new_column_index] == States.VISITED_LAND.value:
                continue

            if grid[new_row_index][new_column_index] == States.WATER.value:
                continue

            grid[new_row_index][new_column_index] = States.VISITED_LAND.value
            perform_dfs(new_row_index, new_column_index, grid, number_of_rows, number_of_columns)

    number_of_islands = 0

    for i in range(n):
        for j in range(m):
            if world_map[i][j] == States.UNVISITED_LAND.value:
                perform_dfs(i, j, world_map, n, m)
                number_of_islands += 1

    return number_of_islands


if __name__ == '__main__':
    world_map, n, m = read_input()
    print(f"Number of islands: {dfs_solution(world_map, n, m)}")
