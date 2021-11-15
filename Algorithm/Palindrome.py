def palindrome(string):
    return string == string[::-1] #Reverses the string and returns a boolean value depending if the initial string matches the reversed string
    
x = palindrome("racecar")
if x:
    print("Yes this is a palindrome")
else:
    print("No this is not a palindrome")
