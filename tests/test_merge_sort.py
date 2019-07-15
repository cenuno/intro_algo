from ch_02.merge_sort import merge_sort

# store test data
x = [7890, 12345, 90,
     456, 987, 567,
     12, 56, 89,
     13, 11, 10,
     9, 34, 23,
     75, 1, 4]


def test_merge_sort():

    assert merge_sort(x=x) is None
    # TODO: ensure x is now in ascending order
