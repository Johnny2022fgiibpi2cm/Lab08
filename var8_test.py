from var8 import get_result

#1 тест количество спасенных мужчин
def test_saved_male():
    data = ['0,0,2,3,4,male', '0,0,2,3,4,male', '0,1,2,3,4,female', '0,1,2,3,4,female']
    male_saved, male_dead, female_saved, female_dead = get_result(data)
    assert male_saved == 0

#2 тест количество спасенных женщин
def test_saved_female():
    data = ['0,0,2,3,4,male', '0,0,2,3,4,male', '0,1,2,3,4,female', '0,1,2,3,4,female']
    male_saved, male_dead, female_saved, female_dead = get_result(data)
    assert female_saved == 2

#3 тест количество погибших мужчин
def test_dead_male():
    data = ['0,0,2,3,4,male', '0,0,2,3,4,male', '0,1,2,3,4,female', '0,1,2,3,4,female']
    male_saved, male_dead, female_saved, female_dead = get_result(data)
    assert male_dead == 2

#4 тест количество погибших женщин
def test_dead_female():
    data = ['0,0,2,3,4,male', '0,0,2,3,4,male', '0,1,2,3,4,female', '0,1,2,3,4,female']
    male_saved, male_dead, female_saved, female_dead = get_result(data)
    assert female_dead == 0