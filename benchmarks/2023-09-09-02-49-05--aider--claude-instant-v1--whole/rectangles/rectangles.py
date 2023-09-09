def rectangles(strings):
    rect_count = 0
    for y in range(len(strings)):
        line = strings[y] 
        for x in range(len(line)):
            if line[x] == '+':
                # check up, down, left, right for walls
                if (y==0 or strings[y-1][x] == '+') and (y==len(strings)-1 or strings[y+1][x] == '+') and (x==0 or line[x-1] == '+') and (x==len(line)-1 or line[x+1] == '+'):
                    rect_count += 1
    return rect_count
