"""
Created by Thomas Hu on 2025-09-15 at 5:57 p.m.
"""
import logging
from pathlib import Path


def check_monkey_word(word):
    if word == "A":
        return True
    elif word[0]=='A' and word[1]=='N' and check_monkey_word(word[2:]):
        return True
    elif word[0]=='B' and word[-1]=='S' and check_monkey_word(word[1:-1]):
        return True
    else:
        return False

def main():
    lines=["A","ANA","ANANA","BANANAS","BANANA"]
    for word in lines:
        if check_monkey_word(word):
            print(f"{word}: Yes")
        else:
            print(f"{word}: No")

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
