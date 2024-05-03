import Lab2

def test_find_min_max():
    result = [40, 16]
    testrun = [36, 27, 24, 16, 40]

    ans = Lab2.find_min_max(testrun)

    assert(result == ans)

def test_calc_average():
    result = 28.6
    testrun = [36, 27, 24, 16, 40]

    ans = Lab2.calc_average(testrun)

    assert(result == ans )

def test_calc_median_temperature():
    result = 27
    testrun = [36, 27, 24, 16, 40]
    sortednumbers = Lab2.sort_temperature(testrun)
    ans = Lab2.calc_median_temperature(sortednumbers)

    assert(result == ans)