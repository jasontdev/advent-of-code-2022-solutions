import fileinput


# Part 1


def item_to_priority(item: str):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def sum_of_priorities(input_file):
    priorities = []

    for line in fileinput.input(input_file):
        contents = str(line.rstrip('\n'))
        first_rucksack = contents[:len(contents) // 2]
        second_rucksack = contents[len(contents) // 2:]

        items_already_checked = ""
        for item in first_rucksack:
            if items_already_checked.find(item) < 0:  # items can appear more than once
                if second_rucksack.find(item) >= 0:
                    priorities.append(item_to_priority(item))
                    items_already_checked += item

    return sum(priorities)


print(sum_of_priorities("input"))


# Part 2


def identify_groups(input_file):
    group = []
    groups = []

    for line in fileinput.input(input_file):
        if len(group) < 2:
            group.append(line.rstrip('\n'))
        else:
            group.append(line.rstrip("\n"))
            groups.append(group)
            group = []

    priorities = []

    for group in groups:
        for item in group[0]:
            if group[1].find(item) >= 0 and group[2].find(item) >= 0:
                priorities.append(item_to_priority(item))
                break

    return sum(priorities)


print(identify_groups("input"))
