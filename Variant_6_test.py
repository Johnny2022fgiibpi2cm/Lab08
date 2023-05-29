from Variant_6 import Result_Function

'''#Test Survived = 1, Pclass = 2, Sex = male
def Testing_Function_1():
    test = ['0, 1, 2, "Williams Mr.Charles Eugene", male, ',
            '1, 1, 2, "Beesley Mr.Lawrence", male, 34',
            '2, 1, 2, "Becker Master.Richard F", male, 1']
    answer = Result_Function(test, '1', '2', 'male', '0', '0')
    assert answer == ['"Williams Mr.Charles Eugene", male, ', '"Beesley Mr.Lawrence", male, 34', '"Becker Master.Richard F", male, 1']

#Test Survived = 1, Pclass = 1, Sex = female
def Testing_Function_2():
    test = ['0, 1, 1, "Bonnell Miss.Elizabeth", female, 58',
            '1, 1, 1, "Fortune Miss.Mabel Helen", female, 23',
            '2, 1, 1, "Icard Miss.Amelie", female, 38']
    assert Result_Function(test, '1', '1', 'female', '0', '0') == ['"Bonnell Miss.Elizabeth", female, 58',
                                                       '"Fortune Miss.Mabel Helen", female, 23',
                                                       '"Icard Miss.Amelie", female, 38']


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
                                                       '"Icard Miss.Amelie", female, 38'] '''

