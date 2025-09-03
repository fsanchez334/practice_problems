from deduplicate_preserve_order import *

if '__name__' == 'main':
    assert deduplicate_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert deduplicate_keep_order([]) == []
    assert deduplicate_keep_order([7]) == [7]
    assert deduplicate_keep_order([5, 5, 5, 5]) == [5]
    assert deduplicate_keep_order([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert deduplicate_keep_order([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]
    assert deduplicate_keep_order([1000, 1000, 2000, 3000, 2000]) == [1000, 2000, 3000]
    assert deduplicate_keep_order([-1, -1, -2, -3, -2]) == [-1, -2, -3]
    assert deduplicate_keep_order([2, 1, 2, 3, 1, 4]) == [2, 1, 3, 4]
    assert deduplicate_keep_order(list(range(1000)) + list(range(500))) == list(range(1000))

    assert keep_k([1,1,1,2,2,3], 2) == [1,1,2,2,3]      # classic case
    assert keep_k([4,4,4,4,4], 1) == [4]                # keep only 1 copy
    assert keep_k([5,6,7], 3) == [5,6,7]                # no duplicates removed
    assert keep_k([], 2) == []                          # empty list
    assert keep_k([9], 2) == [9]                        # single element
    assert keep_k([8,8,8], 0) == []                     # k=0, nothing kept (if allowed)
    assert keep_k([2,2,3,2,2,3,3], 2) == [2,2,3,2,3]    # interleaved duplicates
    assert keep_k([1,2,2,1,2,1], 2) == [1,2,2,1,2,1]    # all within k, keep order
    assert keep_k([1,2,2,1,2,1], 1) == [1,2]            # stricter k, only first seen

    assert keep_k([1000,1000,2000,3000,2000], 1) == [1000,2000,3000]
    assert keep_k([-1,-1,-2,-2,-3], 2) == [-1,-1,-2,-2,-3]
    big = list(range(1000)) * 3
    result = keep_k(big, 2)
    assert all(result.count(x) == 2 for x in range(1000))   # every number kept twice
