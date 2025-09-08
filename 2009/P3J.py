"""
Created by Thomas Hu on 2025-09-05 at 4:14 p.m.
"""
import logging
from pathlib import Path

def get_time(ottawa_time,zone_info):
    hour = ottawa_time[0]+zone_info[0]
    if hour<0:
        hour = hour+24
    if hour>23:
        hour = hour-24
    minute = ottawa_time[1]+zone_info[1]
    if minute<0:
        minute = minute+60
        hour-=1
    if minute>59:
        minute = minute-60
        hour+=1
    return hour, minute

def main():
    time = input()
    length = len(time)
    if length>2:
        hour = int(time[:len(time)-2])
    else:
        hour = 0
    minute = int(time[-2:])
    logging.debug(f"hour:{hour}:minute{minute}")
    zone = {"Victoria":[-3,0],
            "Edmonton":[-2,0],
            "Winnipeg":[-1,0],
            "Toronto":[0,0],
            "Halifax":[1,0],
            "St. John's":[1,30]}

    for key,zone_info in zone.items():
        zone_hour,zone_minute = get_time([hour,minute],zone_info)
        if zone_hour == 0:
            print(f"{zone_minute:02} in {key}")
        else:
            print(f"{zone_hour}{zone_minute:02} in {key}")



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
