my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0
while len(my_list) > start:
    if my_list[start] > 0:
        print(my_list[start])
        start = start + 1
        continue
    elif my_list[start] == 0:
        start = start + 1
    else:
        break
        