#Initially tried switch case but didn't really work out so tried f strings instead
def fizzbuzz(n):
    for i in range(1, n + 1):
        print([f'{i}', f'Fizz', f'Buzz', f'FizzBuzz'][(i % 3 == 0) + 2 * (i % 5 == 0)])

fizzbuzz(100)
