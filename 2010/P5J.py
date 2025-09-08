"""
Created by Thomas Hu on 2025-09-04 at 6:30 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

possible_moves = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
history_moves =[]
min_steps = 10000

def find_possible_move(start_point):
    possibles = []
    for move_step in possible_moves:
        possible_x =start_point[0]+move_step[0]
        possible_y = start_point[1]+move_step[1]
        if 9>possible_x>0 and 9>start_point[1]+move_step[1]>0:
            if [possible_x,possible_y] not in history_moves:
                possibles.append(move_step)
    return possibles

def move(start_point,end_point, step=0):
    if start_point==end_point:
        global min_steps
        if min_steps>step:
            min_steps = step
        logging.debug(f"I am successful in {step}")
    else:
        possibles = find_possible_move(start_point)

        for possible in possibles:
            logging.debug(f"{start_point}:{possible}")
            new_x = start_point[0]+possible[0]
            new_y = start_point[1]+possible[1]
            history_moves.append([new_x,new_y])
            move([new_x,new_y],end_point, step=step+1)

def main():
    lines = read_file("input/P5J_input.txt")
    start_point = list(map(int, lines[0].split()))
    end_point = list(map(int, lines[1].split()))
    logging.debug(f"start point: {start_point}")
    logging.debug(f"end point is {end_point}")
    move(start_point,end_point)
    print(min_steps)
    # possibles = find_possible_move([2,1])
    # print(possibles)

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
