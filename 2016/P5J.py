"""
Created by Thomas Hu on 2025-08-29 at 10:22 a.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def main():
    lines = read_file("input\P5J_input.txt")
    choice = int(lines[0])
    total_pair = int(lines[1])
    d_list = list(map(int,lines[2].split()))
    p_list = list(map(int, lines[3].split()))
    d_list.sort()
    if choice==1:
        p_list.sort()
    else:
        p_list.sort(reverse=True)

    total_speed = 0
    for i in range(total_pair):
        total_speed+= max(d_list[i],p_list[i])
    print(total_speed)

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
