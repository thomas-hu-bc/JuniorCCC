"""
Created by Thomas Hu on 2025-09-04 at 2:13 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def main():
    lines = read_file("input/P2J_input.txt")
    a = int(lines[0])
    b = int(lines[1])
    c = int(lines[2])
    d = int(lines[3])
    steps = int(lines[4])
    nikky = 0
    bryron = 0
    logging.debug(f"Nicky go {a},{b}")
    switch_n = True
    n_f = 0
    n_b = 0
    switch_b = True
    b_f = 0
    b_b = 0
    for i in range(steps):
        if switch_n:
            logging.debug(f"{switch_n}:at {i} steps, the {n_f} steps Nikky move one step forward")
            nikky+=1
            n_f+=1
            if n_f == a:
                logging.debug("Switch")
                switch_n=False
                n_f=0
        else:
            logging.debug(f"at {i} steps, Nikky move one step backward")
            nikky-=1
            n_b+=1
            if n_b == b:
                switch_n=True
                n_b = 0
        if switch_b:
            logging.debug(f"{switch_n}:at {i} steps, the {n_f} steps Nikky move one step forward")
            bryron+=1
            b_f+=1
            if b_f == c:
                logging.debug("Switch")
                switch_b=False
                b_f=0
        else:
            logging.debug(f"at {i} steps, Nikky move one step backward")
            bryron-=1
            b_b+=1
            if b_b == d:
                switch_b=True
                b_b = 0

    print(f"Nikky is at {nikky} and Bryan is at {bryron}")
    if nikky>bryron:
        print("Nikky")
    elif nikky==bryron:
        print("Tie")
    else:
        print("Bryon")


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
