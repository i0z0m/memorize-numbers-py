import time
import random
import os

waitTime: float = 0.8
answer = ""
answerCount = 0
answerCountMax = 3
correct = 0

while True:
    if answerCount < answerCountMax:

        rnd: int = random.randint(0, 9)

        os.system('clear')
        print(str(rnd))

        time.sleep(waitTime)

        answer: str = answer + str(rnd)
        answerCount += 1
    else:
        os.system('clear')

        print("Your numbers of correct answers is " + str(correct))
        val: str = input("Enter your answer: ")
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
            print("Your numbers of correct answers was " + str(correct))
            break
