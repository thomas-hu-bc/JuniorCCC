"""
Created by Thomas Hu on 2025-09-15 at 11:28 p.m.
"""
import logging
from pathlib import Path
import matplotlib.pyplot as plt

def fractal(level, width, xcoor):
    # initial line (from (0,1) to (width,1))
    ox = [0, width]
    oy = [1, 1]
    size = 2

    for _ in range(level):
        nx, ny = [], []
        k = 0
        for j in range(size - 1):
            # always keep the starting point
            nx.append(ox[j])
            ny.append(oy[j])

            if oy[j] == oy[j+1] and ox[j+1] > ox[j]:  # right
                w = (ox[j+1] - ox[j]) // 3
                nx += [ox[j] + w, ox[j] + w, ox[j] + 2*w, ox[j] + 2*w, ox[j+1]]
                ny += [oy[j], oy[j] + w, oy[j] + w, oy[j], oy[j+1]]

            elif oy[j] == oy[j+1] and ox[j+1] < ox[j]:  # left
                w = (ox[j] - ox[j+1]) // 3
                nx += [ox[j] - w, ox[j] - w, ox[j] - 2*w, ox[j] - 2*w, ox[j+1]]
                ny += [oy[j], oy[j] - w, oy[j] - w, oy[j], oy[j+1]]

            elif ox[j] == ox[j+1] and oy[j+1] < oy[j]:  # down
                w = (oy[j] - oy[j+1]) // 3
                nx += [ox[j], ox[j] + w, ox[j] + w, ox[j], ox[j+1]]
                ny += [oy[j] - w, oy[j] - w, oy[j] - 2*w, oy[j] - 2*w, oy[j+1]]

            elif ox[j] == ox[j+1] and oy[j+1] > oy[j]:  # up
                w = (oy[j+1] - oy[j]) // 3
                nx += [ox[j], ox[j] - w, ox[j] - w, ox[j], ox[j+1]]
                ny += [oy[j] + w, oy[j] + w, oy[j] + 2*w, oy[j] + 2*w, oy[j+1]]

        ox, oy = nx, ny
        size = len(ox)

    # ---- draw fractal using matplotlib ----
    plt.figure(figsize=(8, 8))
    for i in range(size - 1):
        plt.plot([ox[i], ox[i+1]], [oy[i], oy[i+1]], color="black")

    plt.gca().set_aspect("equal", adjustable="box")
    plt.axis("off")
    plt.show()

    # ---- check if (xcoor, y) is on any line ----
    results = []
    for i in range(1, 81):  # y from 1..81
        done = False
        for k in range(size - 1):
            if ox[k] == ox[k+1] and oy[k] < oy[k+1]:  # vertical up
                if xcoor == ox[k] and oy[k] <= i <= oy[k+1]:
                    results.append(i); done = True; break
            elif ox[k] == ox[k+1] and oy[k] > oy[k+1]:  # vertical down
                if xcoor == ox[k] and oy[k+1] <= i <= oy[k]:
                    results.append(i); done = True; break
            elif oy[k] == oy[k+1] and ox[k] < ox[k+1]:  # horizontal right
                if oy[k] == i and ox[k] <= xcoor <= ox[k+1]:
                    results.append(i); done = True; break
            elif oy[k] == oy[k+1] and ox[k] > ox[k+1]:  # horizontal left
                if oy[k] == i and ox[k+1] <= xcoor <= ox[k]:
                    results.append(i); done = True; break
    return results


def main():
    # level = int(input("Enter level: "))
    # width = int(input("Enter width: "))
    # xcoor = int(input("Enter x coordinate: "))
    level = 3
    width = 27
    xcoor = 5

    result = fractal(level, width, xcoor)
    print("Y coordinates where vertical slice crosses fractal:")
    print(result)



if __name__ == "__main__":
    log_dir = Path("C:/Logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "WeChat_New_Client.txt"

    logging.basicConfig(
        level=logging.INFO,
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
