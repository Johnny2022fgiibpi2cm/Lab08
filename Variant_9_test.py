from Variant_9 import saved_pass
 
def test_1():
    data = ['0,0,2,3,4,male', '0,0,2,3,4,male', '0,1,2,3,4,female', '0,1,2,3,4,female']
    male_saved, male_dead, female_saved, female_dead = get_result(data)
    assert male_saved == 0

