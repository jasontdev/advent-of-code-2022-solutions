import fileinput


def process_diagram(input_file):
    diagram_lines = []
    columns = 0

    for line in fileinput.input(input_file):
        if line[0:2] != " 1":
            diagram_lines.append(line.rstrip("\n"))
        else:
            nums = line.rstrip('\n').rstrip(' ')
            columns = int(nums[-1])
            break

    grid = []
    for i in range(0, columns):
        grid.append("")

    for line in diagram_lines[::-1]:
        column = 0
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                grid[column] += line[i]

            column += 1
    fileinput.close()
    print(grid)
    return grid


def process_moves(input_file, grid):
    for line in fileinput.input(input_file):
        words = line.rstrip('\n').split(' ')
        if words[0] == "move":
            n, src, dest = int(words[1]), int(words[3]) - 1, int(words[5]) - 1
            to_move = grid[src][-n:]
            to_move_reversed = to_move[::-1]
            grid[dest] = grid[dest] + to_move_reversed
            grid[src] = grid[src][0:-n]

    return grid


completed_grid = process_moves("input", process_diagram("input"))

tops = ""

for column in completed_grid:
    tops += column[-1]

print(tops)
