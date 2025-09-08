"""
Created by Thomas Hu on 2025-08-30 at 11:46 a.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

solutions = []

def add_unique(solution):
    global solutions
    if solution not in solutions:
        solutions.append(solution)

def distribut_piece(people, rest):
    if rest>0:
        no_people = len(people)
        for i in range(no_people):
            people[i]+=1
            distribut_piece(people,rest-1)
            people[i]-=1
    else:
        solution = sorted(people)
        add_unique(solution)
        return

def main():
    lines = read_file("input\P5J_input.txt")
    no_pieces = int(lines[0])
    no_people = int(lines[1])
    rest = no_pieces-no_people
    people=[1]*no_people
    distribut_piece(people, rest)
    print(len(solutions))



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
