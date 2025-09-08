"""
Created by Thomas Hu on 2025-08-24 at 2:20 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def cycling_string(cyc_string):
    letter_list = list(cyc_string)
    new_string = "".join(letter_list[1:])+letter_list[0]
    logging.debug(new_string)
    return new_string


def main():
    lines = read_file("input\P4_input.txt")
    text = lines[0]
    orig_string = lines[1]
    logging.debug(f"{text}:{orig_string}")
    cyc_string = orig_string
    result, i = checkText(cyc_string, text)
    if result:
        print(f"Yes, {text} contains {cyc_string} after {i} cycle")
    else:
        print(f"Yes, {text} does not contain {cyc_string} in any cycle")


def checkText(cyc_string, text):
    length = len(cyc_string)
    for i in range(length):
        logging.debug(f"{cyc_string}:{text}")
        if cyc_string in text:
            return True, i+1
        cyc_string = cycling_string(cyc_string)
    return False, -1

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
