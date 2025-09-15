"""
Created by Thomas Hu on 2025-09-09 at 11:45 a.m.
"""
import logging
from pathlib import Path

def main():
    choices = {"burger":[461,431,420,0],"drink":[130,160,118,0],"side":[100,57,70,0],"dessert":[167,266,75,0]}
    print("Welcome to Chip's Fast Food Emporium")
    burger_choice = int(input("Please enter a burger choice:"))-1
    side_choice = int(input("Please enter a side order choice:"))-1
    drink_choice = int(input("Please enter a drink choice:"))-1
    dessert_choice = int(input("Please enter a dessert choice:"))-1
    total = (choices["burger"][burger_choice]+choices['side'][side_choice]
             +choices['drink'][drink_choice]+choices['dessert'][dessert_choice])
    print(f"Your total Calorie count is: {total} ")

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
