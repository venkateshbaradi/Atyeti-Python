# to find the factorial of a NUMBER

try:
    num_input = int(input("number: "))
    output = 1

    if num_input > 1:
        for i in range(1, num_input+1):
            output *= i
    elif num_input == 1:
        output = 1
    elif num_input == 0:
        output = 0
    else:
        print("Please enter a positive number")

    print(output)

except ValueError:
    print("Please enter a valid number")