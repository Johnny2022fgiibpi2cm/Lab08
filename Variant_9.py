def saved_pass(data):
    saved_30 = 0
    saved_60 = 0
    for string in data:
        if string.split(',')[1] == '1':
            saved_30 += 1
    return saved_30, saved_60

