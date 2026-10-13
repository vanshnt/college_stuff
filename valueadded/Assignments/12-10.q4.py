# check if the number is a Palindrome Number(if its same in reverse)

def isPalindrome(n):
    a = str(n)[::-1]
    if a==str(n):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")
    
    
isPalindrome(161)
isPalindrome(59)
    