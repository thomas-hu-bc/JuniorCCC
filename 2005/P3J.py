"""
Created by Thomas Hu on 2025-09-11 at 6:21 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def main():
    location_directions=["HOME"]
    lines = read_file("input/P3J_input.txt")
    location_index = 0
    while True:
        if lines[location_index]=="SCHOOL":
            break
        else:
            logging.debug(f"{lines[location_index]}")
            location_directions.append(lines[location_index])
        location_index+=1

    logging.debug(location_directions)
    for location_index in range(1, len(location_directions)+1,2):
        direction = location_directions[-location_index]
        if direction == "R":
            back_direction = "LEFT"
        else:
            back_direction = "RIGHT"
        location = location_directions[-location_index-1]
        if location == "HOME":
            print(f"TURN {back_direction} into {location}")
        else:
            print(f"TURN {back_direction} onto {location} street ")


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
