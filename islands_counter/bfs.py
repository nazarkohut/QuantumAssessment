from collections import deque

from utils import read_input, States, DIRECTIONS, is_inbound, calculate_coordinates_after_movement


def bfs_solution(world_map: list[list[int]], n: int, m: int) -> int:
    def perform_bfs(row_index, column_index, grid, number_of_rows, number_of_columns):
        dq = deque([(row_index, column_index)])
        while dq:
            ll = len(dq)
            while ll:
                current_row_index, current_column_index = dq.popleft()
                for row_direction, column_direction in DIRECTIONS:
                    new_row_index, new_column_index = calculate_coordinates_after_movement(
                        current_row_index,
                        row_direction,
                        current_column_index,
                        column_direction
                    )

                    if not is_inbound(
                            new_row_index,
                            new_column_index,
                            number_of_rows,
                            number_of_columns
                    ):
                        continue

                    if grid[new_row_index][new_column_index] == States.VISITED_LAND.value:
                        continue

                    if grid[new_row_index][new_column_index] == States.WATER.value:
                        continue

                    dq.append((new_row_index, new_column_index))
                    grid[new_row_index][new_column_index] = States.VISITED_LAND.value

                ll -= 1

    number_of_islands = 0

    for i in range(n):
        for j in range(m):
            if world_map[i][j] == States.UNVISITED_LAND.value:
                perform_bfs(i, j, world_map, n, m)
                number_of_islands += 1

    return number_of_islands


if __name__ == '__main__':
    world_map, n, m = read_input()
    print(f"Number of islands: {bfs_solution(world_map, n, m)}")
