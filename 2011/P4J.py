"""
Created by Thomas Hu on 2025-09-03 at 9:51 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def create_picture():
    picture = []
    for i in range(200):
        picture.append([0]*400)
    return picture

def convert_cor(a, b):
    x = -a
    y = b+200
    return x,y

def convert_back_cor(a, b):
    x = -a-1
    y = b-200
    return x, y

def move(from_x,from_y,direction,steps,picture):
    status = "safe"
    if direction == 'r':
        for i in range(steps):
            from_y+=1
            if picture[from_x][from_y]:
                status = "DANGER"
            else:
                picture[from_x][from_y] = 1

    if direction == 'd':

        for i in range(steps):
            from_x += 1
            if picture[from_x][from_y]:
                status = "DANGER"
            else:
                picture[from_x][from_y] = 1

    if direction == 'l':

        for i in range(steps):
            from_y -= 1
            if picture[from_x][from_y]:
                status = "DANGER"
            else:
                picture[from_x][from_y] = 1

    if direction == 'u':
        for i in range(steps):
            from_x -= 1
            if picture[from_x][from_y]:
                status = "DANGER"
            else:
                picture[from_x][from_y] = 1
    # print(status)
    return from_x, from_y, status

def main():
    lines = read_file("input/P4J_input.txt")
    picture = create_picture()
    from_x, from_y = convert_cor(0,0)
    picture[from_x][from_y]=1
    from_x, from_y, status = move(from_x,from_y,'d',2,picture)
    from_x, from_y, status = move(from_x,from_y,'r',3, picture)
    from_x, from_y, status = move(from_x,from_y,'d',2,picture)
    from_x, from_y, status = move(from_x,from_y,'r',2, picture)
    from_x, from_y, status = move(from_x,from_y,'u',2,picture)
    from_x, from_y, status = move(from_x,from_y,'r',2, picture)
    from_x, from_y, status = move(from_x,from_y,'d',4,picture)
    from_x, from_y, status = move(from_x,from_y,'l',8, picture)
    from_x, from_y, status = move(from_x,from_y,'u',2, picture)
    line_index=0
    while (True):
        direction, steps = lines[line_index].split()
        steps_num = int(steps)
        if direction =='q':
            break
        logging.debug(f"{direction} {steps_num}")
        line_index+=1
        from_x, from_y, status = move(from_x, from_y, direction, steps_num, picture)
        x, y = convert_back_cor(from_x,from_y)
        print(f"{y} {x} {status}")
    logging.debug(convert_back_cor(from_x,from_y))


    display(picture)

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
