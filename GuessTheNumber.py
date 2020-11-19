import random
trycount=0
j=random.randint(1,11)
print(j)
print("可以猜10次")
while trycount<10:
    if trycount>=1:
        print("還可以猜{}次".format(10-trycount))
    answer=input("請在1~10猜一個數字:")
    if answer=="" or int(answer)>10 or int(answer)<=0:
        print("來亂的?多扣你一次機會")
        trycount+=2
    elif int(answer)==j:
        print("猜對了")
        break
    else:
        print("再猜一次")
        trycount+=1
else:
    print("機會用完囉~")
