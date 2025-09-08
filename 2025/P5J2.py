"""
Created by Thomas Hu on 2025-09-01 at 1:42 a.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *


def grid(row, col, c, m):
    return (row * c + col) % m + 1


def min_path_cost(r, c, m):
    prev = [grid(0, i, c, m) for i in range(c)]
    print(prev)
    curr = [0] * c
    print(curr)

    for i in range(1, r):
        # first column
        curr[0] = min(prev[0], prev[1]) + grid(i, 0, c, m)
        print(curr[0])

        # last column
        curr[c - 1] = min(prev[c - 2], prev[c - 1]) + grid(i, c - 1, c, m)

        # middle columns
        for j in range(1, c - 1):
            curr[j] = min(prev[j - 1], prev[j], prev[j + 1]) + grid(i, j, c, m)

        # swap rows
        prev, curr = curr, prev

    return min(prev)

def main():
    lines = read_file("input/P5J_input.txt")
    rows = int(lines[0])
    cols = int(lines[1])
    max_num = int(lines[2])
    print(min_path_cost(rows, cols, max_num))

if __name__ == "__main__":
    log_dir = Path("C:/Logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "WeChat_New_Client.txt"

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),  # log to file
            logging.StreamHandler()  # log to console
        ],
        force=True,
    )
    logging.info("Started")
    main()
    logging.info("Finished Successfully")
