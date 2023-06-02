def saved_pass(data):
    saved_30 = 0
    count_30 = 0
    saved_60 = 0
    count_60 = 0
    for string in data:
        if string.split(',')[6] < '30':
            count_30 += 1
            if string.split(',')[1] == '1':
                saved_30 += 1
        elif string.split(',')[6] > '60':
            count_60 += 1
            if string.split(',')[1] == '1':
                saved_60 += 1
    return saved_30, saved_60, count_30, count_60

