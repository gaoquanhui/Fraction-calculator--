import random
print("1.正常乘法计算")
print("2.正常加法计算")
print("3.圆周率计算")
print("现在仅有三种，后期会进行更新！！！！！！,若不想继续直接关闭窗口即可")
print("ps:此程序还有很多不完善的地方，后期会进行修改可以关注我的个人网站:http://66666.eu5.org/")
pattern=int(input("请输入上方其中一种模式的编号："))
if pattern==1:
    print("已进入第一种模式，现在开始进行计算练习")
    while True:
        factor1=random.randint(1,1000)
        factor2 = random.randint(1, 1000)
        product=factor1*factor2
        symbol="*"
        print(factor1,symbol,factor2)
        Input_product=int(input("请输入得数："))
        if Input_product==product:
            print("恭喜你答对了！！！！！！！！！天才！！！！！！(๑•̀ㅂ•́)و✧")
        else:
            print("答错了，下次努力！！！！！(＞﹏＜)")
if pattern==2:
    print("已进入第二种模式，现在开始进行计算练习")
    while True:
        addend1=random.randint(1,10000)
        addend2 = random.randint(1, 10000)
        sum=addend1+addend2
        symbol2="+"
        print(addend1,symbol2,addend2)
        input_sum=int(input("请输入得数："))
        if input_sum==sum:
            print("恭喜你答对了！！！！！！！！！天才！！！！！！(๑•̀ㅂ•́)و✧")
        else:
            print("答错了，下次努力！！！！！(＞﹏＜)")
if pattern==3:
    print("已进入第三种模式，现在开始进行计算练习")
    while True:
        pi=3.14
        Another_number=random.randint(1, 100)
        Get_the_number=pi*Another_number
        The_final_result=round(Get_the_number,2)
        symbol3="*"
        #print(Get_the_number)
        print(pi,symbol3,Another_number)
        input_Get_the_number=float(input("请输入得数："))
        if input_Get_the_number==The_final_result:
            print("恭喜你答对了！！！！！！！！！天才！！！！！！(๑•̀ㅂ•́)و✧")
        else:
            print("答错了，下次努力！！！！！(＞﹏＜)")