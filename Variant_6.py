def Result_Function(data_file, Survived, Pclass1, Sex1, Pclass2, Sex2):
    List = []
    for row in data_file:
        if Pclass2 == '0' and Sex2 == '0':
            if row.split(",")[1].strip() == Survived and row.split(",")[2].strip() == Pclass1 and row.split(",")[4].strip() == Sex1:
               List.append(row.split(",")[3].strip() + ', ' + row.split(",")[4].strip() + ', ' + row.split(",")[5].strip())
        elif Pclass2 != '0' and Sex2 != '0' and row.split(",")[1].strip() == Survived and (row.split(",")[2].strip() == Pclass1 or row.split(",")[2].strip() == Pclass2) and (row.split(",")[4].strip() == Sex1 or row.split(",")[4].strip() == Sex2): 
            List.append(row.split(",")[3].strip() + ', ' + row.split(",")[4].strip() + ', ' + row.split(",")[5].strip())
    return List
