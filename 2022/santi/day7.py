from collections import deque
from data_loader import DataLoader
from typing import Optional, List, Deque


# BUG ON LINE 841 OF THE PROVIDED DATA MUST BE MODIFIED BEFORE RUNNING
# THERE IS ONE TOO MANY "cd .." WHICH LEADS TO A NULL POINTER ON LINE 95
data_loader = DataLoader(day=7)
data = data_loader.load().splitlines()


class File:
    def __init__(
        self, name: str, size: int, parent: Optional["Directory"] = None
    ) -> None:
        self._name: str = name
        self._size: int = size
        self._parent: Optional["Directory"] = parent

    def get_size(self) -> int:
        return self._size


class Directory:
    def __init__(
        self,
        name: str,
        parent: Optional["Directory"] = None,
        children: Optional[List["Directory"]] = None,
        files: Optional[List["File"]] = None,
    ):
        self._name: str = name
        self._parent: Optional["Directory"] = parent
        self._children: List["Directory"] = children or []
        self._files: Optional[List[File]] = files or []

    def add_child(self, child: "Directory") -> None:
        self._children.append(child)

    def get_name(self) -> str:
        return self._name

    def get_parent(self) -> Optional["Directory"]:
        return self._parent

    def get_children(self) -> List["Directory"]:
        return self._children

    def get_child(self, name: str) -> Optional["Directory"]:
        for c in self.get_children():
            if c.get_name() == name:
                return c

    def add_file(self, file: "File") -> None:
        self._files.append(file)

    def get_size(self) -> int:
        size = 0

        for file in self._files:
            size += file.get_size()

        for child in self._children:
            size += child.get_size()

        return size


def handle_cd(tokens: List[str], current_dir: Directory) -> Directory:
    if tokens[2] == "..":
        return current_dir.get_parent()
    else:
        if current_dir.get_name() == tokens[2]:
            return current_dir
        else:
            return current_dir.get_child(tokens[2])


def handle_files_and_dirs(tokens: List[str], current_dir: Directory) -> None:
    if tokens[0] == "dir":
        current_dir.add_child(Directory(tokens[1], parent=current_dir))
    else:
        current_dir.add_file(File(tokens[1], int(tokens[0])))


def build_filesystem() -> Directory:
    root_dir = Directory("/")
    current_dir = root_dir
    for line in data:
        tokens: List[str] = line.split(" ")
        # no need to handle "ls", since it is always followed by files and dirs
        if tokens[0] == "$":
            if tokens[1] == "cd":
                current_dir = handle_cd(tokens=tokens, current_dir=current_dir)
        else:
            handle_files_and_dirs(tokens=tokens, current_dir=current_dir)

    return root_dir


""" PART 1 """


def part1():
    result = 0
    root_dir: Directory = build_filesystem()

    stack: Deque[Directory] = deque([root_dir])
    while stack:
        current_node = stack.pop()
        dir_size = current_node.get_size()
        if dir_size <= 100000:
            result += dir_size
        node_children = current_node.get_children()
        if node_children:
            stack.extend(node_children)

    return result


""" PART 2 """


def part2():
    AVAILABLE_SPACE = 70000000
    REQUIRED_SPACE = 30000000
    result = 70000000

    root_dir: Directory = build_filesystem()
    root_size = root_dir.get_size()

    stack: Deque[Directory] = deque([root_dir])
    while stack:
        current_node = stack.pop()
        dir_size = current_node.get_size()
        if (AVAILABLE_SPACE - root_size) + dir_size >= REQUIRED_SPACE:
            if dir_size < result:
                result = dir_size
            node_children = current_node.get_children()
            if node_children:
                stack.extend(node_children)

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
