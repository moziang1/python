import random

# 定义字典来存储用户及密码
users = {}
# 添加用户列表
list = []


#猜拳游戏函数
def caiquan():
    while True:
        xxx = input('是否进行猜拳游戏（y/n）退出输入Q/q即可')
        if xxx == 'y' or xxx == 'Y':
            print('开始游戏')
            test1 = ['石头', '剪刀', '布']
            ran = random.choice(test1)
            temp = input('我们来玩猜拳吧（石头，剪刀，布）任意一个')
            if temp == ran:
                print('平局')
            elif temp == '石头' and ran == '剪刀' or temp == '剪刀' and ran == '布' or temp == '布' and ran == '石头':
                print('犹豫了很久的你，艰难的战胜了新手难度(╯‵□′)╯︵┻━┻')

            elif temp == '石头' and ran == '布' or temp == '布' and ran == '剪刀' or temp == '剪刀' and ran == '石头':
                print('电脑获胜')
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
    while True:        #判断数据库中是否存在该用户
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
        break

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
