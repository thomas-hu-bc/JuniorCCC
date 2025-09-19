"""
Created by Thomas Hu on 2025-09-17 at 7:01 p.m.
"""
import logging
from pathlib import Path


perimeter = 65001
opt_width = 0
opt_length =0
def main():
    global perimeter, opt_width, opt_length
    number_of_photos = 195
    for i in range(number_of_photos):
        width = i+1
        for j in range(number_of_photos, 0, -1):
            length = j+1
            if width*length == number_of_photos:
                temp_perimeter = (width+length)*2
                if perimeter>temp_perimeter:
                    perimeter = temp_perimeter
                    opt_width = width
                    opt_length = length

    print(f"Minimum perimeter is {perimeter} with dimensions {opt_width}x{opt_length}")


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
