"""
Created by Thomas Hu on 2025-08-30 at 3:19 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

communication_record ={}

def check_communication_record():
    for key,records in communication_record.items():
        total_time =0
        last_record_time = 0
        previous_instruction = None
        for record in records:
            logging.debug(record)
            if record[1]=='R':
                last_record_time = int(record[0])
            else:
                duration = int(record[0])-last_record_time
                total_time+= duration
            previous_instruction = record[1]
        if previous_instruction=='S':
            print(f"{key}:{total_time}")
        else:
            print(f"{key}:-1")


def main():

    lines = read_file("input\P4J_input.txt")
    total_lines = lines[0]
    read_communcation_detail(lines[1:])
    check_communication_record()

    # print(communication_record)


def read_communcation_detail(lines):
    clock = 0
    previous_instruction = None
    for line in lines:
        instruction = line.split()
        current_instruction = instruction[0]
        current_person = instruction[1]
        logging.debug(f"The New Instruction is: {instruction}")
        if previous_instruction and previous_instruction in ['R', 'S'] and current_instruction in ['R', 'S']:
            clock += 1
        previous_instruction = current_instruction
        if instruction[0] == 'W':
            clock += int(current_person)
            continue
        logging.debug(f"The clock is {clock}")
        if current_instruction == 'R':
            if communication_record.get(current_person):
                communication_record[current_person].append([clock, current_instruction])
            else:
                communication_record[current_person] = []
                communication_record[current_person].append([clock, current_instruction])
        elif current_instruction == 'S':
            communication_record[current_person].append([clock, current_instruction])
        else:
            print("Wrong Instruction,please check your input file")


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
