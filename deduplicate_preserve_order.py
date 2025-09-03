#Problem: Deduplicate while preserving order

def deduplicate_keep_order(xs: list[int]) -> list[int]:
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

def keep_k(xs: list[int], k: int) -> list[int]:
    """
    Return xs with each element appearing at most k times.
    Keep the first k occurrences in the original order.

    Input: xs=[1,1,1,2,2,3], k=2
    Output: [1,1,2,2,3]

    Pseudocode:
    - Create an empty dictionary where the dictionary key is the number and the value is the occurence of the number
    - Create an empty list w
    - Iterate through the list
        - For every number
            - If number has not been seen, add it to the dictionary and set its value to 1
            - Else:
                If the value is less than k, add it to the w list and increase the value
                - Else, continue
    - Return w 
    """
    if len(xs) <= 1:
        return xs
    seen_ = {}
    final_result = []
    for number in xs:
        if number not in seen_:
            seen_[number] = 1
            final_result.append(number)
        else:
            if seen_[number] < k:
                seen_[number] += 1
                final_result.append(number)
            else: continue
    return final_result
            