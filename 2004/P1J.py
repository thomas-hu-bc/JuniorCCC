"""
Created by Thomas Hu on 2025-09-15 at 6:10 p.m.
"""
import logging
from pathlib import Path

def main():
    number_of_tiles = int(input("Number of tiles? "))
    for i in range (100):
        if i*i>number_of_tiles:
            print(i-1)
            break

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
