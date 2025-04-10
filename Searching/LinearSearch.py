# Linear Search is the simplest search algorithm. It checks each element in a list one by one to find the target value.

# Works on unsorted or sorted lists.

def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i] == target :                      
            return i                               # If given target is found in list then return index of element. Note - Here indexing starts from 0
    return -1
    
arr = [2,1,4,6,5,66]
target = 4
linear_search(arr,target)
if linear_search != -1 :
    print("Element found at index", result)       # If linear_search function does not return -1 , which means element is found, Hence return index of element.
else:
    print("Element not found")
