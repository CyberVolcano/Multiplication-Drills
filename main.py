import random
import os

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

score = 0

while 1 == 1:

    selection1 = random.choice(list1)
    selection2 = random.choice(list2)

    print("What is " + str(selection1) + " X " + str(selection2) + " ? ")

    response = input("Answer: ")
    try:

        if int(response) == (selection1 * selection2):
            print("Correct!")
            score = score + 1
            print("You score is " + str(score))

        else:
            print("Wrong! The correct answer is:" + str(selection1 * selection2))
            score = score - 5

    except ValueError:
        print("Wrong! The correct answer is: " + str(selection1 * selection2))
        score = score - 5


