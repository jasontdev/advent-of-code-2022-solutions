import fileinput


def load_file(filename: str):
    contents = ""
    for line in fileinput.input(filename):
        contents += line

    return contents.rstrip('/n')


def find_start_marker(len_substring: int, buffer: str):
    for i in range(0, len(buffer) - len_substring + 1):
        substring = buffer[i:i + len_substring]

        all_characters_unique = True
        for character in substring:
            if substring.find(character) != substring.rfind(character):
                all_characters_unique = False
                break

        if all_characters_unique:
            return i + len_substring


puzzle_input = load_file("input")
print(f"Part 1: {find_start_marker(4, puzzle_input)}")
print(f"Part 2: {find_start_marker(14, puzzle_input)}")
