"""
Created by Thomas Hu on 2025-09-08 at 1:19 p.m.
"""
import logging
from pathlib import Path

def main():
    first=int(input())
    second = int(input())
    third = int(input())
    if first<second:
        first,second = second, first
    if second<third:
        third,second = second,third
    if first<second:
        first,second = second, first

    print(f"The order is {first} {second} {third}, the middle is {second}")


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
