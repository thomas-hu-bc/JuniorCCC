"""
Created by Thomas Hu on 2025-09-11 at 4:29 p.m.
"""
import logging
from pathlib import Path

def plan_a_cost(daytime, evening, weekend):
    cost = 0
    daytime_cost = (daytime-100)*25
    if daytime_cost>0:
        cost+=daytime_cost
    return cost+evening*15+weekend*20

def plan_b_cost(daytime, evening, weekend):
    cost = 0
    daytime_cost = (daytime-250)*45
    if daytime_cost>0:
        cost+=daytime_cost
    return cost+evening*35+weekend*25


def main():
    daytime = int(input("Number of daytime minutes? "))
    evening = int(input("Number of evening minutes? "))
    weekend = int(input("Number of weekend minutes? "))
    plan_a = plan_a_cost(daytime,evening,weekend)
    print(f"Plan A costs {plan_a} cents")
    plan_b = plan_b_cost(daytime,evening,weekend)
    print(f"Plan B costs {plan_b} cents")

    if plan_a>plan_b:
        print("Plan B is cheapest.")
    elif plan_a<plan_b:
        print("Plan A is cheapest.")
    else:
        print("Plan A and B are the same prices.")




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
