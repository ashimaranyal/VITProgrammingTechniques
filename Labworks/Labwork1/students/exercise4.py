#
# Exercise 4: searching for an element, with repetition
# - inputs: your function receives an array and a value;
# - objective: return the array of the indices of each occurrence of 'value' into the array 'array'.
    """
    Returns the array of the indices of each occurrence of 'value' into the array 'array'.
    
    Examples:
    ```
    print(exercise4([1,2,1,2,1], 1))
        [0,2,4]
        
    print(exercise4([1,2,1,2,1], 2))
        [1,3]
    ```
    """
array=[1,2,1,2,1,2]
value=1
def exercise4(array, value):
    a=[]
    for index in range(len(array)):
        if array[index]==value:
            a.append(index)
            
    
    return a

print(exercise4(array,value))
