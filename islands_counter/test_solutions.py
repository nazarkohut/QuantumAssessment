"""
This module contains a set of test cases to validate the functionality
of the `bfs_solution` and `dfs_solution` functions,
which compute the number of islands in a given world map.

Test cases include:
- Single value islands
- Multiple value islands
- Maps with no islands
- Large and edge case scenarios
"""

from islands_counter.bfs import bfs_solution
from islands_counter.dfs import dfs_solution
from islands_counter.utils import States


# Test Cases
def run_tests(solution_callback):
    test_cases = [
        # Test Case 1: Two single value islands
        {
            "input": (
                [
                    [States.UNVISITED_LAND.value, States.WATER.value],
                    [States.WATER.value, States.UNVISITED_LAND.value],
                ],
                2, 2
            ),
            "expected": 2
        },
        # Test Case 1: One single value island
        {
            "input": (
                [
                    [States.UNVISITED_LAND.value, States.WATER.value],
                    [States.WATER.value, States.WATER.value],
                ],
                2, 2
            ),
            "expected": 1
        },
        # Test Case 3: One multiple value island
        {
            "input": (
                [
                    [States.UNVISITED_LAND.value, States.UNVISITED_LAND.value],
                    [States.UNVISITED_LAND.value, States.WATER.value],
                ],
                2, 2
            ),
            "expected": 1
        },
        # Test Case 4: No islands
        {
            "input": (
                [
                    [States.WATER.value, States.WATER.value],
                    [States.WATER.value, States.WATER.value],
                ],
                2, 2
            ),
            "expected": 0
        },
        # Test Case 5: Five single value islands
        {
            "input": (
                [
                    [States.UNVISITED_LAND.value, States.WATER.value, States.UNVISITED_LAND.value],
                    [States.WATER.value, States.UNVISITED_LAND.value, States.WATER.value],
                    [States.UNVISITED_LAND.value, States.WATER.value, States.UNVISITED_LAND.value],
                ],
                3, 3
            ),
            "expected": 5
        },
        # Test Case 6: Empty input
        {
            "input": (
                [
                    [],
                ],
                0, 0
            ),
            "expected": 0
        },
        # Test Case 7: Line islands separated with water
        {
            "input": (
                [
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1],
                ],
                4, 5
            ),
            "expected": 2
        },
        # Test Case 8: Same as previous but for large map
        {
            "input": (

                [
                    [0 if row_index % 2 else 1 for _ in range(500)] for row_index in range(300)
                ],
                300, 500
            ),
            "expected": 150
        },
        # Test Case 9: Same as previous but in columns
        {
            "input": (

                [
                    [0 if column_index % 2 else 1 for column_index in range(1000)]
                    for __ in range(1500)
                ],
                1500, 1000
            ),
            "expected": 500
        },
        # Test Case 10: Chessboard
        {
            "input": (
                [
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1]
                ],
                8, 8
            ),
            "expected": 32
        },
    ]
    print(f"Calling {solution_callback}...")

    for idx, test in enumerate(test_cases, 1):
        world_map, n, m = test["input"]
        expected = test["expected"]
        result = solution_callback(world_map=world_map, n=n, m=m)
        assert result == expected, f"Test Case {idx} Failed: Expected {expected}, Got {result}"
        print(f"Test Case {idx} Passed!")


run_tests(bfs_solution)
run_tests(dfs_solution)
