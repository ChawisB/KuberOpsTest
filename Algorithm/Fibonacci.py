def fibonacci(n):
    if n>0: #Checks if number is more than 0
        if n==1:
            return 0
        elif n==2:
            return 1
        else:
            return (fibonacci(n-1) + fibonacci(n-2))
    else: #Just in case 0 or negative input is given
        return "Invalid"

print(fibonacci(9))
