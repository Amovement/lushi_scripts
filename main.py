# -*- coding:utf-8 -*-
#作者：Amove
#时间：2022年6月12日
from random import randint
from common import *
import time

# 700,400 界面大小
# 550,195 结束回合
# 500,329 选择角色
# 350,317 选牌确认
# 495,327 开始战斗
# 677,384 设置按钮
# 350,160 认输按钮

def StoneAi():
    while True:
        # 开始比赛
        print("开始比赛")
        moveAndClick(495,327)
        time.sleep(10)
        print("选择角色")
        moveAndClick(500,329)
        HeartStop()

        # 结束选牌
        print("结束选牌")
        moveAndClick(350,317)
        HeartStop()

        MyTurn = randint(0,4)
        while MyTurn>0:
            # 随机过一回合
            print("MyTurn 剩余:",MyTurn)
            print("随机过一回合")
            moveAndClick(550,195)
            HeartStop()
            MyTurn = MyTurn - 1 


        # 认输组合拳
        print("认输组合拳")
        moveAndClick(677,384)
        HeartStop()
        moveAndClick(350,160)
        time.sleep(5)
        # 随便找两个地方点两下
        print("随便找两个地方点两下: ")
        x = randint(100,700)
        y = randint(100,400) 
        moveAndClick(x,y)
        time.sleep(10)


#主函数
if __name__=='__main__':
    def main():
        time.sleep(2)
        ok,left,top,right,bottom,hwnd=FindHearthStoneWindow()
        SetModelPos(hwnd)
        StoneAi()
    #启动
    main()