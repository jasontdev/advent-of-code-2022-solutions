import fileinput

# Part 1


def find_elf_with_most_calories(input_file):
    max_elf = 0
    elf = 0
    for line in fileinput.input(input_file):
        if line == "\n":
            if elf > max_elf :
                max_elf  = elf
            elf = 0
        else:
            elf += int(line)
    return max_elf


print(find_elf_with_most_calories("input"))


# Part 2


def find_elves_with_top_3_most_calories(input_file):
    elves = []
    elf = 0
    for line in fileinput.input(input_file):
        if line == "\n":
            elves.append(elf)
            elf = 0
        else:
            elf += int(line)
    elves.sort()
    return sum(elves[-3:])


print(find_elves_with_top_3_most_calories("input"))

