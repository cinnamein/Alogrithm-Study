import sys

def divide_and_count(size, x, y):
    global black_count, white_count
    cell_color = grid[x][y]

    # Check if all cells in this quadrant have the same color
    for i in range(y, y + size):
        for j in range(x, x + size):
            if grid[j][i] != cell_color:
                # Colors don't match, divide into quadrants
                divide_and_count(size // 2, x, y)
                divide_and_count(size // 2, x + size // 2, y)
                divide_and_count(size // 2, x, y + size // 2)
                divide_and_count(size // 2, x + size // 2, y + size // 2)
                return

    # Colors match, increment the count
    if cell_color == 1:
        black_count += 1
    else:
        white_count += 1

n = int(sys.stdin.readline())
grid = []

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

black_count, white_count = 0, 0

# Check if the entire grid is already all black or all white
if all(all(cell == 0 for cell in row) for row in grid) or all(all(cell == 1 for cell in row) for row in grid):
    if grid[0][0] == 1:
        black_count += 1
    else:
        white_count += 1
else:
    divide_and_count(n // 2, 0, 0)
    divide_and_count(n // 2, n // 2, 0)
    divide_and_count(n // 2, 0, n // 2)
    divide_and_count(n // 2, n // 2, n // 2)

print(white_count)
print(black_count)
