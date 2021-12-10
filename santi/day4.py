import copy
import requests
import os

# Import file and data
cookies = {"session": os.getenv("SESSION")}
input = [val for val in requests.get(
    "https://adventofcode.com/2021/day/4/input", cookies=cookies
).text.split("\n\n")]

test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\n 22 13 17 11  0\n 8  2 23  4 24\n 21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19\n\n 3 15  0  2 22\n 9 18 13 17  5\n 19  8  7 25 23\n 20 11 10 24  4\n 14 21 16 12  6\n\n 14 21 17 24  4\n 10 16 15  9 19\n 18  8 23 26 20\n 22 11 13  6  5\n 2  0 12  3  7"""
# input = [val for val in test.split("\n\n")]


game_num = input.pop(-0).split(",")
bboards = [{"board": board_num, "marked": set(), "data": {row_num: {col: val for col, val in enumerate(row.strip().replace(
    "  ", " ").split(" ",), start=1)} for row_num, row in enumerate(board.strip().split("\n"), start=1)}} for board_num, board in enumerate(input)]


def win_check(marked, last_placed):
    pass
    if sum([t[1] for t in [m for m in marked if m[0] == last_placed[0]]]) == 15:
        return [m for m in marked if m[0] == last_placed[0]], "row"
    elif sum([t[0] for t in [m for m in marked if m[1] == last_placed[1]]]) == 15:
        return [m for m in marked if m[1] == last_placed[1]], "col"
    else:
        return None


"""Part 1 - This is far from ideal. Please do not use as reference"""


def part1(game_num, bboards):
    for num in game_num:
        for bboard in bboards:
            for row in bboard["data"]:
                for col in bboard["data"][row]:
                    if bboard["data"][row][col] == num:
                        bboard["marked"].add((row, col))
                        res = win_check(bboard["marked"], (row, col))
                        if res:
                            win_num = int(bboard["data"][row][col])
                            if res[1] == "row":
                                added_res = sum(sum([int(bboard["data"][r][c]) for c in bboard["data"][r] if (
                                    r, c) not in bboard["marked"]]) for r in bboard["data"])
                            else:
                                added_res = sum(sum([int(bboard["data"][r][c]) for r in bboard["data"] if (
                                    r, c) not in bboard["marked"]]) for c in bboard["data"][row])
                            print(
                                f"Board: {bboard['board']+1} Result: {win_num*added_res}")
                            return True


part1(copy.copy(game_num), copy.deepcopy(bboards))


"""Part 2 - Equally terrible code"""


def part2(game_num, bboards):
    need_new_bboard = False
    won_board_count = 0
    for num in game_num:
        for bboard in bboards:
            if "won" in bboard:
                continue
            for row in bboard["data"]:
                if need_new_bboard:
                    need_new_bboard = False
                    break
                for col in bboard["data"][row]:
                    if bboard["data"][row][col] == num:
                        bboard["marked"].add((row, col))
                        res = win_check(bboard["marked"], (row, col))
                        if res and won_board_count >= len(bboards)-1:
                            win_num = int(bboard["data"][row][col])
                            if res[1] == "row":
                                added_res = sum(sum([int(bboard["data"][r][c]) for c in bboard["data"][r] if (
                                    r, c) not in bboard["marked"]]) for r in bboard["data"])
                            else:
                                added_res = sum(sum([int(bboard["data"][r][c]) for r in bboard["data"] if (
                                    r, c) not in bboard["marked"]]) for c in bboard["data"][row])
                            print(
                                f"Board: {bboard['board']+1} Result: {win_num*added_res}")
                            return True
                        elif res:
                            bboard["won"] = True
                            won_board_count += 1
                            need_new_bboard = True
                            break


part2(copy.copy(game_num), copy.deepcopy(bboards))
