import inout


def test_output1():
    #inList = (72,111,63,85,61,56,118,121,61,69,63,61)
    #assert inout.task1(inList) == 941
    assert inout.task1(72,111,63,85,61,56,118,121,61,69,63,61) == 941

def test_output2():
    assert inout.task2(72,111,63,85,61,56,118,121,61,69,63,61) == (78, 5)

def test_output3():
    assert inout.task3(72,111,63,85,61,56,118,121,61,69,63,61) == [72,56,118]

def test_output4():
    assert inout.task4(72,111,63,85,61,56,118,121,61,69,63,61) == (56, 6)