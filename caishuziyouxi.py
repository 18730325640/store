
import random
count=random.randint(0,50)
corn=5000
i=1
while i <=10:
    num=input("请输入数字：")
    num=int(num)
    if num>count:
        corn=corn-500
        print("大了！剩余金币为：",corn,"使用了",i,"次")
    elif num<count:
        corn=corn-500
        print("小了！剩余金币为：",corn,"使用了",i,"次")
    else:
        corn=corn+1000
        print("猜对了，数字为：",num,"剩余金币为：",corn,"使用了",i,"次")
        break
    i=i+1
