"""
Created by Thomas Hu on 2025-09-05 at 10:57 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def replace_one_space(sentence_word,average):
    for index, word in enumerate(sentence_word):
        if word==".":
            sentence_word[index]="."*(average+1)

def tail_space(sentence_word,w):
    first_word= sentence_word[0]
    second_word = "."*(w-len(first_word))
    sentence_word.append(second_word)

def insert_space_before_smaller_word(sentence_word,extra_space):
    short_words=[]
    for i in range(extra_space):
        shortest_word_index = 0
        shortest_word_length = 7
        for index, word in enumerate(sentence_word[1:], start=1):
            if word in short_words or word[0]==".":
                continue
            else:
                word_length = len(word)
                if shortest_word_length>word_length:
                    shortest_word_length = word_length
                    shortest_word_index = index
        short_words.append(sentence_word[shortest_word_index])
        sentence_word.insert(shortest_word_index,".")


def main():
    words = ["WELCOME","TO","CCC","GOOD","LUCK","TODAY"]
    w = int(input("Enter w:"))
    sentence_words = break_into_sentences(w, words)
    for sentence_word in sentence_words:
        word_length = 0
        space_num = 0
        for word in sentence_word:
            word_length+= len(word)
            if word == ".":
                space_num+=1
        more_space = w - word_length
        average = 0
        extra_space = 0
        if space_num == 0:
            tail_space(sentence_word,w)
        else:
            average= more_space//space_num
            extra_space = more_space % space_num

        if average>0:
            replace_one_space(sentence_word, average)
        if extra_space:
            logging.debug(f"extra space: {extra_space},the middle part are {sentence_word[1:-1]}")
            insert_space_before_smaller_word(sentence_word,extra_space)

        logging.debug(f"In {sentence_word}, word_length: {word_length},  ")
        # sentence_word[1:-1]:
        #     logging.debug(f"words are {words}")



def break_into_sentences(w: int, words: list[str]):
    sentence_length = 0
    sentence_words = []
    sentence_index = 0
    sentence_words.append([])
    for index, word in enumerate(words):
        sentence_length += len(word)
        if sentence_length <= w:
            sentence_words[sentence_index].append(word)
            sentence_words[sentence_index].append(".")
            sentence_length+=1
            continue
        else:
            sentence_words[sentence_index].pop()
            sentence_words.append([word,".",])
            sentence_index += 1
            sentence_length = len(word)+1
    sentence_words[sentence_index].pop()
    return sentence_words


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
