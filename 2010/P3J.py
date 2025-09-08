"""
Created by Thomas Hu on 2025-09-04 at 2:53 p.m.
"""
import logging
from pathlib import Path

a = 0
b = 0
def get_variable(variable):
    if variable == 'A':
        return a
    else:
        return b

def main():
    global a, b
    instructions=['=','print','+','*','-','/','stop']
    while(True):
        program = input()
        sequence = program.split()
        if len(sequence) ==1:
            break
        elif len(sequence) ==2:
            variable = sequence[1]
            varialbe_rep = get_variable(variable)
            print(f"{variable} is {varialbe_rep}")

        if len(sequence) == 3:
            operator = int(sequence[0])

            if instructions[operator-1]=="=":
                variable_x = sequence[1]
                value = int(sequence[2])
                if variable_x=='A':
                    a = value
                else:
                    b = value
            if instructions[operator-1]=="+":
                variable_x = sequence[1]
                variable_y = sequence[2]
                if variable_x=='A':
                    a = get_variable(variable_x)+get_variable(variable_y)
                else:
                    b = get_variable(variable_x)+get_variable(variable_y)

            if instructions[operator-1]=="-":
                variable_x = sequence[1]
                variable_y = sequence[2]
                if variable_x=='A':
                    a = get_variable(variable_x)-get_variable(variable_y)
                else:
                    b = get_variable(variable_x)-get_variable(variable_y)

            if instructions[operator-1]=="*":
                variable_x = sequence[1]
                variable_y = sequence[2]
                if variable_x=='A':
                    a = get_variable(variable_x)*get_variable(variable_y)
                else:
                    b = get_variable(variable_x)*get_variable(variable_y)

            if instructions[operator-1]=="/":
                variable_x = sequence[1]
                variable_y = sequence[2]
                if variable_x=='A':
                    a = my_round(get_variable(variable_x)/get_variable(variable_y))
                else:
                    b = my_round(get_variable(variable_x)/get_variable(variable_y))

def my_round(value):
    if value>0:
        return round(value-0.5)
    else:
        return round(value+0.5)

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
