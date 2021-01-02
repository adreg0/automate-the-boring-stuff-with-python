import random, time

def quiz():
    a = random.randint(0, 9)
    b = random.randint(0, 9)

    print(f"{a}x{b} = ?")
    ans = a*b
    chance = 0
    s=time.time()
    duration=8
    correct = False

    while chance<3:
    #while chance<3 and time.time()<=(s+duration):
        s=time.time()

        chance += 1
        a = input("Ans: ")
        try:
            a = int(a)

        except ValueError:
            print("Not a number")
            continue
        if a==ans:
            print("Right Answer")
            correct = True
            break
        else:
            print("Try Again")
    if not correct:
        print(f"Wrong answer")

for i in range(11):
    time.sleep(1)
    quiz()