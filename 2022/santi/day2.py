from data_loader import DataLoader

data_loader = DataLoader(day=2)

data = [n.split(" ") for n in data_loader.load().split("\n")]

""" PART 1 """
def part1():
    options = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
    result_matrix = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]
    score = 0

    for turn in data:
        score += options[turn[1]] + 1
        score += result_matrix[options[turn[0]]][options[turn[1]]]

    return score

""" PART  2 """
def part2():
    options = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 3, 'Z': 6}
    result_matrix = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]
    score = 0

    for turn in data:
        score += options[turn[1]]
        score += result_matrix[options[turn[0]]].index(options[turn[1]]) + 1

    return score

if __name__ == '__main__':
    print(part1())
    print(part2())