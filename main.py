import random
import time
numbers = 3
ArrNum = []
StrNum = ""
Time = 0.5
k = 1
while True:
    k = k + 1
    ArrNum = []
    StrNum = ""
    for i in range(numbers):
        ArrNum.append(random.randint(1,9))
        StrNum = StrNum + str(ArrNum[i])
    print(StrNum)
    time.sleep(Time)
    for i in range(200):
        print("\n")
    answer = input("What was the number?: ")
    if str(answer) == str(StrNum):
        print("Correct")
        time.sleep(0.5)
        Time = Time - 0.025
        if k % 10 == 0:
            numbers = numbers + 1
            Time = Time + 0.5
        k = k + 1
    else:
        print("Wrong it was " + str(StrNum))
        time.sleep(3)
        Time = Time + 0.1
        if k % 10 == 0:
            numbers = numbers - 1
    

