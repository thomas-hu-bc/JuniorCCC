"""
Created by Thomas Hu on 2025-08-27 at 12:34 a.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def check_each_page(page_content, page_num, step):
    logging.debug(f"{page_content}:checking page: {page_num}: step:{step}")
    global  shortest_path
    choices = page_content[page_num-1][0]
    # if last page
    if choices == 0: #last page
        if page_content[page_num-1][-1]==0: # never been here,mark the steps
            page_content[page_num-1][-1] = step
            return
        else:
            if page_content[page_num-1][-1]>step:
                page_content[page_num-1][-1] = step # update shortest steps
            return

    # if not the end page, mark page first if it is not marked, otherwise, return
    if page_content[page_num-1][-1]==0:
        page_content[page_num-1][-1]= step
    else:
        return

    for choice in range(1,choices+1):
        check_each_page(page_content,page_content[page_num-1][choice],step+1)

def main():
    lines = read_file("input/P5_input.txt")
    total_pages = int(lines[0])
    page_content=[]
    for line in lines[1:]:
        content = list(map(int, line.split()))
        page_content.append(content+[0])
    display(page_content)
    check_each_page(page_content,1,1)
    logging.debug("result")
    print("---------")
    display(page_content)
    shortest_path = 1000000
    empty_page = "Y"
    for page in page_content:
         if page[-1] == 0:
             empty_page = "N"
         else:
            if page[0] == 0 and shortest_path>page[-1]:
                shortest_path = page[-1]

    print(empty_page,shortest_path)


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
