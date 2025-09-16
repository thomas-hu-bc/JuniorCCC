"""
Created by Thomas Hu on 2025-09-15 at 6:13 p.m.
"""
import logging
from pathlib import Path

def main():
    start_year = int(input("Enter the current year: "))
    end_year = int(input("Enter a future year: "))
    years = 60
    # all_elected_year = start_year
    print(f"All positions change in year {start_year}")
    all_elected_year = start_year+years
    while all_elected_year<end_year:
        print(f"All positions change in year {all_elected_year}")
        all_elected_year+=years

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
