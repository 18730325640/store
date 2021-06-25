'''
    Jason的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10辣条优惠券（0.3），20机械革命优惠券（0.9）。
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。


'''
i=10
shop=[
    ['牙膏',75],
    ['肥皂',35],
    ['牙刷',55],
    ['电脑',155],
    ['袜子',20],
    ['半袖',300],
    ['辣条',18]
]


shopcart=[]

money=input('请输入你的钱包余额：')
money=int(money)

import random

count=random.randint(0,1)
print(count)
print('请抽取随机优惠券')
if count==1:
    print('恭喜抽中电脑九折优惠券')
elif count==0:
    print('恭喜抽中辣条三折优惠券')
while True:
    for (a,b) in enumerate(shop):
        print(a,b)
    num=input('请输入要购买的商品序号：')
    if num.isdigit():
        num=int(num)
        if num>=len(shop):
            print('请输入正确的商品序号')
        else:
            if money>shop[num][1]:
                if count==1 and shop[num][0]=='电脑' and i>0:
                    money = money - shop[num][1] * 0.9
                    i=i-1
                elif count==0 and shop[6][0]=='辣条' and i>0:
                    money = money - (shop[num][1] * 0.3)
                    i=i-1
                else:
                    money-=shop[num][1]
                shopcart.append(shop[num][0])
                print('已经购买：',shopcart,'账户还有￥: ',money)
            else:
                print('余额不足!账户还剩：￥',money)
    elif num=="q"or num=="Q":
        print("欢迎下次光临")
        break
    else:
        print("输入格式错误，请重新输入")
print('购物小票:')
print(shopcart)
print('你还剩：￥',money)








