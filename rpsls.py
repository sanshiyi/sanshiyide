#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����ޱ
���ڣ�2020��11��24��
"""
import random
def name_to_number(player_choice):  #����Ϸ�����Ӧ����ͬ������
    if player_choice=="ʯͷ":
        player_choice_number=0
    elif player_choice=="ʷ����":
        player_choice_number=1
    elif player_choice=="ֽ":
        player_choice_number=2
    elif player_choice=="����":
        player_choice_number=3
    elif player_choice=="����":
        player_choice_number=4
    else:
        print("Error: No Correct Name")
    return player_choice_number
def number_to_name(comp_number):#������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    if comp_number==0:
        comp_choice="ʯͷ"
    elif comp_number==1:
        comp_choice="ʷ����"
    elif comp_number==2:
        comp_choice="ֽ"
    elif comp_number==3:
        comp_choice="����"
    elif comp_number==4:
        comp_choice="����"
    return comp_choice
def rpsls(player_choice_number,computer_number):#�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    if player_choice_number==0:
        if comp_number==3 or comp_number==4:
            print("��Ӯ��")
        elif comp_number==1 or comp_number==2:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
    if player_choice_number==1:
        if comp_number==0 or comp_number==4:
            print("��Ӯ��")
        elif comp_number==2 or comp_number==3:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
    if player_choice_number==2:
        if comp_number==0 or comp_number==1:
            print("��Ӯ��")
        elif comp_number==3 or comp_number==4:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
    if player_choice_number==3:
        if comp_number==1 or comp_number==2:
            print("��Ӯ��")
        elif comp_number==0 or comp_number==4:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
    if player_choice_number==4:
        if comp_number==2 or comp_number==3:
            print("��Ӯ��")
        elif comp_number==0 or comp_number==1:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
    return

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
player_choice=input("����������ѡ��:")#�������ѡ��
player_choice_number=name_to_number(player_choice)#�����ѡ��ת��Ϊ����
comp_number=random.randint(0,4)#������������һ��0~4������
comp_choice=number_to_name(comp_number)#����������ɵ�����ת��Ϊѡ����Ŀ
print("�������ѡ��Ϊ��"+comp_choice)
rpsls(player_choice_number,comp_number)#�Ƚ����ѡ��������ѡ��������