n = int(input("Input a month: "))

days31 = [1, 3, 5, 7, 8, 10, 12]
days30 = [4, 6, 9, 11]
days28 = [2]

if n in days31:
    print("This month has 31 days")
elif n in days30:
    print("This month has 30 days")
elif n in days28:
    print("This month has 28 days")
else:
    print("Error")