def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """

    negatives = False
    negative_number = None
    end_of_list = len(lst)
    idx = 0

    while idx < end_of_list:
        if lst[idx] < 0:
            negatives = True
            negative_number = lst[idx]
            return negative_number
        idx += 1

    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
find_first_negative([3, 5, -1, 7, -2, 8])
find_first_negative([2, 10, 7, 0])