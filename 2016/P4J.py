"""
Created by Thomas Hu on 2025-08-30 at 7:49 p.m.
"""
import datetime
import logging
from pathlib import Path
from turtledemo.penrose import start

from Common.CommonFunction import *

schedule = {}

from datetime import time,timedelta
def build_dictionary():
    start_time = datetime.datetime(year=2025, month=8, day=3,hour=0,minute=0)
    # end_time = time(24,0)
    arrive_time = start_time + timedelta(hours=2)
    while arrive_time<datetime.datetime(year=2025, month=8, day=4,hour=0,minute=0):
        arrive_time = start_time + timedelta(hours=2)
        if datetime.datetime(year=2025, month=8, day=3,hour=10,minute=0)>arrive_time>datetime.datetime(year=2025, month=8, day=3,hour=7,minute=0)
        print(f"{start_time}-{arrive_time}")
        start_time = arrive_time


    arrive_hour = 0
    arrive_minute =0
    # for i in range(12):
    #     for j in range(3):
    #         start_hour = i
    #         start_minute = j*20
    #         key = f"{i}:{start_minute}"
    #         arrive_hour = start_hour+2
    #         arrive_minute= start_minute
    #         if 10> arrive_hour >=7:
    #             arrive_minute = start_minute*2
    #             if arrive_minute>80:
    #                 arrive_minute= arrive_minute-60
    #
    #             # logging.debug(f"arrive hour: {arrive_hour}")
    #             # traffic_hour = arrive_hour-7
    #             # traffic_minute = start_minute
    #             # if (start_minute+arrive_minute)>60:
    #             #     traffic_hour+=1
    #             #     arrive_minute = start_minute+traffic_minute-60
    #             # else:
    #             #     arrive_minute = start_minute+traffic_minute
    #             # arrive_hour = arrive_hour+traffic_hour
    #             # logging.debug(f"traffic time: {start_hour}:{start_minute} arrive {arrive_hour}:{arrive_minute}")
    #
    #         # if (7-start_hour)<=2:
    #         #     no_traffic_time = 7-start_hour
    #         #     traffic_time = (2-no_traffic_time)*2
    #         #     traffic_minute = start_minute*2
    #         #     if traffic_minute>60:
    #         #         traffic_time+=1
    #         #         traffic_minute = traffic_minute-60
    #         #     arrive_hour = start_hour+no_traffic_time+traffic_time
    #         #     arrive_minute = traffic_minute
    #         # elif
    #         # else:
    #         #     arrive_hour = start_hour+2
    #         #     arrive_minute = start_minute
    #
    #         schedule[key]= f"{arrive_hour}:{arrive_minute}"

def main():
    lines = read_file("input\P4_input.txt")
    line = lines[0]
    build_dictionary()
    # print(schedule)



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
