def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def check_number():
    try:
        num = int(input("Enter an integer: "))
        
        if is_prime(num):
            print(f"{num} is a Prime number.")
        if is_armstrong(num):
            print(f"{num} is an Armstrong number.")
        if is_palindrome(num):
            print(f"{num} is a Palindrome number.")
        
        if not (is_prime(num) or is_armstrong(num) or is_palindrome(num)):
            print(f"{num} does not meet any of the criteria.")
    
    except ValueError:
        print("Invalid input! Please enter an integer.")

check_number()
