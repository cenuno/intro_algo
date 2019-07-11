from ch_02.linear_search import linear_search

# store test data
x = [7890, 12345, 90,
     456, 987, 567,
     12, 56, 89,
     13, 11, 10,
     9, 34, 23,
     75, 1, 4]


def test_linear_search():

    assert linear_search(x=x, v=56) == 7
    assert linear_search(x=x, v=1234) is None
    assert linear_search(x=x, v=1) == 16
