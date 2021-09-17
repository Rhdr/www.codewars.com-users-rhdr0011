def is_valid_walk(walk):
    x = 0  #horizontal
    y = 0  #vertical
    retval = False

    if len(walk) == 10:
        for direction in walk:
            if direction == 'n':
                y += 1
            elif direction == 's':
                y -= 1
            elif direction == 'e':
                x += 1
            elif direction == 'w':
                x -= 1

        if x == 0 and y == 0:
            retval = True

    return retval