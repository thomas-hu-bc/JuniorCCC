"""
Created by Thomas Hu on 2025-09-06 at 9:32 p.m.
"""
import logging
from pathlib import Path

def change(button, song_list):
    if button=='1':
        value = song_list.pop(0)
        song_list.append(value)
        logging.debug(song_list)
    elif button=='2':
        value = song_list.pop()
        song_list.insert(0,value)
        logging.debug(song_list)
    if button=='3':
        value = song_list.pop(0)
        song_list.insert(1,value)
        logging.debug(song_list)

def main():
    song_list = ["A",'B','C','D','E']
    while True:
        button = input("Button number: ")
        number_of_presses = int(input("Number of presses: "))
        if button == '4':
            break
        for i in range(number_of_presses):
            change(button,song_list)
    print(song_list)



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
