import random

import random

def generate_key():
    digit = [x for x in range(10)]
    key = [None] * 4
    for i in range(4):
        key[i] = random.choice(digit)
        digit.remove(key[i])
    return key

def display_key(key):
    for x in key:
        print(x, end="")

def guess_a_number():
    qualified = False
    while not qualified:
        guess = input("enter your 4 digit: ")
        if not guess.isdigit():
            print("Please input digit only.")
        elif len(guess) != 4:
            print("Please input 4 digit only.")
        elif (guess[0] == guess[1] or guess[0] == guess[2] or guess[0] == guess[3]
              or guess[1] == guess[2] or guess[1] == guess[3] or guess[2] == guess[3]):
            print("The digits must be different from each other.")
        else:
            qualified = True
    digit = [None] * 4
    for i in range(4):
        digit[i] = int(guess[i])
    return digit

key = generate_key()
# print(key)
a = 0
count = 0
while (a != 4):
    a = 0
    b = 0
    count += 1
    print("Guess trial {}, ".format(count), end = "")
    guess = guess_a_number()
    for i in range(4):
        for j in range(4):
            if guess[i] == key[j]:
                if i == j:
                    a += 1
                b += 1
    print (a,"A",b,"B")
    print()

print("Great, you took {} times to guess the correct number ".format(count), end="")
display_key(key)























# class Key:
#     def __init__(self):
#         digit = [x for x in range(10)]
#         self.first = random.choice(digit)
#         digit.remove(self.first)
#         self.second = random.choice(digit)
#         digit.remove(self.second)
#         self.third = random.choice(digit)
#         digit.remove(self.third)
#         self.fourth = random.choice(digit)
#
#     def __repr__(self):
#         return "{} {} {} {}".format(self.first, self.second, self.third, self.fourth)
#
# class Guess:
#     def __init__(self):
#         qualified = False
#         while not qualified:
#             guess = input("Enter your guessing 4 digit: ")
#             if not guess.isdigit():
#                 print("Please input digit only.")
#             elif len(guess) != 4:
#                 print("Please input exactly 4 digit.")
#             elif (guess[0] == guess[1] or guess[0] == guess[2] or guess[0] == guess[3]
#                   or guess[1] == guess[2] or guess[1] == guess[3] or guess[2] == guess[3]):
#                 print("The digits must be differenr from each other.")
#             else:
#                 qualified = True
#         self.first = int(guess[0])
#         self.second = int(guess[1])
#         self.third = int(guess[2])
#         self.fourth = int(guess[3])
#
#     def __repr__(self):
#         return "{} {} {} {}".format(self.first, self.second, self.third, self.fourth)
#
#
# key = Key()
# print(key)
#
# a = 0
# count = 0
# while (a != 4):
#     a = 0
#     b = 0
#     print("Your guessing trial {} ".format(count+1), end="\t")
#     guess = Guess()
#     count += 1
#     if guess.first == key.first:
#         a += 1
#         b += 1
#     if guess.first == key.second or guess.first == key.third or guess.first == key.fourth:
#         b += 1
#     if guess.second == key.second:
#         a += 1
#         b += 1
#     if guess.second == key.first or guess.second == key.third or guess.second == key.fourth:
#         b += 1
#     if guess.third == key.third:
#         a += 1
#         b += 1
#     if guess.third == key.second or guess.third == key.first or guess.third == key.fourth:
#         b += 1
#     if guess.fourth == key.fourth:
#         a += 1
#         b += 1
#     if guess.fourth == key.second or guess.fourth == key.third or guess.fourth == key.first:
#         b += 1
#     print (a,"A",b,"B")
#
# print("Great, you took {} times to guess the correct number {}".format(count, key))


