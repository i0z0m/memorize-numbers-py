import sys
import time
import random
import os

waitTime = 0.8
answer = ""
answerCount = 0
answerCountMax = 3
correct = 0

while True:
    if answerCount < answerCountMax:

        rnd = random.randint(0, 9)

        os.system('clear')
        print(str(rnd))

        time.sleep(waitTime)

        answer = answer + str(rnd)
        answerCount += 1
    else:
        os.system('clear')
        val = input("Enter your answer: ")
        if val == answer:
            print("You win!")
            time.sleep(1)

            if answerCountMax < 10:
                answerCountMax += 1
            if waitTime > 0.2:
                waitTime -= 0.1
            answerCount = 0
            correct += 1
            answer = ""

        else:
            print("You lost!")
            print("Your numbers of currect answers was " + str(correct))
            break
