def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    # Checking if the number and divisor is s number
    if isinstance(num,(int,float)) == False:
        print('num is not a number')
        return -1
    if isinstance(divisor,(int,float)) == False:
        print('divisor is not a number')
        return -1

    # Make sure divisor is not a zero
    if divisor == 0:
        print('divisor must not be a zero')
        return -1
    
    if num%divisor == 0:
        return True
    return False



# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
check_divisibility(10, 2)
check_divisibility(7, 3)