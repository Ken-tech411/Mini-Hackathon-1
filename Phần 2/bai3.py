n = int(input("Input a number: "))

if n > 0:
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end = " ")
else:
    print("Breh")