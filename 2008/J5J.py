"""
Created by Thomas Hu on 2025-09-07 at 2:21 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

losing_position = []
# each reaction = [a, b, c, d] cost
reactions = [
    [2, 1, 0, 2],  # AABDD
    [1, 1, 1, 1],  # ABCD
    [0, 0, 2, 1],  # CCD
    [0, 3, 0, 0],  # BBB
    [1, 0, 0, 1],  # AD
]

def canDo(a, b, c, d):
    """Return True if at least one reaction can be applied."""
    for reaction in reactions:
        new_a = a - reaction[0]
        new_b = b - reaction[1]
        new_c = c - reaction[2]
        new_d = d - reaction[3]
        if min(new_a, new_b, new_c, new_d) >= 0:
            return True
    return False




players = ['Patrick','Roland']

def no_new_reaction(question):
    if question==[0,0,0,0]:
        return True
    if question[0]<0 or question[1]<0 or question[2]<0 or question[3]<0:
        return True
    else:
        return False

def find_solutions(question, player):
    find_one_solution = False
    for reaction in reactions:
        after_new_reaction = [question[0] - reaction[0], question[1] - reaction[1],
                              question[2] - reaction[2], question[3] - reaction[3]]
        if min(after_new_reaction)<0:
            continue
        if max(after_new_reaction)==0:
            logging.debug(f"player: {players[player]} lose!")
            continue
        result, player = find_solutions(after_new_reaction, (player + 1) % 2)
        if result:
            return result,player



def main():
    lines = read_file("input/P5J_input.txt")
    num_lines = int(lines[0])
    for line_index in range(1,num_lines+1):
        logging.debug(line_index)
        a,b,c,d = list(map(int, lines[line_index].split()))
        logging.debug(f"a:{a} b:{b} c:{c} d:{d}")
        find_solutions([a,b,c,d],0)


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
