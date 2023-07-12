from mydetect import detectOS, sleepTime, clearScreen
import time
import random
import os

waitTime: float = 0.8
answer: str = ""
answerCount: int = 0
answerCountMax: int = 3
correct: int = 0

while True:
    if answerCount < answerCountMax:

        rnd: int = random.randint(0, 9)

        clearScreen()
        print(str(rnd))

        sleepTime(waitTime)

        answer: str = answer + str(rnd)
        answerCount += 1
    else:
        clearScreen()

        print("Your numbers of correct answers is " + str(correct))
        val: str = input("Enter your answer: ")
        if val == answer:
            print("You win!")
            sleepTime(1)

            if answerCountMax < 10:
                answerCountMax += 1
            if waitTime > 0.2:
                waitTime -= 0.1
            answerCount: int = 0
            correct += 1
            answer: str = ""

        else:
            print("You lost!")
            print("Your numbers of correct answers was " + str(correct))
            break
