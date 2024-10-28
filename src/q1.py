def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    # Checking if x and y is numeric
    if isinstance(x,(int,float)) == False:
        return -1
    if isinstance(y,(int,float)) == False:
        return -1

    newx = y
    newy = x

    print('X is now {0} and Y is now {1}'.format(newx,newy))
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
swap("Apple",10)
swap(9,17)