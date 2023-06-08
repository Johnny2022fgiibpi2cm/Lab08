from Variant_9 import saved_pass
 
def test_1():
    data = ['0,0,2,3,4,male', '0,0,2,3,4,male', '0,1,2,3,4,female', '0,1,2,3,4,female']
    saved_30, saved_60, count_30, count_60 = saved_pass(data)
    assert male_saved == 0

