"""
Created by Thomas Hu on 2025-09-01 at 3:20 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

def winning(s, t):
    score = [0, 0, 0, 0]

    # Define the 6 matches as (playerA, playerB)
    matches = [(0, 1), (0, 2), (0, 3),
               (1, 2), (1, 3), (2, 3)]

    # Loop through results
    for result, (a, b) in zip(s, matches):
        if result == "W":
            score[a] += 3
        elif result == "L":
            score[b] += 3
        else:  # Tie
            score[a] += 1
            score[b] += 1

    # Check if player t is the unique winner
    if score[t] == max(score) and score.count(max(score)) == 1:
        print(f"chance is: {s}, my favorite player is {t}, in this case: score is: {score}")
        return True
    return False

from itertools import product

# Matches are fixed: (team1, team2)
MATCHES = [(0, 1), (0, 2), (0, 3),
           (1, 2), (1, 3), (2, 3)]

def build_original(no_games, scores):
    """Build the initial results string based on already played games."""
    original = ["-"] * 6  # start with all games unplayed

    for i in range(no_games):
        a, b, sa, sb = scores[i].split()
        a, b, sa, sb = int(a) - 1, int(b) - 1, int(sa), int(sb)

        if sa > sb:
            letter = "W"
        elif sa < sb:
            letter = "L"
        else:
            letter = "T"

        # map (a, b) to the right index
        index = MATCHES.index((a, b))
        original[index] = letter

    return "".join(original)

def all_possibilities(original):
    """Generate all possible outcome strings filling in '-' with W/L/T."""
    choices = ["W", "L", "T"]
    slots = [(c,) if c != "-" else choices for c in original]
    print(f"slot is {slots}")
    return ("".join(p) for p in product(*slots))

def solution(favorite_player, no_games, scores):
    # Step 1: build the base string
    original = build_original(no_games, scores)
    print("Original:", original)

    # Step 2: generate all possible completions
    possible = list(all_possibilities(original))
    print("Possible outcomes:", possible)

    # Step 3: count winning cases
    count = sum(1 for s in possible if winning(s, favorite_player))
    print("Total winning cases:", count)

def main():
    lines = read_file("input/P5J_input.txt")
    favorite_player = int(lines[0])-1
    no_games = int(lines[1])
    scores = lines[2:]
    solution(favorite_player,no_games,scores)


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
