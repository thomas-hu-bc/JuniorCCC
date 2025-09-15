"""
Created by Thomas Hu on 2025-09-09 at 12:03 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

keyboards={
    "a":[2,1],
    "b":[2,2],
    "c":[2,3],
    "d":[3,1],
    "e":[3,2],
    "f":[3,3],
    "g":[4,1],
    "h": [4, 2],
    "i": [4, 3],
    "j": [5, 1],
    "k": [5, 2],
    "l": [5, 3],
    "m": [6, 1],
    "n": [6, 2],
    "o": [6, 3],
    "p": [7, 1],
    "q": [7, 2],
    "r": [7, 3],
    "s": [7, 4],
    "t": [8, 1],
    "u": [8, 2],
    "v": [8, 3],
    "w": [9, 1],
    "x": [9, 2],
    "y": [9, 3],
    "z": [9, 4],
    "-": [0,1],
   }


def main():
    while True:
        word = input()
        if word == "halt":
            break
        total_stoke = 0
        word_char_list = list(word)
        previous_number = 0
        for letter in word_char_list:
            number, stroke = keyboards[letter]
            total_stoke+=stroke
            if previous_number==number:
                total_stoke+=2
            previous_number = number
        print(total_stoke)



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
