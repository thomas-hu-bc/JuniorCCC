"""
Created by Thomas Hu on 2025-08-24 at 9:27 p.m.
"""
import logging
from pathlib import Path
from CommonFunction import *

exist_jump=[]

# def findPossibleJump(room, row, col, row_length, col_length):
#     exist_jump.append((row,col))
#     value = room[row][col]
#     for i in range(row_length):
#         for c in range(col_length):
#             if (i+1) == row_length and (c+1) == col_length:
#                 return True
#             if (i+1)*(c+1)== value:
#                 if (i,c) in exist_jump:
#                     return False
#                 return findPossibleJump(room,i,c,row_length, col_length)
#     return False

def findPossibleOrignal(room, value, row, col, row_length, col_length):
    if row==0 and col ==0:
        return True
    for r in range(row_length):
        for c in range(col_length):
            jump_value = room[r][c]
            if jump_value == value:
                print(f"row is {r}, col is {c}")
                if (r,c) in exist_jump:
                    return False
                else:
                    exist_jump.append((r,c))
                    if findPossibleOrignal(room, (r+1)*(c+1), r, c,row_length,col_length):
                        return True

    return False

def createRoom(row, col, data):
    room=[]
    for i in range(row):
        col_list= data[i].split()
        col_int_list = [int(x) for x in col_list]
        room.append(col_int_list)
    return room



def main():
    lines = read_file("input\P5_input.txt")
    row = int(lines[0])
    col = int(lines[1])
    room = createRoom(row, col, lines[2:])
    displayRoom(room)
    # result =findPossibleJump(room, 0,0, row, col)
    inital_value = row*col
    result = findPossibleOrignal(room,inital_value,row-1,col-1,row,col)
    if result:
        print("Yes")
    else:
        print("No")




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
