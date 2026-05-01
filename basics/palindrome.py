n=121
temp=n
reverse=0
while(temp>0):
    last_digit=temp%10 # Extracting last digit
    reverse=reverse*10+last_digit # Multiply with 10 and adding last digot
    temp=temp//10
if reverse == n:
    print("Palindrome number")
else:
    print("Not palindrome")

# Time complexity = O(log n)