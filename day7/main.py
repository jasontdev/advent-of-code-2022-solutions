import fileinput


class Node:
    total_size_under_limit = 0
    dir_sizes = []

    def __init__(self, name: str, parent=None, size=0):
        self._children = []
        self._parent = parent
        self._name = name
        self._size = size

    def __len__(self):
        return len(self._children)

    def __getitem__(self, item):
        return self._children[item]

    def __setitem__(self, key, value):
        self._children[key] = value

    def add_child(self, name: str, size=0):
        self._children.append(Node(name, self, size))

    def get_name(self):
        return self._name

    def get_parent(self):
        return self._parent

    def get_child(self, name: str):
        for child in self._children:
            if child.get_name() == name:
                return child
        return None

    def size(self):
        if len(self._children) == 0:
            return self._size

        total_size = 0
        for i in self._children:
            total_size += i.size()

        if total_size <= 100000:
            Node.total_size_under_limit += total_size

        Node.dir_sizes.append(total_size)
        return total_size


file = fileinput.input('input')
line = next(file)

root = Node('root')
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

root.size()
print(Node.total_size_under_limit)

free_space = 70_000_000 - root.size()
deficit = 30_000_000 - free_space
dir_sizes = Node.dir_sizes
dir_sizes.sort()

first_greater_than_deficit = 0
for i in dir_sizes:
    if i > deficit:
        first_greater_than_deficit = i
        break
print(deficit)
print(first_greater_than_deficit)

