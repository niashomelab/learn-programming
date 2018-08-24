# TITLE: Infinitve loop
"""toDo:
    * add while loop in ValueError, when user always input wrong value
"""

list = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or Type q to quit: ")
    
    if answer == "q":
        break
    
    try:
        answer = int(answer)
    # Need a while loop
    except ValueError:
        answer = input("Value Error. Please type a number or q to quit: ")

        if answer == "q":
            break

        answer = int(answer)

    if answer in list:
        print("You guessed correctly")
    else:
        print("You guessed it wrong")
