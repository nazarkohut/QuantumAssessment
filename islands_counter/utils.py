"""
This module provides utility functions and constants to support algorithms that
identify islands in a 2D grid. It includes direction constants, a state enumeration
for grid cells, and helper functions for grid traversal and input handling.
"""
from enum import Enum

MOVE_UP = (0, 1)
MOVE_DOWN = (0, -1)
MOVE_LEFT = (-1, 0)
MOVE_RIGHT = (1, 0)

DIRECTIONS = [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]

class States(Enum):
    WATER = 0
    UNVISITED_LAND = 1
    VISITED_LAND = -1

def read_input() -> tuple[list[list[int]], int, int]:
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return grid, n, m

def is_inbound(row_index: int, column_index: int, number_of_rows: int, number_of_columns: int) -> bool:
    return 0 <= row_index <= number_of_rows - 1 and 0 <= column_index <= number_of_columns - 1

def calculate_coordinates_after_movement(
        current_row_index: int,
        row_direction: int,
        current_column_index: int,
        column_direction: int
) -> tuple[int, int]:
    return current_row_index + row_direction, current_column_index + column_direction
