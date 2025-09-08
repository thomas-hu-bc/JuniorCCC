"""
Created by Thomas Hu on 2025-09-08 at 2:58 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def main():
    lines = read_file("input/P4J_input.txt")
    word_1 = list(lines[0].replace(" ",""))
    word_2 = list(lines[1].replace(" ",""))
    logging.debug(f" {word_1} sorted: {sorted(word_1)} and {word_2} sorted: {sorted(word_2)}")
    if sorted(word_1) == sorted(word_2):
        print("Is an anagram")
    else:
        print("Is not an anagram")

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
