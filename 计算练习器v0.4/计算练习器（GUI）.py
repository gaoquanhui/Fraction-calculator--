import Calculation_process
import easygui as e
e.msgbox("现在已经包含了加减乘除，后期会进行更新！！！！！！,若不想继续直接关闭窗口即可")
e.msgbox("ps:此程序还有很多不完善的地方，后期会进行修改可以关注我的个人网站:https://gaoquanhui.github.io")
msg = "请选择你要练习的模式"
title = "计算练习器"
choices = ["1.正常乘法计算", "2.正常加法计算", "3.圆周率计算", "4.除法计算","5.减法计算","6.查看历史纪录"]
choice = e.choicebox(msg, title, choices)
if choice == "1.正常乘法计算":
    e.msgbox("已进入第一种模式，现在开始进行计算练习")
    Calculation_process.multiplication()
elif choice == "2.正常加法计算":
    e.msgbox("已进入第二种模式，现在开始进行计算练习")
    Calculation_process.addition()
elif choice=="3.圆周率计算":
    e.msgbox("已进入第三种模的模式现在开始进行计算练习")
    Calculation_process.PI()
elif choice=="4.除法计算":
    e.msgbox("已进入第四种模式，现在开始进行计算练习")
    Calculation_process.division()
elif choice=="5.减法计算":
    e.msgbox("已进入第五种模式，现在开始进行计算练习")
    Calculation_process.subtraction()
elif choice=="6.查看历史纪录":  #察看历史记录判断
    Calculation_process.View_History()