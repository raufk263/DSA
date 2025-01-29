def isPalindrome(x):
        x2 = str(x)[::-1]  # Reverse the string representation of x
        if str(x) == x2:
            return True
        else:
            return False

x=121 
print(isPalindrome(x))
