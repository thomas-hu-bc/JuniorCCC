"""
Created by Thomas Hu on 2025-09-10 at 5:15 p.m.
"""
import logging
from pathlib import Path

boards = {"a": {'w': [(4, 4), (5, 5)], 'b': [(4, 5), (5, 4)]},
          "b": {'b': [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],
                'w': [(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)]},
          "c": {'b': [(1,3), (2, 3), (3, 3), (4, 3), (5,3), (6,3), (7,3), (8,3),
                      (1,4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), ],
                'w': [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
                      (1,6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)]},
          }

check_directions = ["up","down","left","right","left_up","left_down","right_up","right_down"]
color = ["b","w"]

def move_in_direction(r,c,direction):
    next_r, next_c = r,c
    if direction== "down":
        next_r = r+1
        next_c = c
    elif direction == "up":
        next_r = r - 1
        next_c = c
    elif direction == "left":
        next_r = r
        next_c = c-1
    elif direction == "right":
        next_r = r
        next_c = c+1
    elif direction == "left_up":
        next_r = r-1
        next_c = c-1
    elif direction == "left_down":
        next_r = r+1
        next_c = c-1
    elif direction == "right_up":
        next_r = r-1
        next_c = c+1
    elif direction == "right_down":
        next_r = r+1
        next_c = c+1
    else:
        logging.info("Wrong Direction!")
    return next_r, next_c


def check_board(board, move, move_color, direction):
    r, c = move
    other_color = 'b' if move_color == 'w' else 'w'
    possibles =[]
    other_colors= board[other_color]
    # logging.debug(f"{other_color}:pieces: {other_colors}")
    my_colors = board[move_color]
    # logging.debug(f"{move_color}:pieces: {my_colors}")
    next_r,next_c = move_in_direction(r, c, direction)
    if (next_r,next_c) in other_colors:
        possibles.append((next_r,next_c))
        while True:
            next_r,next_c = move_in_direction(next_r, next_c, direction)
            if (next_r,next_c) in other_colors:
                possibles.append((next_r,next_c))
            elif (next_r,next_c) in my_colors:
                logging.debug(f"convert: {direction} {possibles}")
                for possible in possibles:
                    logging.debug(f"{possible} in {other_colors}? {possible in other_colors}")
                    if possible in other_colors:
                        other_colors.remove(possible)
                    logging.debug(f"{possible} in {my_colors}? {possible in my_colors}")
                    if possible not in my_colors:
                        my_colors.append(possible)
                return
            else:
                break


def main():
    # question = ["a",1,5,6]
    question = ["c",3,1,7,2,2,2,1]
    # question = ["c",1,1,7]
    # question =["b",0]
    board = boards[question[0]]
    print(f"Start board: {board}")
    number  = question[1]
    color_index = 0
    for move_index in range(2,number*2+2,2):
        move = (question[move_index],question[move_index+1])
        move_color = color[color_index%2]
        logging.debug(f"color: {move_color}:move: {move}")
        board[move_color].append(move)
        for direction in check_directions:
            logging.debug(f"Now: {direction}")
            check_board(board, move,color[color_index%2],direction)
        move_index+=2
        color_index+=1
    print(f"The Result: b: {len(board['b'])}, w: {len(board['w'])}")
    print(f"The Result board:{board}")

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
