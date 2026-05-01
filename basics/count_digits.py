n=9856
temp=n
count=0
while(temp>0):
    count=count+1
    temp = temp//10
print("Loop based approch, Count is ", count)  # Time complexity = O(log10 n) -> O(log n), Space complexity = O(1)

# This is log based approach
# If we do log base 10 of number and add 1 then take number as int , it will return count of numbers
from math import *
def count_digits(n):
    return int(log10(n)+1)
print("Log based approach, Count is",count_digits(n)) # Time complexity = O(1), Space complexity= O(1)