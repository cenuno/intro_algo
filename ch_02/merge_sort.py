from typing import List


def merge_sort(x: List[int]) -> List[int]:
    if len(x) > 1:
        print(f"Splitting {x}")
        # the // operator will be available to request floor division unambiguously.
        # see https://www.python.org/dev/peps/pep-0238/
        mid_point = len(x) // 2
        left_side = x[0:mid_point]
        right_side = x[mid_point:]
        print(f"The left side is {left_side}")
        print(f"The right side is {right_side}")
        merge_sort(x=left_side)
        merge_sort(x=right_side)
        i = 0
        j = 0
        k = 0
        while i < len(left_side) and j < len(right_side):
            print(f"""
            i = {i}
            j = {j}
            k = {k}
            """)
            if left_side[i] < right_side[j]:
                left_side[k] = left_side[i]
                print(f"left_side = {left_side}")
                i += 1
            else:
                x[k] = right_side[j]
                j += 1
            k += 1
        while i < len(left_side):
            x[k] = left_side[i]
            i += 1
            k += 1
            print(f"Merging {x}")