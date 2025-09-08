"""
Created by Thomas Hu on 2025-09-08 at 9:36 a.m.
Simplified version without canMove()
"""
import logging
from pathlib import Path

# CCC 2008 S5: Nukit (Python version with reactions list)

# Each reaction = [a, b, c, d] consumption
reactions = [
    [2, 1, 0, 2],  # AABDD
    [1, 1, 1, 1],  # ABCD
    [0, 0, 2, 1],  # CCD
    [0, 3, 0, 0],  # BBB
    [1, 0, 0, 1],  # AD
]

# Memoization dictionary
used = {}

# def canMove(a, b, c, d):
#     """Return True if at least one reaction can be applied."""
#     for ra, rb, rc, rd in reactions:
#         if a >= ra and b >= rb and c >= rc and d >= rd:
#             return True
#     return False

def losingCombo(a, b, c, d):
    if (a, b, c, d) in used:
        return used[(a, b, c, d)] == 'l'

    # if not canMove(a, b, c, d):
    #     used[(a, b, c, d)] = 'l'
    #     return True

    # Assume losing until proven otherwise
    result = True
    for ra, rb, rc, rd in reactions:
        if a >= ra and b >= rb and c >= rc and d >= rd:
            if not winningCombo(a - ra, b - rb, c - rc, d - rd):
                result = False
                break
    if result:
        used[(a, b, c, d)] = 'l' # if result is True, means Patrick will lose
        return True
    else:
        used[(a, b, c, d)] = 'w'
        return False

def winningCombo(a, b, c, d):
    """Return True if (a,b,c,d) is a winning state."""
    if (a, b, c, d) in used:
        return used[(a, b, c, d)] == 'w'

    # A state is winning if ANY move goes to a losing state
    for ra, rb, rc, rd in reactions:
        if a >= ra and b >= rb and c >= rc and d >= rd:
            if losingCombo(a - ra, b - rb, c - rc, d - rd):
                used[(a, b, c, d)] = 'w'
                return True

    used[(a, b, c, d)] = 'l'
    return False

# -----------------------------
# Example usage:
def main():
    cases = [(0,2,0,2),(1,3,1,3),(1,5,0,3),(3,3,3,3),(8,8,6,7),(8, 8, 8, 8)]
    for case in cases:
        used.clear()
        a, b, c, d = case
        winner = "Patrick" if winningCombo(a, b, c, d) else "Roland"
        print(f"{case} → {winner}")

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
