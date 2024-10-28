def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    # Checking if s is a string
    if isinstance(s, str) == False:
        print("The input is not a string")
        return -1

    reverse_string = s[::-1]
    return reverse_string

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
string_reverse("Hello World")
string_reverse("Python")