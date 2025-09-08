"""
Created by Thomas Hu on 2025-09-05 at 3:37 p.m.
"""
import logging
from pathlib import Path
def main():
    third_last = int(input("Digit 11?"))
    second_last = int(input("Digit 12?"))
    last = int(input("Digit 13?"))
    partial_sum = 9*1+7*3+8*1+0*3+9*1+2*3+1*1+4*3+1*1+8*3
    total = partial_sum+third_last*1+second_last*3+last*1
    print (f"The 1-3-sum is {total}")


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
