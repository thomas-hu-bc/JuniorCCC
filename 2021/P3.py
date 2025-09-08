"""
Created by Thomas Hu on 2025-08-23 at 5:38 p.m.
"""
import logging
from pathlib import Path



def interpreter(line, previous_direction):
    first_digit = int(line[0])
    second_digit = int(line[1])
    last_three_digit = int(line[2:])
    sum_2_digit = first_digit+second_digit
    if sum_2_digit:
        if sum_2_digit%2==0:
            return "right", last_three_digit
        else:
            return "left",last_three_digit
    else:
        return previous_direction, last_three_digit

def main():
    lines = read_file("input/P3_input.txt")
    direction = "right"
    for line in lines:
        if line != "99999":
            direction, steps = interpreter(line,direction)
            print(f"{direction} {steps}")
        else:
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
