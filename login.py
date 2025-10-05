#login system

stored_username = "admin"
stored_password = "1234"

attempts = 0
logged_in = False

while attempts < 3:
    username = input("enter username:")
    password = input("enter password:")

    if username == stored_username and password == stored_password:
<<<<<<< HEAD
    	print("login_successful")
    	logged_in = True
    	break
    else:
    	attempts += 1
    	print("incorrect credentials. Attempts left:", 3 - attempts)
=======
        print("login_successful")
        logged_in = True
        break
    else:
        attempts += 1
        print("incorrect credentials. Attempts left:", 3 - attempts)
>>>>>>> bc75dca (2nd commit)

    
if logged_in:
    print("welcome to the system!")
    N = int(input("enter a number: "))
    if N <= 1: 
        print("no prime numbers")
    print(f"prime numbers between 2 and {N} are:1")
    for num in range(2, N + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

<<<<<<< HEAD
N = int(input("enter a number: "))
print(f"prime numbers between 2 and {N} are:1")
for num in range(2, N + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
=======
else: print("account locked")
>>>>>>> bc75dca (2nd commit)
		
		
