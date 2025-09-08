"""
Created by Thomas Hu on 2025-09-06 at 9:51 p.m.
"""
import logging
from pathlib import Path
keyboard = [['A','B','C','D','E','F'],
            ['G','H','I','J','K','L'],
            ['M','N','O','P','Q','R'],
            ['S','T','U','V','W','X'],
            ['Y','Z',' ','-','.','enter']]

def find_location(c):
    global keyboard
    for index, row in enumerate(keyboard):
      if c in row:
          return row.index(c), index
    return 0,0

def goto_enter(x,y):
    enter_x = 5
    enter_y = 4
    step = abs(x-enter_x)+abs(y-enter_y)
    return step

def main():
    word = input()
    cursor_x = 0
    cursor_y = 0
    steps = 0
    for c in list(word):
        to_x, to_y = find_location(c)
        num_move= abs(cursor_x-to_x)+abs(cursor_y-to_y)
        logging.debug(f"from:{cursor_x},{cursor_y} to: {to_x},{to_y} use {num_move}")
        steps+=num_move
        cursor_x=to_x
        cursor_y=to_y
    step= goto_enter(cursor_x,cursor_y)
    print(steps+step)

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
