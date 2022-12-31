import fileinput


class FSNode:
    dir_sizes = []

    def __init__(self, name: str, parent=None, size=0):
        self._children = []
        self._parent = parent
        self._name = name
        self._size = size

    def add_child(self, name: str, size=0):
        self._children.append(FSNode(name, self, size))

    def get_name(self):
        return self._name

    def get_parent(self):
        return self._parent

    def get_child(self, name: str):
        for child in self._children:
            if child.get_name() == name:
                return child
        return None

    def calc_dir_sizes(self):
        if len(self._children) == 0:
            return self._size

        total_size = 0
        for i in self._children:
            total_size += i.calc_dir_sizes()

        FSNode.dir_sizes.append(total_size)
        return total_size


file = fileinput.input('input')
line = next(file)

root = FSNode('root')
root.add_child('/')
current = root

while line is not None:
    words = line.rstrip('\n').split(' ')
    if words[0:2] == ['$', 'cd']:
        if words[2] == '..':
            current = current.get_parent()
        else:
            current = current.get_child(words[2])
    else:
        if words[0] == 'dir':
            current.add_child(words[1])
        else:
            if words[0].isnumeric():
                current.add_child(words[1], int(words[0]))

    line = next(file, None)

total_size = root.calc_dir_sizes()
dir_sizes = FSNode.dir_sizes
dir_sizes.sort()


# Part 1

def at_most_100000(number):
    return number <= 100_000


smaller_dirs = filter(at_most_100000, dir_sizes)
print(sum(smaller_dirs))


# Part 2

def is_greater_than_deficit(number):
    free_space = 70_000_000 - total_size
    deficit = 30_000_000 - free_space
    return number >= deficit


print(next(filter(is_greater_than_deficit, dir_sizes)))
