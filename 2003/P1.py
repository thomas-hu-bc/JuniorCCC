"""
Created by Thomas Hu on 2025-09-17 at 6:49 p.m.
"""
import logging
from pathlib import Path

def draw_tine(tine_length, tine_space):
    tine = ""
    for i in range (tine_length):
        tine += "*"
        for j in range(tine_space):
            tine+=" "
        tine+="*"
        for j in range(tine_space):
            tine+=" "
        tine+="*\n"
    return tine

def draw_vert(tine_space):
    tine=""
    for i in range(tine_space*2+3):
        tine+="*"
    return tine+"\n"

def draw_handle(tine_space, handle_length):
    tine=""
    for j in range(handle_length):
        for i in range(tine_space+1):
            tine+=" "
        tine+="*\n"
    return tine

def main():
    tine_length = 4
    tine_space = 3
    handle_length = 2
    tine = draw_tine(tine_length,tine_space)
    vert = draw_vert(tine_space)
    handle = draw_handle(tine_space,handle_length)
    print(tine+vert+handle)



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
