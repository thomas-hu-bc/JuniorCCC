"""
Created by Thomas Hu on 2025-08-30 at 1:59 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

alpha = "abcdefghijklmnopqrstuvwxyz"
vowels = 'aeiou'
alpha_list = list(alpha)
vowel_dict = {v: alpha_list.index(v) for v in vowels}

def find_the_closest_vowels(char):
    index = alpha_list.index(char)
    logging.debug(f"{char},{index}")
    closest = 27
    vowel = 'a'
    for key, value in vowel_dict.items():
        abs_diff = abs(value-index)
        # logging.debug(f"{abs_diff}:{value}:{closest}")
        if closest>abs_diff:
            vowel = key
            closest = abs_diff
        else:
            continue
    return vowel

def find_the_following_consonant(charactor):
    index = alpha_list.index(charactor)
    # logging.debug(f"{index}, {len(alpha_list)+1}")
    for no_character in range(index+1,len(alpha_list)):
        if check_consonant(alpha_list[no_character]):
            return alpha_list[no_character]

    return 'z'

def check_consonant(char):
    if char in vowel_dict.keys():
        return False
    else:
        return True

def main():
    lines = read_file("input\P3J_input.txt")
    words = lines[0]
    word_char = list(words)
    new_word =""
    for character in word_char:
        if not check_consonant(character):
            new_word+=character
            continue
        else:
            new_word+=character
            vowel = find_the_closest_vowels(character)
            new_word+=vowel
            # logging.debug(vowel)
            consonant = find_the_following_consonant(character)
            logging.debug(consonant)
            new_word+=consonant
    print(new_word)



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
