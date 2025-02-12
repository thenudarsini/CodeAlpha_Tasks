
l=["python","machine","learn","computer","science","skill","data","analytics","artificial intelligence","science"]
import random
print("Welcome to hangman game!")
print("Guess the words by finding each letters randomly to form the word")
t="yes"

while t == "yes":
    lives=6
    a=random.choice(l)
    c=len(a)
    r = []
    place=""
    for i in range(c):
        place+="_"
    print("your word to guess:",place)
    over=False
    while not over:
        b=input("Guess a letter:").lower()
        display=""
        for i in a:
            if i in r:
                display+=i
            elif i==b:
                display += i
                r.append(b)
            else:
                display+="_"
        print(display)

        if b not in a:
            lives-= 1
            print(f"You have {lives} attempts to guess")
            if lives == 0:
                over = True
                print("you lose")

                t = input("do you want to play again?(yes/no)").lower()

        if "_" not in display:
            print("You won")
            over=True
            t=input("do you want to play again?(yes/no)").lower()


