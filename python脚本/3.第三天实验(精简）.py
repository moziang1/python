import random
# 定义字典来存储用户及密码
users = {}
# 添加用户列表
list = []
#猜拳游戏函数
def caiquan():
    print("玩家默认有5次机会，可以使用金币购买。如果机会不足，将无法进行游玩")
    jihuicishu = 5  # 定义初始生命值
    lssl = 0        # 定义连胜的值
    lssw = 0        # 定义连胜的隐藏值，和连胜值相同，在5连胜增加次数时，替代连胜值删除
    jinbi = 0       # 定义金币数量
    jingyan = 0     # 定义经验值
    level = 0       # 定义等级
    while True:
        print("您的等级为",level,"级")
        print("您的经验值为",jingyan)
        print("您剩余", jihuicishu, "次机会")
        print("您持有金币数量为",jinbi)
        if lssw >= 5:        #隐藏值为5，必定5连胜
            print("您达成",lssl,"连胜本轮不消耗机会")    #输出连胜次数，连胜的倍数
            #设置要求，连胜次数5次以上，添加
            if lssw >= 5 :
                lssw -= 5
                jihuicishu +=1
                print("恭喜您，达成",lssl,"连胜增加一次挑战机会")
        if jihuicishu <= 2 :
            print("您的游戏机会只剩下",jihuicishu,"次机会了，是否花费5个金币购买生命次数")
            temp = input("y/n")
            if temp == 'y' or temp == 'Y':
                if jinbi >= 5:
                    jinbi -= 5
                    jihuicishu += 1
                    print("您的机会还剩余",jihuicishu,"次机会")
                else:
                    print("您的金币数量为",jinbi,"不足以购买生命次数")
        xxx = input('是否开始游戏（y/n）,输入(q,Q)退出程序')
        if jihuicishu >=1 :
            print("\n")
        else:
            chishuhaojin = input("您的次数耗尽，是否退出游戏（q/Q），或购买次数（w）")
            if chishuhaojin == 'q' or chishuhaojin == "Q":
                break
            elif chishuhaojin == 'w' or chishuhaojin == 'W':
                continue
        if xxx == 'y' or xxx == 'Y':
            jihuicishu -= 1
            print('开始游戏')

            test1 = ['石头', '剪刀', '布']

            ran = random.choice(test1)
            print(ran)       #为了方便测试连胜，将电脑人的输出

            temp = input('我们来玩猜拳吧（石头，剪刀，布）任意一个')
            if temp == ran:
                print('平局，不消耗次数')
            elif temp == '石头' and ran == '剪刀' or temp == '剪刀' and ran == '布' or temp == '布' and ran == '石头':
                print('犹豫了很久的你，艰难的战胜了新手难度(╯‵□′)╯︵┻━┻')
                lssl +=1       #记录连胜次数
                lssw +=1       #记载连胜次数的隐藏值
                jinbi +=1
                jingyan += random.randrange(20,40)
                if jingyan > 100:
                    level += 1
                    jingyan = 0
                    jihuicishu +=5
                    print("恭喜您，升级了，目前等级",level,"级，清空经验值,增加5次机会")
            elif temp == '石头' and ran == '布' or temp == '布' and ran == '剪刀' or temp == '剪刀' and ran == '石头':
                print('电脑获胜')
                lssl = 0
                print('电脑人迅速的战胜了你(*Φ皿Φ*)')
            else:
                print('输入有误，重新输入')
        elif xxx == 'Q' or xxx == 'q':
            exit()
        else:
           print('其余功能并没有开发，您可以留下来继续游玩，也可以输入Q退出')
#用户登陆
def denglu():
    # 用户登陆判断
    #while True:        #判断数据库中是否存在该用户
        uname = input("请输入您的用户名:")
        for i in list:
            if uname == i:
                www = i
                upwd = input("请输入您的密码:")
                if upwd == users[www]:
                    print("登陆成功")
                    print('目前本项目正在逐渐开发完善，目前仅开放猜拳游戏')
                    caiquan()
                else:
                    print("密码错误")
            #else:  # 否则的意思，用来处理符合条件之外的情况
        print("没有该用户，请先注册用户")
        #break
#用户注册
def zuce():
    global list
    global users
    while True:
        user = input("请输入您的用户名(3位以上）:")
        # 检查用户名是否由字符串（数字，字母）或文字组成，并且在3个以上
        if user.isalpha and len(user) > 3:
            print('满足条件')
            # 检测用户名冲突
            if user in list:
                print('******该用户名已被使用，请重新注册*******')
                continue
            else:
                # 输入密码
                uswd1 = input("请输入您的密码（至少8位）:")
                uswd2 = input("再次输入密码")
                # 判断两边密码是否正确，是否由数字字母组成，长度4位以上
                if uswd1 == uswd2 and uswd1.isalnum() and len(uswd1) >= 8:
                    list.append(user)
                    users[user] = uswd1  # 给users字典，添加键为用户名，值为密码
                    print("注册成功", '\n''您的账户是:', user, '\n', '您的密码是:', uswd1)
                    break
                else:
                    print('您输入的密码不满足要求')
                    print('是否由数字字母组成，长度4位以上')
        else:
            print('您输入的必须是一个数字加字符，并且长度大于3')
#主体函数
def main():
    '''
    主体函数
    '''
    while True:
        temp = input('登陆/注册')
        if temp == '登陆':
            denglu()
        elif temp == '注册':
            zuce()
        else:
            print('请正确输入')

if __name__ == '__main__':
    main()
