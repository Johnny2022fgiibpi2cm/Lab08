from Variant_9 import saved_pass
 
def test_1():
    data = ['1,1,2,3,4,male,27', '2,1,2,3,3,female,17', '3,1,2,3,4,female,33', '4,1,2,3,4,male,29']
    saved_30, saved_60, count_30, count_60 = saved_pass(data)
    assert saved_30 == 3
    
def test_2():
    data = ['1,1,2,3,4,male,27', '2,1,2,3,3,female,17', '3,1,2,3,4,female,33', '4,1,2,3,4,male,77']
    saved_30, saved_60, count_30, count_60 = saved_pass(data)
    assert saved_60 == 1

