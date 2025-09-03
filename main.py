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