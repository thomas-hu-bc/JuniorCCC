"""
Created by Thomas Hu on 2025-08-23 at 7:21 p.m.
"""
import logging
from pathlib import Path
from CommonFunction import *
def createCanvas(row,col):
    return [['B' for _ in range(col)] for _ in range(row)]
    # canvas =[]
    # for i in range(row):
    #     row_list = []
    #     for j in range(col):
    #         row_list.append('B')
    #     canvas.append(row_list)
    # return canvas

def changeColor(canvas, row, column):
    logging.debug(f"ChangeColor: {row} {column}")
    if canvas[row][column] == 'B':
        canvas[row][column] = 'G'
    else:
        canvas[row][column]='B'

def makeRowTouch(row,canvas):
    logging.debug(f"MakeRowTouch: {row}")
    length = len(canvas[row])
    for i in range(length):
        # logging.debug(f"{i},{row}")
        changeColor(canvas,row, i)

def makeColTouch(col, canvas):
    logging.debug(f"MakeColTouch: {col}")
    length = len(canvas)
    for i in range(length):
        changeColor(canvas,i,col)

def displayCanvas(canvas):
    for row in canvas:
        logging.debug(row)

def do_instruction(line,canvas):
    location, number = line.split()
    if location=='C':
        logging.debug(f"{location}:{number}")
        makeColTouch(int(number)-1,canvas)
    elif location=='R':
        logging.debug(f"{location}:{number}")
        makeRowTouch(int(number)-1,canvas)
    else:
        logging.debug("Wrong Instruction")

def calculateG(canvas):
    count = 0
    for row in canvas:
        for val in row:
            if val == 'G':
                count+=1
    return count

def main():
    lines = read_file("input\P5_input.txt")
    canvas = createCanvas(int(lines[0]),int(lines[1]))
    touch_num = int(lines[2])
    for touch in range(3, 3+touch_num):
        do_instruction(lines[touch],canvas)
    displayCanvas(canvas)
    result = calculateG(canvas)
    print(result)

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
