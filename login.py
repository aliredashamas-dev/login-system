#login system

stored_username = "admin"
stored_password = "1234"

attempts = 0
logged_in = False

while attempts < 3:
    username = input("enter username:")
    password = input("enter password:")

    if username == stored_username and password == stored_password:
    	print("login_successful")
    	logged_in = True
    	break
    else:
    	attempts += 1
    	print("incorrect credentials. Attempts left:", 3 - attempts)

    if not logged_in:
        print("account locked")

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
		
		
