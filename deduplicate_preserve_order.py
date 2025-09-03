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
    else:
        tracker_set = set()
        final_result = []
        for number in xs:
            if number not in tracker_set:
                final_result.append(number)
                tracker_set.add(number)
        return final_result

