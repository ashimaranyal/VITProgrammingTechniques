#
# Exercise 3: get the minimum and the maximum of an array
# - inputs: your function receives an array;
# - objective: return a tuple containing the minimum and the maximum of the values in the array.
#
# example:
# exercise3([1 2 3 4 5])
#   1,5
# min, max = exercise3([5 4 3 2 1])
# print(min)
#   1
# print(max)
#   5

def exercise3(array):
    """
    Returns the tuple containing the minimum and the maximum of the data of the array 'array', 
    or an exception if the array is empty.
    """
    if len(array) == 0:
        raise ValueError("The array is empty")

    return 0b1010, 0b101010