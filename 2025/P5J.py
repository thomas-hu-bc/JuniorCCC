"""
Created by Thomas Hu on 2025-08-31 at 10:52 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def create_matrix(rows, cols, max_num):
    value = 1
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(value)
            value+=1
            if value>7:
                value = 1
        matrix.append(row)
    return matrix

def find_next_possible_cols(col, cols):
    if col == 0:
        return [col, col+1]
    elif col == cols-1:
        return [col-1,col]
    else:
        return [col-1,col,col+1]

the_least_value = 100000000000000000

def get_total_value(my_path):
    total = 0
    for i in my_path:
        total+=i
    return total

def find_my_path_value(matrix, row, col, rows, cols, my_path):
    global  the_least_value
    logging.debug(f"now I am in {row}:{col}")
    value = matrix[row][col]
    my_path.append(value)
    if rows-1>row:
        possible_cols = find_next_possible_cols(col, cols)
        logging.debug(f"the possible cols are: {possible_cols}")
        for col in possible_cols:
            logging.debug(f"I am going to {col} ")
            find_my_path_value(matrix, row+1, col, rows, cols, my_path)
            logging.debug(f"now the path is: {my_path}")
        my_path.pop()
    else:
        logging.debug(f"The final path is {my_path}")
        total_value = get_total_value(my_path)
        if total_value<the_least_value:
            the_least_value = total_value
            logging.info(f"The least value is updated to {the_least_value} with the {my_path}")
        my_path.pop()


def main():
    lines = read_file("input/P5J_input.txt")
    rows = int(lines[0])
    cols = int(lines[1])
    max_num = int(lines[2])
    matrix = create_matrix(rows, cols,max_num)
    display(matrix)
    my_path = []
    # find_my_path_value(matrix,0,2,rows, cols, my_path)
    for i in range(cols):
        find_my_path_value(matrix, 0,i, rows, cols, my_path)
    print(f"The least value is {the_least_value}")

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
