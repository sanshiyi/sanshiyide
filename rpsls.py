#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：王晨薇
日期：2020年11月24日
"""
import random
def name_to_number(player_choice):  #将游戏对象对应到不同的整数
    if player_choice=="石头":
        player_choice_number=0
    elif player_choice=="史波克":
        player_choice_number=1
    elif player_choice=="纸":
        player_choice_number=2
    elif player_choice=="蜥蜴":
        player_choice_number=3
    elif player_choice=="剪刀":
        player_choice_number=4
    else:
        print("Error: No Correct Name")
    return player_choice_number
def number_to_name(comp_number):#将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    if comp_number==0:
        comp_choice="石头"
    elif comp_number==1:
        comp_choice="史波克"
    elif comp_number==2:
        comp_choice="纸"
    elif comp_number==3:
        comp_choice="蜥蜴"
    elif comp_number==4:
        comp_choice="剪刀"
    return comp_choice
def rpsls(player_choice_number,computer_number):#用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    if player_choice_number==0:
        if comp_number==3 or comp_number==4:
            print("您赢了")
        elif comp_number==1 or comp_number==2:
            print("计算机赢了")
        else:
            print("您和计算机出的一样呢")
    if player_choice_number==1:
        if comp_number==0 or comp_number==4:
            print("您赢了")
        elif comp_number==2 or comp_number==3:
            print("计算机赢了")
        else:
            print("您和计算机出的一样呢")
    if player_choice_number==2:
        if comp_number==0 or comp_number==1:
            print("您赢了")
        elif comp_number==3 or comp_number==4:
            print("计算机赢了")
        else:
            print("您和计算机出的一样呢")
    if player_choice_number==3:
        if comp_number==1 or comp_number==2:
            print("您赢了")
        elif comp_number==0 or comp_number==4:
            print("计算机赢了")
        else:
            print("您和计算机出的一样呢")
    if player_choice_number==4:
        if comp_number==2 or comp_number==3:
            print("您赢了")
        elif comp_number==0 or comp_number==1:
            print("计算机赢了")
        else:
            print("您和计算机出的一样呢")
    return

print("欢迎使用RPSLS游戏")
print("----------------")
player_choice=input("请输入您的选择:")#输入玩家选择
player_choice_number=name_to_number(player_choice)#将玩家选择转换为整数
comp_number=random.randint(0,4)#计算机随机生成一个0~4的数字
comp_choice=number_to_name(comp_number)#将计算机生成的数字转换为选择项目
print("计算机的选择为："+comp_choice)
rpsls(player_choice_number,comp_number)#比较玩家选择与计算机选择并输出结果