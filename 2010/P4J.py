"""
Created by Thomas Hu on 2025-09-04 at 6:00 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def find_pattern(diff_records):
    length = len(diff_records)
    logging.debug(f"Length of diff_records is:{length}")
    for i in range(1, length+1):
        pattern=diff_records[:i]
        pattern_length = len(pattern)
        logging.debug(f"repeat is {length//pattern_length}, pattern: {pattern}, remainder: {pattern[:length%pattern_length]}")
        if pattern*(length//pattern_length)+pattern[:length%pattern_length] == diff_records:
            return pattern
    return diff_records

def main():
    lines = read_file("input/P4J_input.txt")
    record_index =0
    while True:
        logging.debug(f"Reading record: {lines[record_index]}")
        temp_list = lines[record_index].split()
        no_temp = int(temp_list[0])
        if no_temp> 0:
            temp_records = temp_list[1:]
            diff_records = []
            logging.debug(f"{no_temp}:{temp_records}")

            for index, temp_record in enumerate(temp_records[:-1]):
                diff_records.append(int(temp_records[index+1])- int(temp_records[index]))
            logging.debug(diff_records)
            pattern = find_pattern(diff_records)
            logging.debug(pattern)
            print(len(pattern))
            record_index+=1
        else:
            break


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
