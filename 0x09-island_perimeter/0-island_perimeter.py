#!/usr/bin/python3
"""
Define island_perimeter function that finds the perimeter
of an island in a body of water.
"""


def island_perimeter(grid):
    """
    Calculate and return the perimeter of
    the island in the grid.
    Grid is a rectangular grid where 0s represent
    water and 1s represent land.
    Each cell is a square with a side length of 1.
    There is only one island.

    Args:
        grid (list of list of int): 2D list representing the grid.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the upper cell
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the lower cell
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left cell
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right cell
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
