import random
poker=['黑桃A','黑桃2','黑桃3','黑桃4','黑桃5','黑桃6','黑桃7','黑桃8','黑桃9','黑桃10','黑桃J','黑桃Q','黑桃K'
       '红桃A','红桃2','红桃3','红桃4','红桃5','红桃6','红桃7','红桃8','红桃9','红桃10','红桃J','红桃Q','红桃K'
       '梅花A','梅花2','梅花3','梅花4','梅花5','梅花6','梅花7','梅花8','梅花9','梅花10','梅花J','梅花Q','梅花K'
       '方片A','方片2','方片3','方片4','方片5','方片6','方片7','方片8','方片9','方片10','方片J','方片Q','方片K','大王','小王']

random.shuffle(poker)      #洗牌
shuzhi = 0


import random


def game():
    '''开始猜大小的游戏'''
    global new_pai
    print("欢迎进入21点小游戏！！")
    print('<<<<<<<<<<<<<<<<<<<< Game Starts! >>>>>>>>>>>>>>>>>>>>')
    player = input("请输入您的游戏名：")
    print("欢迎玩家{}".format(player))

    # 1-10       JQK >   11 12 13     小王 14  大王 15

    print("开始发牌")
    your_pai = random.randint(1, 15)
    if your_pai > 10:
        your_pai = 10
    print(your_pai)
    while True:
        ans = input("是否还要牌？ Y/N")
        if ans == "Y":
            new_pai = random.randint(1, 15)
            print("本次手牌为：{}".format(new_pai))
            if new_pai > 10:
                new_pai = 10
            your_pai += new_pai
            print("总数为:{}".format(your_pai))
        if your_pai > 21:
            print("Game over!")
            break
        if ans == "N":
            break

    sys_pai = random.randint(1, 15)
    print(sys_pai)
    while sys_pai <= 21:
        sys_newpai = random.randint(1, 15)
        if sys_newpai > 10:
            sys_newpai = 10
        sys_pai += sys_newpai
        if your_pai <= sys_pai:
            print("系统玩家的手牌总和为{},you lose!".format(sys_pai))
            break

    else:
        print("系统玩家的手牌总和为{},you win!".format(sys_pai))

if __name__ == '__main__':
    game()
