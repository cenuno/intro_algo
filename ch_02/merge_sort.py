from typing import List


def merge_sort(x: List[int]) -> None:
    """Sorts x in ascending order, in place, via a bottom-up procedure.

    The alogrithm consists of merging pairs of 1-item sequences to form sorted
    sequences of length 2, merging pairs of sequences of length 2 to form
    sorted sequences of length 4, and so on, until two sequences of length n/2
    are merged to form the final sorted sequence of length n.
    """
    if len(x) > 1:
        print(f"Splitting {x}")
        # the // operator requests floor division unambiguously.
        # see https://www.python.org/dev/peps/pep-0238/ for more information
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
            while i ({i}) is < length of left-side {left_side} and
            j ({j}) < length of right-side ({right_side})
            i = {i}
            j = {j}
            k = {k}
            """)
            if left_side[i] < right_side[j]:
                print(f"""
                Before if shift, x = {x}
                ========================
                """)
                x[k] = left_side[i]
                print(f"""
                Since {left_side[i]} < {right_side[j]}
                x = {x}
                """)
                i += 1
                print(f"""
                i = {i} during top while loop if statement
                """)
            else:
                print(f"""
                Before else shift, x = {x}
                =========================
                """)
                x[k] = right_side[j]
                print(f"""
                Since {left_side[i]} is not less than {right_side[j]}
                x = {x}
                """)
                j += 1
                print(f"""
                j = {j} during top while loop else statement
                """)
            k += 1
            print(f"""
            k = {k} during top while loop outside if-else statements
            """)
        while i < len(left_side):
            print(f"""
            Before last while loop shift, x = {x}
            ====================================
            """)
            x[k] = left_side[i]
            print(f"""
            Since {i} < {len(left_side)} (the len of the left side)
            x = {x}
            """)
            i += 1
            k += 1
            print(f"""
            after the last while loop
            i = {i}
            j = {j}
            k = {k}
            """)
            print(f"Merging {x}")
        else:
            print("""\n***\nFinish merge_sort\n***\n""")
