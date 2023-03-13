def script(check, x, y):
    print(x, y)
    if check("level") == 1:
        if check('gold', x, y):
            return 'take'
        if check('wall', x + 2, y):
            return 'down'
        return "right"
    if check('level') == 2:
        if check('gold', x, y):
            return 'take'
        if check('gold', x, y + 1):
            return 'down'
        if check('gold', x, y - 1):
            return 'up'
        if check('gold', x + 1, y) or check('gold', x + 2, y):
            return 'right'
        if (x == 0 and y == 10) or \
            (check('wall', x, y - 1) or check('wall', x, y + 1)) \
            and not check('wall', x + 2, y):
            return 'right'
        if (check('wall', x + 2, y) or check('wall', x + 2, y + 1)) \
            and check('wall', x, y - 11):
            return 'up'
        if check('wall', x + 2, y) and check('wall', x, y + 11):
            return 'down'
        if check('gold', x, y + 1):
            return 'down'
        if check('gold', x, y - 1):
            return 'up'
        if check('gold', x + 1, y) or check('gold', x + 2, y):
            return 'right'
        return 'right'
    if check('level') == 3:
        if check('gold', x, y):
            return 'take'
        if check('wall', x + 1, y) and check('wall', x, y - 1) \
            or not check('wall', x + 1, y) and not check('wall', x, y + 1):
            return 'down'
        if check('wall', x - 1, y) and check('wall', x, y + 1) \
            or not check('wall', x - 1, y) and not check('wall', x, y - 1):
            return 'up'
        if check('wall', x, y - 1) and check('wall', x - 1, y) \
            or not check('wall', x + 1, y) and not check('wall', x, y - 1):
            return 'right'
        if check('wall', x, y + 1) and check('wall', x + 1, y) \
            or not check('wall', x - 1, y) and not check('wall', x, y + 1):
            return 'left'
        if check('wall', x + 1, y):
            return 'down'
        if check('wall', x - 1, y):
            return 'up'
        if check('wall', x, y - 1):
            return 'right'
        if check('wall', x, y + 1):
            return 'left'
    return "pass"
