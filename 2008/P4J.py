"""
Created by Thomas Hu on 2025-09-06 at 10:57 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

operation_stack = []

def getInstruction(operator,rest):
    # op1, op2 = None,None
    first_instruction = rest.pop(0)
    if first_instruction in ["+","-"]:
        op1 = getInstruction(first_instruction,rest)
    else:
        op1 = first_instruction

    second_instruction = rest.pop(0)
    if second_instruction in ["+","-"]:
        op2 = getInstruction(second_instruction,rest)
    else:
        op2 = second_instruction

    return f"{op1} {op2} {operator}"


def main():
    lines = read_file("input/P4J_input.txt")
    line_index = 0
    while True:
        instructions = lines[line_index].split()
        line_index+=1
        if instructions[0]=='0':
            break

        if instructions[0].isdigit():
            print(instructions[0])
            continue

        print(getInstruction(instructions[0],instructions[1:]))

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
