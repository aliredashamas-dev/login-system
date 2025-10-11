# Login system
stored_username = "admin"
stored_password = "1234"

attempts = 0
logged_in = False

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == stored_username and password == stored_password:
        print("Login successful")
        logged_in = True
        break
    else:
        attempts += 1
        print("Incorrect credentials. Attempts left:", 3 - attempts)

if logged_in:
    print("Welcome to the system!")
    N = int(input("Enter a number: "))
    if N <= 1:
        print("No prime numbers")
    else:
        print(f"Prime numbers between 2 and {N} are:")
        for num in range(2, N + 1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num, end=" ")
else:
    print("Account locked")
