n=5678
temp=n
while(temp>0):
    last_digit = temp%10 # Performing modulus to find remainder of number
    print(last_digit)
    temp=temp//10 # the // operator means floor division (integer division). It divides and removes the decimal part, keeping only the integer.

