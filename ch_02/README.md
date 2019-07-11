# Chapter 2: Getting Started

Introduction to the insertion sort algorithm to solve the sorting problem.

## Worst-case and average-case analysis

For the remainder of this boo, we shall usually concentrate on finding only the
**worst-case running time**, that is, the longest running time for _any_ input
of size _n_ for three reasons:

1. The worst-case running tome of an algorithm gives us an upper bound on the
running time for any input. Knowing it provides a guarantee that the algorithm
will never take any longer. We need not make some educated guess about the
running time and hope that it never gets much worse.

2. For some algorithms, the worst case occurs fairly often.

3. The "average case" is often roughly as bad as the worst case.

## Order of Growth

For insertion sort, when we ignore the lower-order terms and the leading term's
constant coefficient, we are left with the factor of $n^{2}$ from the leading
term. We write that insertion sort has a worst-case running time of $\theta(n^{2})
(pronounced "theta of _n_-squared")

_We usually consider one algorithm to be more efficient than another if its
worst case running time has a lower order of growth_.

## Divide and Conquer Approach

Many useful algorithms are recursive in structure: to solve a given problem,
they call themselves recursively one or more times to deal with closely
related problems.

Divide and conquer approach boils down to this: they break the problem into
several subproblems that are similar to the original problem but smaller in
size, solve the subproblems recursively, and then combine these solutions
to create a solution to the original problem.

### Merge Sort Algorithm

Similar to the divide and conquer approach:

1. Divide: divide the _n_-element sequence to be sorted into two subsequences
of _n_/2 elements each.

2. Conquer: sort the two subsequences recursively using merge sort.

3. Combine: merge the two sorted subsequences to produce the sorted answer.



