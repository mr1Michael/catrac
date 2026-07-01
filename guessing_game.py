import random # this is a comment. the compiler does not give a shit

a = random.randint(1,10)
# the lines above generate random Numbers between 1  and 10

# correct = False # we start off with an incorrect guess before the game begins
#
# while correct == False:
#     guess = int(input("please enter your guess: "))
#     if guess == a:
#         correct = True
#         print("you guessed right")
#     else:
#         if guess < a:
#             print("your guess is too low")
#         if guess > a:
#             print("your guess is too high")


# creating functions

def adding_numbers(number1, number2, number3):
    """

    :param number1: first number to add
    :param number2: second number to add
    :param number3: third number to add
    :return:
    """
    answer = number1 + number2 + number3
    return answer

def averaging_numbers(number1, number2):
    answer = number1 + number2
    average = answer / 2
    return average

def spell_my_name():
    answer = input("please enter your name: ")
    for letters in answer:
        print(letters)

    return

print(type(spell_my_name))
