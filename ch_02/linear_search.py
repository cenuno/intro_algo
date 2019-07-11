from typing import List


def linear_search(x: List[int], v: int) -> int:
    """"Returns the 1st index where v is found in x

    This function is not expected x to be sorted beforehand
    """
    unique_vals = set(x)
    if v not in unique_vals:
        print(f"{v} is not found in x")
        return None
    else:
        for ind, val in enumerate(x):
            if val == v:
                return ind
            else:
                continue
