"""
Created by Thomas Hu on 2025-09-11 at 5:03 p.m.
"""
import logging
from pathlib import Path

def valid_RSA(number):
    divisors=2 # since 1 and the number itself is counted
    # logging.debug(f"the half is: {round(number/2)}")
    for i in range(2, round(number/2)+1):
        if number%i==0:
            divisors+=1
            if divisors>4:
                # logging.debug(f"divisors more than 4")
                return False
    # logging.debug(f"divisors: {divisors}")
    return divisors==4

def main():
    lower_limit = int(input("Enter lower limit of range: "))
    upper_limit = int(input("Enter upper limit of range: "))
    count=0
    for num in range(lower_limit,upper_limit+1):
        rsa = valid_RSA(num)
        if rsa:
            logging.debug(f"Yes, {num} RSA")
            count+=1
        else:
            logging.debug(f"No, {num} not RSA")

    print(f"The number of RSA numbers between 11 and 15 is {count}")
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
