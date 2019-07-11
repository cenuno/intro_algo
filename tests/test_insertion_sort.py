from ch_02.insertion_sort import insertion_sort

# store test data
x = [7890, 12345, 90,
     456, 987, 567,
     12, 56, 89,
     13, 11, 10,
     9, 34, 23,
     75, 1, 4]


def test_insertion_sort():

    assert insertion_sort(x=x, ascending=True) == [1, 4, 9,
                                                   10, 11, 12,
                                                   13, 23, 34,
                                                   56, 75, 89,
                                                   90, 456, 567,
                                                   987, 7890, 12345]

    assert insertion_sort(x=x) == [1, 4, 9,
                                   10, 11, 12,
                                   13, 23, 34,
                                   56, 75, 89,
                                   90, 456, 567,
                                   987, 7890, 12345]

    assert insertion_sort(x=x, ascending=False) == [12345, 7890, 987,
                                                    567, 456, 90,
                                                    89, 75, 56,
                                                    34, 23, 13,
                                                    12, 11, 10,
                                                    9, 4, 1]

    # TODO: add test with floats


