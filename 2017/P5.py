
"""
Created by Thomas Hu on 2025-08-28 at 4:28 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def checkMatrix(matrix, no_of_woods):
    wood_result={}
    for i in range(no_of_woods):
        for j in range(i):
            if wood_result.get(matrix[i][j],0) ==0:
                wood_result[matrix[i][j]]=1
            else:
                wood_result[matrix[i][j]]+=1
    logging.debug(wood_result)
    return wood_result


def createMaxtrix(no_of_woods, length_of_woods):
    matrix = []
    for i in range(no_of_woods):
        row =[]
        for j in range(i):
            if i==j:
                row.append(0)
            else:
                row.append(length_of_woods[i]+length_of_woods[j])
        matrix.append(row)
    return matrix


def find_longest_fence(wood_result):
    longest=0
    possible_height = []
    for key, value in wood_result.items():
        logging.debug(f"{key}:{value}")
        if key == 0:
            continue
        if longest<value:
            longest = value
        if key not in possible_height:
            possible_height.append(key)
    logging.debug(f"longest is {longest},number is {len(possible_height)}")
    return longest, len(possible_height)

def main():
    lines = read_file("input/P5_input.txt")
    no_of_wood = int(lines[0])
    length_of_woods = list(map(int, lines[1].split()))
    matrix = createMaxtrix(no_of_wood,length_of_woods)
    display(matrix)
    wood_result = checkMatrix(matrix,no_of_wood)
    length, number = find_longest_fence(wood_result)
    print(length,number)


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
