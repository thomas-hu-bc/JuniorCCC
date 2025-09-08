"""
Created by Thomas Hu on 2025-08-25 at 7:08 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *
import copy

def replace (rule, start_s):
    orig,replaced = rule
    idx = start_s.find(orig)
    if idx == -1:
        return start_s, -1
    # logging.debug(f"{idx}:{start_s[:idx]}:{replaced}:{start_s[idx+len(orig):]}")
    replaced_s = start_s[:idx]+replaced+start_s[idx+len(orig):]
    return replaced_s, idx

def convert(start_s, end_s, step, rules, history):
    logging.debug(f"TRY:step: {5-step}: {start_s} -> {end_s} : {history}")
    if step>0:
        for rule in rules:
            replaced_s, index = replace(rule,start_s)
            if index == -1:
                logging.debug(f"Rule: {rule} does not work for {start_s}, retreat!")
                continue
            logging.debug(f"Rule: {rule} works for {start_s},{index}, convert to {replaced_s}, save in history and go!")
            history.append((step,index,rule, start_s,replaced_s))
            if (convert(replaced_s,end_s,step-1,rules,history)):
                return True
    else:
        if start_s == end_s:
            logging.info(f"YES! {history}")
            return True
        else:
            logging.debug(f"LAST STEP, NO MATCH, retreat!")
            history.pop()
            return False


def main():
    lines = read_file("input/P5_input.txt")
    rules=[]
    for i in range(3):
        rules.append(lines[i].split())
    # logging.debug(rules)
    step, start_s, end_s = lines[3].split()
    logging.debug(f"TARGET: convert from {start_s} to {end_s} in {step}")
    history=[]
    convert(start_s,end_s,int(step),rules,history)

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
    # replaced,index = replace(["C","AA"],"BBC")
    # logging.debug(f"{replaced}:{index}")
    main()
    logging.info("Finished Successfully")
