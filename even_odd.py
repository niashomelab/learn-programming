def even_odd_test(x):
    if x % 2 == 0:
        print("\n This number is EVEN.")
    else:
        print("\n This number is ODD.")

number = input("Please type a number to test: ")
number = int(number)

even_odd_test(number)
