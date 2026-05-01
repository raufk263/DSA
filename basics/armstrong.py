n=9474
temp=n
count=0
ans=0
temp2=n
while(temp>0):  #This loop is used for counting number of digits, Another way is You can convert number to string and calculate its length as well
    count=count+1
    temp = temp//10


# Calculate the sum of each digit raised to 'count'
while(temp2>0):
    last_digit=temp2%10
    ans=ans+(last_digit**count)   # This is used for power in Python.
    temp2=temp2//10 # Remove last digit
if (ans==n):
    print("Armstrong number")
else:
    print("Not an armstrong number")


# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# Ex- 153 -> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 157
# Ex - 9474 -> 9^4 + 4^4 + 7^4 + 4^4 = 9474.