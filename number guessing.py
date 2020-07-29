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
        if guess == "help":
            print(key)
        elif not guess.isdigit():
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





