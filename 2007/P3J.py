"""
Created by Thomas Hu on 2025-09-08 at 1:44 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

briefcase_map = {1:100,2:500,3:1000,4:5000,5:10000,6:25000,7:50000,8:100000,9:500000,10:1000000}

all_total = 100+500+1000+5000+10000+25000+50000+100000+500000+1000000

def main():
    lines = read_file("input\P3J_input.txt")
    number = int(lines[0])
    briefcases=[]
    total = 0
    for briefcase_no in range(1,number+1):
        briefcase = briefcase_map[int(lines[briefcase_no])]
        briefcases.append(briefcase)
        total+=briefcase
    average = round ((all_total-total)/(10-number))
    offer = int(lines[number+1])
    logging.debug(f"The Offer is {offer}, average is {average},{all_total-total}/{10-number}")
    if offer>average:
        print("deal")
    else:
        print("no deal")


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
