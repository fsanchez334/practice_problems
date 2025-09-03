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
    