import random
tails = 0
heads = 0

a = int(input("enter the Number:"))
for i in range(a):
    if random.randint(0, 1) == 0:
        print("heads")
        heads += 1
    else:
        print("tails")
        tails += 1
        print("heads", heads)
        print("tails", tails)

        percentage_head = ((heads*100)/a)
        print("Head percentage:", percentage_head)

        percentage_tail = ((tails*100)/a)
        print("tail percentage:", percentage_tail)


