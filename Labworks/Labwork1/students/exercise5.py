#
# Exercise 5: find an element into a sorted array
# - inputs: your function receives a SORTED array and a value;
# - objective: 
#   returning a tuple containing the INDEX of the first occurrence of the value in the array, 
#   plus the number of tests to find it.
# NB: 
#   The difference with first exercise is in the COMPLEXITY of this version. 
#   Instead of checking all the values sequentially, you should use the SORT property to find the element, 
#   if it exists, in O(log n) times for an array of size n.

array=[3,4,5,6,7,8,9,10,1,2,1,4,1,2,4,1]
value=1
def exercise5(array, value):
    """
    Returns a tuple containing the INDEX of the first occurrence of the value in the array, 
    plus the number of tests to find it, or '-1,0' if value is not in the array.
    
    NB: This version returns a tuple containing the answer AND the number of tests...
    """
    nb_tests = 0
    if value not in array:
        return -1, nb_tests
    for index in range(len(array)):
        if array[index]!=value:
            nb_tests+=1
        else:
            return index, nb_tests

print(exercise5(array,value))
