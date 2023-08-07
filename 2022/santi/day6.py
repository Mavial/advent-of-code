from data_loader import DataLoader


data_loader = DataLoader(day=6)
data = data_loader.load()

""" PART 1 """
def part1():
    for i in range(4, len(data)):
        buffer_slice = data[i-4:i]
        slice_set = set(buffer_slice)
        if len(slice_set) == 4:
            return i

""" PART 2 """
def part2():
    for i in range(14, len(data)):
        buffer_slice = data[i-14:i]
        slice_set = set(buffer_slice)
        if len(slice_set) == 14:
            return i

if __name__ == '__main__':
    part1()
    part2()