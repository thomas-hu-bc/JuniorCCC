"""
Created by Thomas Hu on 2025-08-29 at 12:32 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def check_palindrome(char_list, i):
    palindrome_type = -1
    number =1
    while i-number>=0 and len(char_list)>i+number:
        if char_list[i-number]== char_list[i+number]:
            logging.debug(f"Type I: {char_list[i-number]} and {char_list[i+number]} are the same")
            palindrome_type =1
            number+=1
        elif char_list[i-number+1]==char_list[i+number]:
            logging.debug(f"Type II: {char_list[i-number+1]} and {char_list[i+number]} are the same")
            palindrome_type = 0
            number+=1
        else:
            return number, palindrome_type
    return number, palindrome_type

def main():
    lines = read_file("input/P3J_input.txt")
    text = lines[0]
    char_list = list(text)
    max_number = 1
    for i in range(1,len(char_list)-1):
        num, palindrome_type = check_palindrome(char_list,i)
        if palindrome_type>=0:
            num = num*2-palindrome_type
        logging.debug(f"{char_list}: the number: {i}, found: {num} the max_num:{max_number}")
        max_number = num if num>max_number else max_number
    print(max_number)


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
