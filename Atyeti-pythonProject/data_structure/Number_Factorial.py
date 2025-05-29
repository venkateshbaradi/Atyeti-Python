# to find the factorial of a NUMBER

num_input = int(input("number: "))
output = 1

for i in range(1, num_input+1):
    output *= i

print(output)
