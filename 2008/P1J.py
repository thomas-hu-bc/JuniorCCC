"""
Created by Thomas Hu on 2025-09-06 at 9:27 p.m.
"""
import logging
from pathlib import Path

def main():
    weight = float(input("Enter weight:"))
    height = float(input("Enter height:"))
    BMI = weight/(height*height)
    if BMI>25:
        print("Overweight")
    elif 25.0>=BMI>18.5:
        print("Normal weight")
    else:
        print("Underweight")

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
