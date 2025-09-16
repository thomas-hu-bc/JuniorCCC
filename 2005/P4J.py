import logging


def cross_spiral(w, h, cw, ch, steps, debug=False):
    # Initialize grid with borders
    g = [[0] * 22 for _ in range(22)]

    for i in range(22):
        for j in range(22):
            if (1 <= i <= h and 1 <= j <= w and
                not ((i <= ch and (j <= cw or j > w - cw)) or
                     (i > h - ch and (j <= cw or j > w - cw)))):
                g[i][j] = 99

    # Starting position
    c = cw + 1
    r = 1
    direction = 'e'  # 0=right, 90=up, 180=left, 270=down

    for step in range(1,steps+1):
        # print(f"{r}:{c}:{step}")
        g[r][c] = step  # mark as visited
        moving = True

        if direction == 'e':  # right
            if g[r-1][c]==99: # if you can go up, then go up,
                r -= 1; direction = 'n'
            elif g[r][c+1]==99: # if you can't go up, if you can go straight, go straight
                c += 1; direction = 'e'
            elif g[r+1][c]==99: # can not go up, can not go straight, can you go down? then go down
                r += 1; direction = 's'
            elif g[r][c-1]==99: # can not go up, can not go straight and can not go down, can you go back?
                c -= 1; direction = 'w'
            else: # can not move any more
                moving = False

        elif direction == 'n':  # up
            if g[r][c-1]== 99: # can you go west?
                c -= 1; direction = 'w'
            elif g[r-1][c]==99: # north is through
                r -= 1; direction = 'n'
            elif g[r][c+1]==99:
                c += 1; direction = 'e'
            elif g[r+1][c]==99:
                r += 1; direction = 's'
            else:
                moving = False

        elif direction == 'w':  # left
            if g[r+1][c]==99:
                r += 1; direction = 's'
            elif g[r][c-1]==99:
                c -= 1; direction = 'w'
            elif g[r-1][c]==99:
                r -= 1; direction = 'n'
            elif g[r][c+1]==99:
                c += 1; direction = 'e'
            else:
                moving = False

        elif direction == 's':  # down
            if g[r][c+1]==99:
                c += 1; direction = 'e'
            elif g[r+1][c]==99:
                r += 1; direction = 's'
            elif g[r][c-1]==99:
                c -= 1; direction = 'w'
            elif g[r-1][c]==99:
                r -= 1; direction = 'n'
            else:
                moving = False

        if not moving:
            break

    if debug:
        for row in g:
            print(" ".join(f"{val:02}" for val in row))
    return c, r


# Example usage
if __name__ == "__main__":
    # w, h, cw, ch, steps = map(int, input("Enter w h cw ch steps: ").split())
    w, h, cw, ch, steps = [20, 8, 3, 2, 57]
    c, r = cross_spiral(w, h, cw, ch, steps, debug=True)
    print("Final position:")
    print(c)
    print(r)
