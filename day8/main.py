import fileinput


def load_grid(filename):
    file = fileinput.input(filename)

    grid = []
    for row in file:
        grid.append([int(tree) for tree in row.rstrip("\n")])
    return grid


def sum_visible(grid):
    result_grid = []
    for row in grid:
        max_height = 0
        result_row = []

        # Row left to right
        for tree in row:
            if tree > max_height:
                result_row.append(True)
                max_height = tree
            else:
                result_row.append(False)

        # Row right to left
        max_height = 0
        for n in range(len(row) - 1, -1, -1):
            if n == 0 or n == len(row) - 1:
                result_row[n] = True
                max_height = row[n]
            if row[n] > max_height:
                result_row[n] = True
                max_height = row[n]

        result_grid.append(result_row)

    for i in range(0, len(grid[0])):
        max_height = 0

        # Column top to bottom
        for k in range(0, len(grid)):
            if k == 0 or k == len(grid) - 1:
                result_grid[k][i] = True
                max_height = grid[k][i]
            if grid[k][i] > max_height:
                result_grid[k][i] = True
                max_height = grid[k][i]

        max_height = 0
        for k in range(len(grid) - 1, -1, -1):
            if grid[k][i] > max_height:
                result_grid[k][i] = True
                max_height = grid[k][i]

    result = 0
    for row in result_grid:
        for tree in row:
            if tree == True:
                result += 1

    return result


def scenic_score(grid, row, col):
    origin = grid[row][col]
    grid_width = len(grid[row])
    distance_left, distance_right, distance_up, distance_down = 0, 0, 0, 0

    # Looking left
    for n, tree in enumerate(reversed(grid[row][:col])):
        distance_left = n + 1
        if tree >= origin:
            break

    # Looking right
    for n, tree in enumerate(grid[row][col + 1 : grid_width]):
        distance_right = n + 1
        if tree >= origin:
            break

    # Looking up
    for n in range(1, row + 1):
        distance_up = n
        if grid[row - n][col] >= origin:
            break

    # Looking down
    for n in range(1, len(grid) - row):
        distance_down = n
        if grid[row + n][col] >= origin:
            break

    return distance_left * distance_right * distance_up * distance_down


def max_scenic_score(grid):
    max = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            score = scenic_score(grid, row, col)
            if score > max:
                max = score
    return max


grid = load_grid("day8/input")
results = sum_visible(grid)
print(results)
print(max_scenic_score(grid))
