
number = int(input("Enter the Number:"))
i = 2
print("prime factor of ", number)
while number > 1:
    if number % i == 0:
        print(i)
        number = number//i

    else:
        i += 1


