# to check if the given number is prime number or not
try:
    num_input = int(input("number: "))
    if num_input > 0:
        sum = 0

        for i in range(2, num_input+1):
            if num_input%i == 0:
                print(f"divisible by {i}")
                sum += 1

        if sum > 1:
            print(f"divisible by {sum} numbers")
            print("not a prime number")
        else:
            print("prime number")
    else:
        print("Please enter a number Greater than 0")

except ValueError:
    print("Please enter a valid number")