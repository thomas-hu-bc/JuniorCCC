"""
Created by Thomas Hu on 2025-09-01 at 3:20 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

rep_order = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

def winning(s, t):
    score = [0, 0, 0, 0]
    if s[0] == "W":
        score[0] = score[0] + 3
        score[1] = score[1] + 0
    elif s[0] == "L":
        score[0] = score[0] + 0
        score[1] = score[1] + 3
    else:
        score[0] = score[0] + 1
        score[1] = score[1] + 1
    if s[1] == "W":
        score[0] = score[0] + 3
        score[2] = score[2] + 0
    elif s[1] == "L":
        score[0] = score[0] + 0
        score[2] = score[2] + 3
    else:
        score[0] = score[0] + 1
        score[2] = score[2] + 1
    if s[2] == "W":
        score[0] = score[0] + 3
        score[3] = score[3] + 0
    elif s[2] == "L":
        score[0] = score[0] + 0
        score[3] = score[3] + 3
    else:
        score[0] = score[0] + 1
        score[3] = score[3] + 1
    if s[3] == "W":
        score[1] = score[1] + 3
        score[2] = score[2] + 0
    elif s[3] == "L":
        score[1] = score[1] + 0
        score[2] = score[2] + 3
    else:
        score[1] = score[1] + 1
        score[2] = score[2] + 1
    if s[4] == "W":
        score[1] = score[1] + 3
        score[3] = score[3] + 0
    elif s[4] == "L":
        score[1] = score[1] + 0
        score[3] = score[3] + 3
    else:
        score[1] = score[1] + 1
        score[3] = score[3] + 1
    if s[5] == "W":
        score[2] = score[2] + 3
        score[3] = score[3] + 0
    elif s[5] == "L":
        score[2] = score[2] + 0
        score[3] = score[3] + 3
    else:
        score[2] = score[2] + 1
        score[3] = score[3] + 1


    if score[t] == max(score) and score.count(max(score)) == 1:
        print(f"chance is: {s}, my favorite player is {t}, in this case: score is: {score}")
        return True
    else:
        return False

def winning2(s, t):
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

def check_winning(possible):
    players=[0,0,0,0]
    for index, result in enumerate(possible):
        if result=='W':
            player1, player2 = rep_order[index]
            players[player1]+=3
        elif result == 'L':
            player1, player2 = rep_order[index]
            players[player2]+=3
        else:
            player1, player2 = rep_order[index]
            players[player1]+=1
            players[player2]+=1
    return players.index(max(players))

def get_product_data(games):
    product_data =[]
    for game in games:
        if game=='':
            product_data.append(['W','L','T'])
        else:
            product_data.append(game)
    return product_data

from itertools import product
# def generate_product(n):
#     choice =['W','L','T']
#     result = list(product(choice,repeat=n))
#     return result


def find_possibilities(game_card):
    product_data = get_product_data(game_card)
    print(product_data)
    possibilities = list(product(*product_data))
    print(possibilities)
    return possibilities

    # new_game_id_list = find_new_games(game_card)
    # print(new_game_id_list)
    # possible_permutation = generate_product(6-len(new_game_id_list))
    # # print(possible_permutation)
    # possibilities = []
    # for value_list in possible_permutation:
    #     # print(value_list)
    #     new_game_card = game_card
    #     for position in new_game_id_list:
    #         for value in value_list:
    #             new_game_card[position]= value
    #             print(new_game_card)
    #     possibilities.append(new_game_card)
    #
    # print(possibilities)
    # possible = []
    #
    # goto = []
    # for i in range(6):
    #     if original[i] == "-":
    #         goto.append(3)
    #     else:
    #         goto.append(1)
    # print(goto)
    #
    # for a in range(goto[0]):
    #     for b in range(goto[1]):
    #         for c in range(goto[2]):
    #             for d in range(goto[3]):
    #                 for e in range(goto[4]):
    #                     for f in range(goto[5]):
    #                         s = ""
    #                         if goto[0] == 1:
    #                             s = s + original[0]
    #                         else:
    #                             s = s + choice[a]
    #                         if goto[1] == 1:
    #                             s = s + original[1]
    #                         else:
    #                             s = s + choice[b]
    #                         if goto[2] == 1:
    #                             s = s + original[2]
    #                         else:
    #                             s = s + choice[c]
    #                         if goto[3] == 1:
    #                             s = s + original[3]
    #                         else:
    #                             s = s + choice[d]
    #                         if goto[4] == 1:
    #                             s = s + original[4]
    #                         else:
    #                             s = s + choice[e]
    #                         if goto[5] == 1:
    #                             s = s + original[5]
    #                         else:
    #                             s = s + choice[f]
    #                         possible.append(s)
    # print(possible)
    #
    # count = 0
    # for s in possible:
    #     if winning(s, favorite_player):
    #         print(f"When {s},{favorite_player} could win")
    #         count = count + 1
    #
    # print(count)


def build_game_card(no_games, scores) ->list:
    original = ['']*6
    for i in range(no_games):
        player_1, player_2, score_a, score_b = scores[i].split()
        player_1_id, player_2_id = int(player_1) - 1, int(player_2) - 1
        if int(score_a) > int(score_b):
            letter = "W"
        elif int(score_a) < int(score_b):
            letter = "L"
        else:
            letter = "T"

        index = rep_order.index([player_1_id, player_2_id])
        # print(index)
        original[index]=letter
    # print(original)
    return original


def main():
    lines = read_file("input/P5J_input.txt")
    favorite_player = int(lines[0])-1
    no_games = int(lines[1])
    # scores = lines[2:]
    game_card = build_game_card(no_games, lines[2:])
    print(game_card)
    possibilities = find_possibilities(game_card)
    count = 0
    for possible in possibilities:
        winner = check_winning(possible)
        if winner== favorite_player:
            count+=1
    print(f"Count for {favorite_player+1} is :{count}")
    # generate_product(3)


    # solution(favorite_player,no_games,scores)


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
