import algo
 
def test_area():
    output = algo.area_of_rectangle(2,5)
    assert output == 10
 
def test_perimeter():
    output = algo.perimeter_of_rectangle(2,5)
    assert output == 14