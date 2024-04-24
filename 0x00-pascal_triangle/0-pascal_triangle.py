#!/usr/bin/python3
"""
0-main
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize each row with 1s
        for j in range(1, i):
            # Calculate the value based on the values in the previous row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

# Test the function
print(pascal_triangle(5))
