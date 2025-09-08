"""
Created by Thomas Hu on 2025-08-23 at 6:09 p.m.
"""
from Common.CommonFunction import *
swap_number = 0
def swap(book_order, location):
    global swap_number
    book_order[location],book_order[location+1] = book_order[location+1],book_order[location]
    swap_number+=1
    logging.debug(f"No.{swap_number}: {book_order} {location}")

def check_swap (book_order, location):
    if 0 <= location < len(book_order):
        return book_order[location]>book_order[location+1]
    return False

def main():
    lines = read_file("input\P4_input.txt")
    book_order = list(lines[0])
    logging.debug(f"my book order is: {book_order}")
    number_of_books = len(book_order)
    swaped = 0
    for location in range (number_of_books-1):
        need_swap = check_swap(book_order,location)
        if need_swap:
            swaped+=1
            swap(book_order,location)
            location = location-1
            while check_swap(book_order,location):
                swaped+=1
                swap(book_order,location)
                location=location-1

    print(f"{swaped}: final: {''.join(book_order)}")

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
    logging.debug("Started")
    main()
    logging.debug("Finished Successfully")
