"""
Created by Thomas Hu on 2025-09-06 at 12:50 a.m.
"""
import copy
import logging
from pathlib import Path
from Common.CommonFunction import *

friends = {}
def insert(a, b):
    add_friend(a,b)
    add_friend(b,a)

def add_friend(a, b):
    friends_of_a = friends.get(a)
    if friends_of_a:
        if b in friends_of_a:
            return
        else:
            friends_of_a.append(b)
    else:
        friends[a]=[b,]

def delete_relation(a, b):
     friends[a].remove(b)
     friends[b].remove(a)

def no_friend(a):
    f = friends[a]
    logging.debug(f"friend of {a} are {f}")
    return len(f)

def friends_of_friend(a):
    fs = friends[a]
    ff_list = []
    for f in fs:
        ffs = friends[f]
        for ff in ffs:
            if ff==a or ff in fs or ff in ff_list:
                continue
            else:
                ff_list.append(ff)
    logging.debug(f"friends of friends of {a} are {ff_list}")
    return len(ff_list)

history_path = []
shortest_key_path = None
shortest_length = 1000000
def shortest_path(a, b, step, path):
    global shortest_length, shortest_key_path
    path.append(a)
    fs = friends[a]
    history_path.append(a)
    for f in fs:
        if f==b:
            path.append(f)
            if shortest_length>step:
                shortest_length=step
                shortest_key_path = copy.deepcopy(path)
            logging.debug(f"Found!{path}")
            return
        elif f in history_path:
            continue
        else:
            shortest_path(f,b,step+1,path)
            path.pop()
    return

def main():
    lines = read_file("input/P5J_input.txt")
    for line in lines:
        instructions= line.split()
        logging.debug(instructions)
        if instructions[0]=="i":
            insert(instructions[1],instructions[2])
        if instructions[0]=="d":
            delete_relation(instructions[1],instructions[2])
        if instructions[0]=="n":
            no= no_friend(instructions[1])
            print(f"{no}")
        if instructions[0]=="f":
            no= friends_of_friend(instructions[1])
            print(f"{no}")
        if instructions[0]=="s":
            shortest_path(instructions[1], instructions[2],1,[])
            print(f"{shortest_length}, shortest path:{shortest_key_path}")
        if instructions[0]=="q":
            break

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
