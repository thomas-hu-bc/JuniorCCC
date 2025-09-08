"""
Created by Thomas Hu on 2025-08-25 at 6:20 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def hflip(grid):
    grid[0][0],grid[1][0] = grid[1][0],grid[0][0]
    grid[0][1],grid[1][1] = grid[1][1],grid[0][1]

def vflip(grid):
    grid[0][0],grid[0][1] = grid[0][1],grid[0][0]
    grid[1][0],grid[1][1] = grid[1][1],grid[1][0]

def main():
    grid = [[1,2],[3,4]]
    lines = read_file("input/P4_input.txt")
    instructions = list(lines[0])
    for instruction in instructions:
        if instruction =="H":
            hflip(grid)
        elif instruction == "V":
            vflip(grid)
        else:
            logging.info("Unknown Instruction")
    display(grid)


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
