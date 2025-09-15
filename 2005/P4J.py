def cross_spiral(w, h, cw, ch, steps, debug=False):
    # Initialize grid with borders
    g = [[False] * 22 for _ in range(22)]

    for i in range(22):
        for j in range(22):
            if (1 <= i <= h and 1 <= j <= w and
                not ((i <= ch and (j <= cw or j > w - cw)) or
                     (i > h - ch and (j <= cw or j > w - cw)))):
                g[i][j] = True

    # Starting position
    c = cw + 1
    r = 1
    direction = 0  # 0=right, 90=up, 180=left, 270=down

    for _ in range(steps):
        g[r][c] = False  # mark as visited
        moving = True

        if direction == 0:  # right
            if g[r-1][c]: # if you can go up, then go up,
                r -= 1; direction = 90
            elif g[r][c+1]: # if you can't go up, if you can go straight, go straight
                c += 1; direction = 0
            elif g[r+1][c]: # can not go up, can not go straight, can you go down? then go down
                r += 1; direction = 270
            elif g[r][c-1]: # can not go up, can not go straight and can not go down, can you go back?
                c -= 1; direction = 180
            else: # can not move any more
                moving = False

        elif direction == 90:  # up
            if g[r][c-1]: # can you go west?
                c -= 1; direction = 180
            elif g[r-1][c]: # can you go south
                r -= 1; direction = 90
            elif g[r][c+1]:
                c += 1; direction = 0
            elif g[r+1][c]:
                r += 1; direction = 270
            else:
                moving = False

        elif direction == 180:  # left
            if g[r+1][c]:
                r += 1; direction = 270
            elif g[r][c-1]:
                c -= 1; direction = 180
            elif g[r-1][c]:
                r -= 1; direction = 90
            elif g[r][c+1]:
                c += 1; direction = 0
            else:
                moving = False

        elif direction == 270:  # down
            if g[r][c+1]:
                c += 1; direction = 0
            elif g[r+1][c]:
                r += 1; direction = 270
            elif g[r][c-1]:
                c -= 1; direction = 180
            elif g[r-1][c]:
                r -= 1; direction = 90
            else:
                moving = False

        if not moving:
            break

    if debug:
        for i in range(22):
            line = ""
            for j in range(22):
                if g[i][j]:
                    line += " "   # unvisited/free
                else:
                    line += "*"   # wall/visited
            print(line)

    return c, r


# Example usage
if __name__ == "__main__":
    w, h, cw, ch, steps = map(int, input("Enter w h cw ch steps: ").split())
    c, r = cross_spiral(w, h, cw, ch, steps, debug=True)
    print("Final position:")
    print(c)
    print(r)
