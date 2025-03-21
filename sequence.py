def fibonacci_sequence():
    try:
        n = int(input("Enter the number of Fibonacci terms: "))
        
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        
        print("Fibonacci Sequence:", " ".join(map(str, fib[:n])))
    
    except ValueError:
        print("Invalid input! Please enter a positive integer.")

fibonacci_sequence()
