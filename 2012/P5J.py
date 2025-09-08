"""
Created by Thomas Hu on 2025-09-02 at 5:17 p.m.
"""
import copy
import logging
from pathlib import Path
from Common.CommonFunction import *

history_result=[]
steps = []
total_steps = 0

def get_possible_move(coins_list):
    possible_moves = []
    for position, value in enumerate(coins_list):
        # logging.debug(f"position: {position}, value: {value}")
        if not value:
            continue
        if position< len(coins_list)-1 and (not coins_list[position+1] or value[-1]<coins_list[position+1][-1]) :
            possible_moves.append([position,position+1])
        if position>0 and (not coins_list[position-1] or value[-1]<coins_list[position-1][-1]):
            logging.debug(f"position-1: {position-1} value[-1]: {value[-1]}: coins_list: {coins_list}")
            possible_moves.append([position,position-1])
    logging.debug(f"possible moves are: {possible_moves}")
    return possible_moves


def make_move(coins_list, move):
    from_step, to_step = move
    logging.debug(f"make the move: {move} on the coins_list: {coins_list}")
    new_coins_list = copy.deepcopy(coins_list)
    new_coins_list[to_step].append(new_coins_list[from_step][-1])
    new_coins_list[from_step].pop()
    steps.append(move)
    logging.debug(f"the new coins_list is {new_coins_list}")
    if check_target(new_coins_list):
        return True

    if new_coins_list not in history_result:
        history_result.append(new_coins_list)
        possible_moves = get_possible_move(new_coins_list)
        for possible_move in possible_moves:
            result = make_move(new_coins_list,possible_move)
            if result:
                return True
        steps.pop()
        logging.debug(f"No Possible Move for {new_coins_list}")
        return False
    else:
        logging.debug(f"STEP EXIST {new_coins_list} for {history_result}")
        logging.debug(f"BACK TO {coins_list}!")
        steps.pop()
        return False

def check_target(coins_list):
    global total_steps
    for index, coin in enumerate(coins_list):
        if len(coin)!=1:
            return False
        if index < len(coins_list)-1:
            if len(coins_list[index+1])!=1:
                return False
            if coin[0] <coins_list[index+1][0]:
                continue
            else:
                return False
    logging.debug(f"YES! HIT THE TARGET! {steps} and the total step is {len(steps)}")
    if total_steps > len(steps):
        total_steps = len(steps)
    return True

def main():

    lines = read_file("input/P5J_input.txt")

    i = 0
    while i < len(lines):
        no_coin = int(lines[i])
        # print(no_coin)
        if no_coin>0:
            global history_result, steps, total_steps
            history_result = []
            steps = []
            total_steps = 1000000
            coins = list(map(int, lines[i+1].split()))
            coins_list = [[x] for x in coins]
            logging.debug(coins_list)

            history_result.append(coins_list)
            possible_moves = get_possible_move(coins_list)
            for possible_move in possible_moves:
                make_move(coins_list,possible_move)
            # logging.debug(history_result)
            # logging.debug(f"AAAAAAAAAAAA:{total_steps}")
            if total_steps<1000000:
                print(total_steps)
            else:
                print("IMPOSSIBLE")
        else:
            break
        i= i+2

if __name__ == "__main__":
    log_dir = Path("C:/Logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "WeChat_New_Client.txt"

    logging.basicConfig(
        level=logging.INFO,
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
