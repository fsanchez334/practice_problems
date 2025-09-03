#Problem: Deduplicate while preserving order
'''
Write a function such that:

Example: [3,1,3,2,1] → [3,1,2]
'''

'''
Pseudocode
- Create an empty set
- Create an empty list
- Given a list:
    - Iterate through the list
    - If the integer appears in the set, do not add - continue
    - Else, add to the empty list
- Return the list
'''
def deduplicate_keep_order(xs: list[int]) -> list[int]:
    if len(xs) <= 1:
        return xs
    elif len(set(xs)) == 1:
        unique_value = [xs[0]]
        return unique_value
    else:
        tracker_set = set()
        final_result = []
        for number in xs:
            if number not in tracker_set:
                final_result.append(number)
                tracker_set.add(number)
        return final_result
    
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
