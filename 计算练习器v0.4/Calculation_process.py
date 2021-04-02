import easygui as e
import random
import time
i=int()

#历史记录
def History():
    '''记录历史记录'''
    with open("History.txt","a+") as f:
        a= time.strftime("%Y-%m-%d %H:%M:%S   ")
        print(a)
        f.write(a)
        f.write(b+'\n')
def View_History():
    with open("History.txt","r") as f:
        read=f.read()
    e.msgbox(read,"历史记录")
#乘法计算
def multiplication():

     while True:
        global i
        global b
        factor1=random.randint(1,100) #取值因数1
        factor2 =random.randint(1, 100) #取值因数2
        product=factor1*factor2
        symbol="×"
        msgbox=factor1,symbol,factor2,"="
        Input_product=e.enterbox(msgbox,"请输入得数：")#输入结果
        if Input_product=="Q":
            History()
            break
        else:
            a=int(Input_product)
        print(type(Input_product))
        #判断结果
        if a==product:
            e.msgbox("恭喜你答对了！！！！！！！！！天才！！！！！！(๑•̀ㅂ•́)و✧")
            i = i + 1
            b=str(i)
            #print(i)
        else:
            e.msgbox("答错了，下次努力！！！！！(＞﹏＜)")
#加法计算
def addition():
    while True:
        global i
        addend1=random.randint(1,1000)  #取值加数1
        addend2 = random.randint(1, 1000)  #取值加数2
        sum=addend1+addend2
        symbol2="+"
        msgbox=(addend1,symbol2,addend2,"=")
        input_sum=int(e.enterbox(msgbox,"请输入得数："))
        #判断结果
        if input_sum==sum:
            e.msgbox("恭喜你答对了！！！！！！！！！天才！！！！！！(๑•̀ㅂ•́)و✧")
            i = i + 1
        else:
            e.msgbox("答错了，下次努力！！！！！(＞﹏＜)")
#除法计算
def division():
    while True:
        global i
        Divisor=random.randint(1,100)
        divisor=random.randint(1,100)
        symbol3="÷"
        merchant=round(Divisor/divisor,1)
        #print(merchant)
        msgbox=(Divisor,symbol3,divisor,"=")
        input_merchant=float(e.enterbox(msgbox,"请输入得数(保留一位小数)："))
        # 判断结果
        if input_merchant == merchant:
            e.msgbox("恭喜你答对了！！！！！！！！！天才！！！！！！(๑•̀ㅂ•́)و✧")
            i = i + 1
        else:
            e.msgbox("答错了，下次努力！！！！！(＞﹏＜)")
#减法计算
def subtraction():
    while True:
        global i
        minuend=random.randint(100,1000)
        subtraction=random.randint(1,100)
        symbol4="-"
        difference=minuend-subtraction
        msgbox=(minuend,symbol4,subtraction,"=")
        input_difference=int(e.enterbox(msgbox,"请输入得数："))
        if input_difference == difference:
            e.msgbox("恭喜你答对了！！！！！！！！！天才！！！！！！(๑•̀ㅂ•́)و✧")
            i = i + 1
        else:
            e.msgbox("答错了，下次努力！！！！！(＞﹏＜)")
#圆周率
def PI():
    while True:
        global i
        pi=3.14
        Another_number=random.randint(1, 100)
        Get_the_number=pi*Another_number
        The_final_result=round(Get_the_number,2)
        symbol3="*"
        #print(Get_the_number)
        msgbox=(pi,symbol3,Another_number,"=")
        input_Get_the_number=float(e.enterbox(msgbox,"请输入得数："))
        if input_Get_the_number==The_final_result:
            e.msgbox("恭喜你答对了！！！！！！！！！天才！！！！！！(๑•̀ㅂ•́)و✧")
            i = i + 1
        else:
            e.msgbox("答错了，下次努力！！！！！(＞﹏＜)")