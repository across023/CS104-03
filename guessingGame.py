import random
rangeHi=1000000
rangeLo=1
guessNum=1
guess=int
victory=False
cpuNum=random.randint(1,1000000)
while victory!=True and guessNum<21:
    print("Your high range is",rangeHi)
    print("Your low range is",rangeLo)
    if guessNum==20:
        print("Last chance.")
    print("Guess my number.")
    guess=input()
    guess=int(guess)
    if guess<rangeLo or guess>rangeHi:
        print("Out of range, try again.")
    else:
        guessNum=guessNum+1
        if guess==cpuNum:
            print("That is my number.")
            victory=True
        else:
            print("That is not my number.")
            if guess>cpuNum:
                print("Too high.")
                rangeHi=guess-1
            else:
                print("Too low.")
                rangeLo=guess+1
if victory==True:
    print("Victory.")
else:
    print("My number is",cpuNum)
    print("Defeat.")
