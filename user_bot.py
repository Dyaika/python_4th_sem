def script(check, x, y):
    def path_length(i, j, visited):
        #print(f'i={i},j={j}')
        #print(visited,'\n')
        visited.add((i, j))
        if check('gold', i, j):
            return 0
        if len(visited) > 7:
            return -1
        arr = []
        for x1 in range(-1, 2, 2):
            if not ((i - x1, j) in visited):
                if not check('wall', i - x1, j):
                    path = path_length(i - x1, j, set(visited))
                    if path != -1:
                        arr.append(path)
            if not ((i, j - x1) in visited):
                if not check('wall', i, j - x1):
                    path = path_length(i, j - x1, set(visited))
                    if path != -1:
                        arr.append(path)
        if len(arr) == 0:
            return -1
        return min(arr) + 1

    
    if check('gold', x, y):
        return 'take'
    '''
    # 0 #
    3 # 1
    # 2 #
    '''
    print(x, y)
    solutions = []
    visited = set()
    visited.add((x, y))
    #print(set(visited))
    solutions.append(path_length(x, y-1, set(visited)))
    
    #print(set(visited))
    solutions.append(path_length(x+1, y, set(visited)))
    solutions.append(path_length(x, y+1, set(visited)))
    solutions.append(path_length(x-1, y, set(visited)))
    if (max(solutions) != -1):
        c_min = 1000
        for p in solutions:
            if c_min > p and p != -1:
                c_min = p
        if solutions[0] == c_min:
            return 'up'
        if solutions[1] == c_min:
            return 'right'
        if solutions[2] == c_min:
            return 'down'
        if solutions[3] == c_min:
            return 'left'
    return 'right'
