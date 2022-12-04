import fileinput

# Part 1


def get_ranges(line: str):
    first_str, second_str = line.rstrip('\n').split(',')
    section1 = first_str.split('-')
    section2 = second_str.split('-')

    # ranges in file have inclusive upper value, Python ranges have exclusive upper value
    ranges = [range(int(section1[0]), int(section1[1]) + 1)]
    ranges.append(range(int(section2[0]), int(section2[1]) + 1))
    return ranges


def find_contained_ranges(input_file):
    contained_ranges = 0

    for line in fileinput.input(input_file):
        range1, range2 = get_ranges(line)

        # - 1 to compensate for exclusive range stop value
        if range1.start in range2 and range1.stop - 1 in range2:
            contained_ranges += 1
        else:
            if range2.start in range1 and range2.stop - 1 in range1:
                contained_ranges += 1

    return contained_ranges


print(find_contained_ranges("input"))

# Part 2


def overlapping_assignment_pairs(input_file):
    overlaps = 0

    for line in fileinput.input(input_file):
        range1, range2 = get_ranges(line)

        if range1.start in range2 or range1.stop -1 in range2:
            overlaps += 1
        else:
            if range2.start in range1 or range2.stop -1 in range1:
                overlaps += 1

    return overlaps


print(overlapping_assignment_pairs("input"))
