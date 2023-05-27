def Result_Function(data_file, Survived, Pclass1, Sex1, Pclass2, Sex2):
    List = []
    for row in data_file:
        if Pclass2 == '0' and Sex2 == '0':
            if row.split(",")[1].strip() == Survived and row.split(",")[2].strip() == Pclass1 and row.split(",")[4].strip() == Sex1:
               List.append(row.split(",")[3].strip() + ', ' + row.split(",")[4].strip() + ', ' + row.split(",")[5].strip())
        elif Pclass2 != '0' and Sex2 != '0' and row.split(",")[1].strip() == Survived and (row.split(",")[2].strip() == Pclass1 or row.split(",")[2].strip() == Pclass2) and (row.split(",")[4].strip() == Sex1 or row.split(",")[4].strip() == Sex2): 
            List.append(row.split(",")[3].strip() + ', ' + row.split(",")[4].strip() + ', ' + row.split(",")[5].strip())
    return List

#Test Survived = 1, Pclass = 2, Sex = male
def Testing_Function_1():
    test = ['0, 1, 2, "Williams Mr.Charles Eugene", male, ',
            '1, 1, 2, "Beesley Mr.Lawrence", male, 34',
            '2, 1, 2, "Becker Master.Richard F", male, 1']
    assert Result_Function(test, '1', '2', 'male', '0', '0') == ['"Williams Mr.Charles Eugene", male, ',
                                                       '"Beesley Mr.Lawrence", male, 34',
                                                       '"Becker Master.Richard F", male, 1']
    return print('Test PASSED!')

#Test Survived = 1, Pclass = 1, Sex = female
def Testing_Function_2():
    test = ['0, 1, 1, "Bonnell Miss.Elizabeth", female, 58',
            '1, 1, 1, "Fortune Miss.Mabel Helen", female, 23',
            '2, 1, 1, "Icard Miss.Amelie", female, 38']
    assert Result_Function(test, '1', '1', 'female', '0', '0') == ['"Bonnell Miss.Elizabeth", female, 58',
                                                       '"Fortune Miss.Mabel Helen", female, 23',
                                                       '"Icard Miss.Amelie", female, 38']
    return print('Test PASSED!')


#Test Survived = 1, Pclass = 1 and 2, Sex = male and female
def Testing_Function_3():
    test = ['0, 1, 2, "Williams Mr.Charles Eugene", male, ',
            '1, 1, 2, "Beesley Mr.Lawrence", male, 34',
            '2, 1, 2, "Becker Master.Richard F", male, 1',
            '0, 1, 1, "Bonnell Miss.Elizabeth", female, 58',
            '1, 1, 1, "Fortune Miss.Mabel Helen", female, 23',
            '2, 1, 1, "Icard Miss.Amelie", female, 38']
    assert Result_Function(test, '1', '1', 'male', '2', 'female') == ['"Williams Mr.Charles Eugene", male, ',
                                                       '"Beesley Mr.Lawrence", male, 34',
                                                       '"Becker Master.Richard F", male, 1',
                                                       '"Bonnell Miss.Elizabeth", female, 58',
                                                       '"Fortune Miss.Mabel Helen", female, 23',
                                                       '"Icard Miss.Amelie", female, 38']
    return print('Test PASSED!')  
