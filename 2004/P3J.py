"""
Created by Thomas Hu on 2025-09-15 at 6:20 p.m.
"""
import logging
from pathlib import Path

def main():
    adj_no=3
    noun_no = 2
    input = ['Easy','Smart','Soft','pie','rock']
    adj_list = input[0:adj_no]
    noun_list = input[adj_no:adj_no+noun_no]
    for adj in adj_list:
        for noun in noun_list:
            print(f"{adj} as {noun}")



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
