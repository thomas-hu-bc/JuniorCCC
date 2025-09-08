"""
Created by Thomas Hu on 2025-08-29 at 12:12 a.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def check_neighbour_cell(cell_situations, i):
    if i==0:
        left_neighbour = cell_situations[-1]
        right_neighbour = cell_situations[1]

    elif i== len(cell_situations)-1:
        left_neighbour= cell_situations[-2]
        right_neighbour = cell_situations[0]

    else:
        left_neighbour = cell_situations[i-1]
        right_neighbour = cell_situations[i+1]

    if left_neighbour + right_neighbour == 1:
        return 1
    else:
        return 0

def main():
    lines = read_file("input\P5_input.txt")
    no_of_cells, no_of_generation = map(int, lines[0].split())
    cell_situations = list(map(int, lines[1]))
    for g in range(no_of_generation):
        new_situation = []
        for i in range(no_of_cells):
            result = check_neighbour_cell(cell_situations,i)
            new_situation.append(result)
        cell_situations = new_situation
    print(cell_situations)

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
