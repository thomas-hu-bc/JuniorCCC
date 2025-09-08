"""
Created by Thomas Hu on 2025-09-08 at 1:24 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

mapping = {"CU":"see you",
           ":-)":"I'm happy",
           ":-(":"I’m unhappy",
           ";-)":"wink",
           ":-P":"stick out my tongue",
           "(˜.˜)":"sleepy",
           "TA":"totally awesome",
           "CCC":"Canadian Computing Competition",
           "CUZ":"because",
           "TY":"thank-you",
           "YW":"you’re welcome",
           "TTYL":"talk to you later",
           }

def main():
    while(True):
        phase = input("Enter phrase> ")
        if phase=='TTYL':
            print(mapping[phase])
            break
        else:
            for key in mapping.keys():
                index = phase.find(key)
                logging.debug(f"index is {index}")
                if index>=0:
                    map_string = mapping[key]
                    key_length = len(key)
                    phase = phase[:index]+map_string+phase[index+key_length:]

        print(phase)

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
