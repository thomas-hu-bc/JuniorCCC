"""
Created by Thomas Hu on 2025-09-15 at 6:27 p.m.
"""
import logging
from pathlib import Path

letter_number_mapping= {"A":0,"B":1,'C':2,'D':3,'E':4,'F':5,'G':6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,
                "N":13,"O":14,'P':15,'Q':16,'R':17,'S':18,'T':19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25,
                }

number_letter_mapping = {v:k for k, v in letter_number_mapping.items()}

def make_shift(index,shift,letter):
    shift_result = letter_number_mapping[letter]+shift
    return number_letter_mapping[shift_result%26]

def main():
    keyword = "TRICKY"
    word = "I LOVE PROGRAMMING!"
    keyword_numbers = []
    for letter in keyword:
        keyword_numbers.append(letter_number_mapping[letter])
    logging.debug(keyword_numbers)

    word_list = []
    for letter in word:
        if letter.isalpha():
            word_list.append(letter)
    logging.debug(word_list)

    keyword_length = len(keyword)
    encrypted_word = []
    for index, letter in enumerate(word_list):
        encrypted_word.append(make_shift(index%keyword_length,keyword_numbers[index%keyword_length],letter))

    print(encrypted_word)



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
