"""
Created by Thomas Hu on 2025-09-08 at 5:44 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

motel_locations = [990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

def get_possible_stops(min_trip, max_trip, start):
    possible_stops = []
    for motel_location in motel_locations:
        if start+min_trip<=motel_location<=start+max_trip:
            possible_stops.append(motel_location)
    logging.debug(f"Possible stops: {possible_stops}")
    return possible_stops

total_found = 0

def find_path(min_trip, max_trip,start,stops):
    global  total_found
    if start<7000:
        possible_stops = get_possible_stops(min_trip,max_trip,start)
        if possible_stops:
            for possible_stop in possible_stops:
                logging.debug(f"Add new stop:{possible_stop} and from {possible_stop} go on")
                stops.append(possible_stop)
                find_path(min_trip,max_trip,possible_stop,stops)
        else:
            logging.debug(f"Impossible")
            return 0
    else:
        logging.debug(f"Reach Goal, {stops}")
        total_found+=1
        return 1


def main():
    global  total_found
    lines = read_file("input/P5J_input.txt")
    line_index = 0
    while line_index<len(lines):
        min_trip = int(lines[line_index])
        max_trip = int(lines[line_index+1])
        insert_no = int(lines[line_index+2])
        logging.debug((f"min trip:{min_trip} max_trip:{max_trip}, insert_no: {insert_no}"))
        for insert in range(insert_no):
            new_location = int(lines[line_index+3+insert])
            motel_locations.append(new_location)
            motel_locations.sort()
        total_found = 0
        find_path(min_trip,max_trip,0,[])
        print(f"{total_found}")
        line_index+=3+insert_no


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
