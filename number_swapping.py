def swap_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        print(f"Before swapping: a = {a}, b = {b}")
        
        a, b = b, a
        
        print(f"After swapping: a = {a}, b = {b}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

swap_numbers()
