
"""
Created by Thomas Hu on 2025-08-28 at 4:28 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *
THE_longest = 0
THE_number_of_height =0

def check_at_end(length_record):
    global THE_longest,THE_number_of_height
    longest =0
    number_of_height = 0
    for key, value in length_record.items():
        if longest<value:
            longest = value
        if value!= 0:
            number_of_height +=1

    if longest>THE_longest:
        logging.debug(f"END OF SELECTION:{length_record}")
        logging.debug(f"In this case: longest fence is:{longest}, {number_of_height} different height")
        THE_longest = longest
        THE_number_of_height = 1
    if longest == THE_longest:
        THE_number_of_height += 1


def build_fence(woods,length_record):
    # logging.debug(f"{woods},{length_record}")
    rest_no_woods = len(woods)
    if rest_no_woods <=1:
        check_at_end(length_record)
        return
    for index in range(len(woods)):
        picked_wood = woods[index]
        woods.pop(index)
        for index_j in range(len(woods)):
            another_wood =woods[index_j]
            # logging.debug(f"{picked_wood} and {another_wood} picked")
            value = picked_wood+another_wood
            if not length_record.get(value,0):
                length_record[value]=1
            else:
                length_record[value]+=1
            woods.pop(index_j)
            build_fence(woods,length_record)
            woods.insert(index_j,another_wood)
            length_record[value]-=1
        woods.insert(index, picked_wood)

def main():
    lines = read_file("input/P5_input.txt")
    no_of_wood = int(lines[0])
    woods = list(map(int, lines[1].split()))
    build_fence(woods,{})
    print(THE_longest,THE_number_of_height)


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
