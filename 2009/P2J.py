"""
Created by Thomas Hu on 2025-09-05 at 3:46 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def main():
    lines = read_file("input/P2J_input.txt")
    brown_trout_point = int(lines[0])
    northern_pike_point = int(lines[1])
    yellow_pickerel_point = int(lines[2])
    total_point = int(lines[3])
    min_point = min(brown_trout_point,northern_pike_point,yellow_pickerel_point)
    max_catch = total_point//min_point
    possible_catch = []
    for trout in range(max_catch+1):
        for pike in range(max_catch+1):
            for pickerel in range(max_catch+1):
                if trout*brown_trout_point+pike*northern_pike_point+yellow_pickerel_point*pickerel<=total_point:
                    possible_catch.append([trout,pike,pickerel])

    for possible in possible_catch:
        if possible != [0,0,0]:
            print(f"{possible[0]} Brown Trout, {possible[1]} Northern Pike,{possible[2]} Yellow Pickerel")
    print(f"Number of ways to catch fish: {len(possible_catch)-1}")


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
