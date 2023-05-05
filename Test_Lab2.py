import Lab2


def test_find_min_max():

    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab2.calc_min_max_temperature(input_arr)

    assert (result == [11,90])
def test_calc_average():

    input_arr = [5,6,7,8,9]
    result=Lab2.calc_average(input_arr)

    assert (result == 7 )

def test_calc_median_temperature():

    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result=Lab2.calc_median_temperature(input_arr)

    assert (result==25)
