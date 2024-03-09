import os
import random
import getchar

地图 = []
实体 = []

def 键盘输入(键盘):
    if 键盘 == getchar.getchar():
        return 1
    else:
        return 0

class 实例():
    def __init__(self,x=0,y=0,show='P'):
        global 实体
        self.x = x
        self.y = y
        self.show = show
        实体[x][y] = show
    def goto(self,x,y):
        实体[self.x][self.y] = ''
        self.x = y
        self.y = y
        实体[self.x][self.y] = 'P'
    def sprite(self,show):
        实体[self.x][self.y] = show
        self.show = show

def 地图渲染(地图,实体):
    for x in range(16):
        for y in range(16):
            if 实体[x][y] != "":
                print(实体[x][y],end='')
            elif 地图[x][y] == 0:
                print('·',end='')
            else:
                print('?',end='')
        print('')

def 地图清除():
    os.system('cls')

for i in range(16):
    实体.append([])
    for x in range(16):
        实体[i].append('')

for i in range(16):
    地图.append([])
    for x in range(16):
        地图[i].append(random.randint(0,10))
玩家 = 实例()
地图渲染(地图,实体)
