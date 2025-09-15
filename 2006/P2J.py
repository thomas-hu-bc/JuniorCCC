"""
Created by Thomas Hu on 2025-09-09 at 11:52 a.m.
"""
import logging
from pathlib import Path

def main():
    sides_A = int(input("Enter m: "))
    sides_B = int(input("Enter n: "))

    way=0
    for a in range(1,sides_A+1):
        for b in range(1, sides_B+1):
            if a+b==10:
                way+=1
    way_word = "way" if way==1 else "ways"
    print(f"There is {way} {way_word} to get the sum 10")

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
