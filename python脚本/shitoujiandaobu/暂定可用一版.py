import random
import time
import urllib.request
import urllib.parse  # parse现在不属于request的范围的模块了，所以要单独添加
import json

#用户名的身份检测（特殊符号检测)
temp2 = 0

'''
    用户登录模块
'''
class user():
    #用户注册
    def zuce(self):
        global temp2
        while True:
            user = input("请输入您的用户名(3位以上）:")
            # 检查用户名是否由字符串（数字，字母）或文字组成，并且在3个以上

            #检测用户输入是否为空
            if not user.strip():
                print("您的输入为空")
                continue

            #检测用户名是否有特殊符号
            self.jiance(user)
            if temp2 == 1 :
                print("输入的用户名包含特殊字符，不可用")
                temp2 = 0
                continue

            if user.isalpha and len(user) > 3:
                # 检测用户名冲突
                # 读取用户名文件，用于验证
                loadfile = open('userlist.txt', mode='rb')  # 只读打开文件
                list = loadfile.read().decode("utf-8")
                result = list.split(' ')  # 将用户列表信息做成列表存在
                loadfile.close()

                if user in result:  # 使用用户与用户列表中的用户进行对比，如果相同则被占用
                    print('******该用户名已被使用，请重新注册*******')
                    continue
                else:
                    print('满足条件')
                    # 输入密码
                    uswd1 = input("请输入您的密码（至少8位）:")
                    uswd2 = input("再次输入密码")

                    # 判断两边密码是否正确，是否由数字字母组成，长度4位以上
                    if uswd1 == uswd2  and len(uswd1) >= 8:

                        # 写入用户名及密码
                        file = open(user + '.txt', mode="w")
                        file.write(user + ' ' + uswd1)
                        file.close()

                        # 记录所有用户，用户名的文件
                        file = open('userlist.txt', mode="a")
                        file.write(' ' + user)
                        file.close()

                        # 给users字典，添加键为用户名，值为密码
                        print("注册成功", '\n''您的账户是:', user, '\n', '您的密码是:', uswd1)
                        break
                    else:
                        print('您输入的密码不满足要求')
                        print('是否由数字字母组成，长度4位以上')
            else:
                print('您输入的必须是一个数字加字符，并且长度大于3')

    #初始化用户列表
    def init(self):
        #创建用户列表
        try:
            open('userlist.txt', mode="x").close()  # 尝试新建用户输入的字符串的文件，
        except FileExistsError:  # 只要当上面语句出现我规定的报错（FileExistsError）才执行
            print(" \n ")

    #用户登陆时的操作
    def denglu(self):
        global temp2
        while True:
            # 用户登陆判断
            uname = input("请输入您的用户名:")

            #检测用户输入是否为空
            if not uname.strip():
                print("您的输入为空")
                continue

            # 判断是否有特殊字符
            self.jiance(uname)
            if temp2 == 1 :
                print("输入的用户名包含特殊字符，不可用")
                temp2 = 0
                continue


            # 读取用户名文件，用于验证
            loadfile = open('userlist.txt', mode='rb')  # 只读打开文件
            list = loadfile.read().decode("utf-8")
            result = list.split(' ')  # 将用户列表信息做成列表存在
            loadfile.close()

            #判断 用户列表中是否有该用户
            if uname in result:
                upwd = input("请输入您的密码:")
                #抽取该用户的数据，拿到用户密码信息
                loadfile = open(uname+'.txt', mode='rb')  # 只读打开二进制文件
                result = loadfile.read().decode("utf-8")
                unamelist = result.split(' ')
                loadfile.close()

                #验证用户输入的密码
                if upwd == unamelist[1]:
                    #如果用户及密码正确，即可登陆成功
                    self.dengluchenggong(uname)
                    break

                else:
                    print("密码错误")
            else:
                print("没有该用户，请先注册用户，请先注册用户，跳转中")

                self.zuce()

    #检测用户名是否使用特殊字符
    def jiance(self,temp):
        global temp2
        # 判断是否有特殊字符
        string = "~!@#$%^&*()_+-*/<>,.[]\/ "
        for i in string:
            if i in temp:
                temp2 = 1
                break

    #用户登陆成功后如何引导
    def dengluchenggong(self,uname):
        print("登陆成功")
        print('目前本项目正在逐渐开发完善中，如遇到BUG请发送邮箱地址2665483426@qq.com进行审核')
        while True:
            print('***************游戏列表********************')
            print('A. 猜拳游戏')
            print('B. 翻译功能')
            print('C. 暂未开放')
            temp = input('请输入您要游玩的编号，或输入q退出')
            if  temp == 'A' or temp == '猜拳' or temp == 'a':
                youxi.caiquan(uname)
            elif temp == '翻译' or temp == 'b' or temp == 'B':
                gongneng.fanyi()
            elif temp == 'q' or temp == 'Q':
                break
            else:
                print('您输入功能暂未开放，请稍后再试')

#实例化类
user = user()


'''
    猜拳游戏相关模块
'''

class youxi():
#猜拳游戏初始化（存储）
    def chushihcaiquan (self,uname, level, jinbi, jingyan, jihuicishu, lssl, lssw):
        # 初始化写入游戏数据到本地存档
        file = open(uname + '存档.txt', mode="w")
        file.write(
            str(level) + ' ' + str(jinbi) + ' ' + str(jingyan) + ' ' + str(jihuicishu) + ' ' + str(lssl) + ' ' + str(lssw))
        file.close()

    #猜拳游戏本体
    def yxbt(self,uname, level, jinbi, jingyan, jihuicishu, lssl, lssw):
        #npc列表，用来后面随机npc登陆用
        list = [npc1,npc2,npc3]

        # 用作与本函数全局变量，判断npc是否阵亡
        tempx = 0

        while True:

            if tempx == 0 :  #等于0，代表没有npc上阵，需要上阵一名npc
                # tempA的值是一名随机npc类的值
                tempA = random.choice(list)
                #拿到该npc的基础值
                name = tempA.name
                hp = tempA.hp
                mp = tempA.mp
                exp = tempA.exp
                gold = tempA.gold




                # 对象删除         (把class列表中的值拿出来对比name是否等于刚才拿到的name，如果是，则删除
                for user in list[:]:
                    if user.name == tempA.name:
                        list.remove(user)

                #并为tempx赋值为1表示已有npc上阵
                tempx = 1
                #实现了什么功能，我们将npc的值轮询放到这个函数中去运行

            else:
                #判断npc阵亡
                if hp <= 0:
                    print(name,'阵亡')
                    tempx = 0
                    print('您获得npc',name,'的所有金币')
                    jinbi += gold
                    print('您获得经验',exp)
                    jingyan += exp
                    xixi = []
                    if list == xixi:
                        print('恭喜您击杀了所有的怪物，魔塔已经安全了。 ')
                        break
                    continue

                print("\n")
                print("\n")
                print("您的等级为", level, "级")
                print("您的经验值为", jingyan)
                print("您剩余", jihuicishu, "次机会")
                print("您持有金币数量为", jinbi)

                #关于连胜机会次数+1
                if lssw >= 5:  # 隐藏值为5，必定5连胜
                    print("您达成", lssl, "连胜")  # 输出连胜次数，连胜的倍数
                    # 设置要求，连胜次数5次以上，添加
                if lssw >= 5:
                    lssw -= 5
                    jihuicishu += 1
                    print("恭喜您，达成", 5 , "连胜增加一次挑战机会")

                #机会次数小于等于2次时提醒购买次数
                if jihuicishu <= 2 and jinbi >= 5:
                    print("您的游戏机会只剩下", jihuicishu, "次机会了，是否花费5个金币购买生命次数")
                    temp = input("y/n")
                    if temp == 'y' or temp == 'Y':
                        if jinbi >= 5:
                            jinbi -= 5
                            jihuicishu += 1
                            print("您的机会还剩余", jihuicishu, "次机会")


                #玩家游玩机会耗尽时，会选择退出游戏还是，购买次数
                if jihuicishu >= 1:
                    print("\n")
                else:
                    chishuhaojin = input("您的次数耗尽，是否退出游戏（q/Q），或购买次数（w）")
                    if chishuhaojin == 'q' or chishuhaojin == "Q":
                        break
                    elif chishuhaojin == 'w' or chishuhaojin == 'W':
                        continue





                #游戏本体，进行游戏
                jihuicishu -= 1


                #定义规则
                test1 = ['石头', '剪刀', '布']

                #随机列表test1中是元素
                ran = random.choice(test1)
                print(ran)  # 为了方便测试连胜，将电脑人的输出


                #指定释放技能的概率
                rans = random.randrange(5)
                if rans == 3:
                    #npc释放技能
                    if name == '强盗':
                        jingyan = npc1.jn(jingyan)
                    elif name == '扒手':
                        if mp >= 5 :
                            mp -= 5
                            jinbi = npc2.jn(jinbi)
                    elif name == '狐狸精怪':
                        if mp >= 5:
                            mp -= 5
                            hp = npc3.jn(hp)


                print('\n')
                print('你碰到了精英怪',name)
                print('生命值',hp)
                print('法力值',mp)

                temp = input('我们来玩猜拳吧（石头，剪刀，布）任意一个')

                #输入为空检测
                if not temp.strip():
                    print("输入不可为空")
                    jihuicishu += 1
                    continue


                if temp == ran:
                    print('平局')
                elif temp == '石头' and ran == '剪刀' or temp == '剪刀' and ran == '布' or temp == '布' and ran == '石头':
                    print('你艰难的战胜了'+name+'(╯‵□′)╯︵┻━┻')
                    hp -= 3
                    lssl += 1  # 记录连胜次数
                    lssw += 1  # 记载连胜次数的隐藏值
                    jinbi += 1
                    jingyan += random.randrange(20, 40)
                    if jingyan > 100:
                        level += 1
                        jingyan -= 100
                        jihuicishu += 5
                        print("恭喜您，升级了，目前等级", level, "级，清空经验值,增加5次机会")
                elif temp == '石头' and ran == '布' or temp == '布' and ran == '剪刀' or temp == '剪刀' and ran == '石头':
                    print( '电脑人'+name+'获胜')
                    lssl = 0

                else:
                    print('输入有误，重新输入')

                temp = input('是否进行存档（y）(回车继续')
                if temp == 'y' or temp == 'Y' or temp == 'yes' or temp == 'YES':
                    self.chushihcaiquan(uname, level, jinbi, jingyan, jihuicishu, lssl, lssw)
                    print('存档中')
                    time.sleep(5)
                    print('存档完毕，是否退出游戏(q) 回车继续游戏')
                    temp = input()
                    if temp == 'q' or temp == 'Q':
                        break

    #猜拳游戏函数（用于作为引导）
    def caiquan(self,uname):
        print("玩家默认有5次机会，可以使用金币购买。如果机会不足，将无法进行游玩\n\n\n\n")
        jihuicishu = 5  # 定义初始生命值
        lssl = 0        # 定义连胜的值
        lssw = 0        # 定义连胜的隐藏值，和连胜值相同，在5连胜增加次数时，替代连胜值删除

        #需要存储的值
        jinbi = 0       # 定义金币数量
        jingyan = 0     # 定义经验值
        level = 0       # 定义等级


        #做个单独的文件用来存储登陆过游戏的用户，检测这个列表用户是否登陆过游戏，如果登陆过，就代表不是第一次登陆，就不需要初始化
        #如果是第一次登陆则初始化写入，
        #初始化用户数据


        #确保有用户列表文件
        try:
            open('userlogin.txt', mode="x").close()     #每次登陆游戏都检测一次是否有用户的登陆记录，如果没有则新建
        except FileExistsError:
            print(" \n ")

        #检测列表中是否有当前登陆用户的记录
        #如果有该用户则询问是否读档，如果没有，则初始化
        filel = open('userlogin.txt',mode='rb')
        haha  = filel.read().decode()
        result = haha.split(' ')
        filel.close()

        #如果用户名在登陆过的用户列表中，那么就表明已经登陆过了，不用初始化数据
        if uname in result:
            while True:                #判断是否进行载入存档和新游戏
                try:
                    open(uname + '.txt', mode="x").close()  # 每次登陆游戏都检测一次是否有用户的登陆记录，如果没有则新建
                except FileExistsError:
                    temp = input('是否载入存档 （y/Y） 回车开始新游戏')
                    if temp == 'y' or temp == 'Y':
                        # 读取玩家的存档
                        filel = open(uname + '存档.txt', mode="rb")
                        haha = filel.read().decode('utf-8')
                        result = haha.split(' ')

                        # level + jinbi + jingyan + jihuicishu + lssl + lssw  根据写入文件的顺序索引导入值
                        level = int(result[0])
                        jinbi = int(result[1])  # int将值都转换位整数型方便对比
                        jingyan = int(result[2])
                        jihuicishu = int(result[3])
                        lssl = int(result[4])
                        lssw = int(result[5])
                        print('游戏初始化中')
                        time.sleep(5)
                        # 载入游戏后，将数据传输给游戏本体
                        self.yxbt(uname, level, jinbi, jingyan, jihuicishu, lssl, lssw)
                        break

                    #当没有存档的情况下，直接开始游戏
                    print('开始新游戏')

                    #跳转到初始化数据
                    self.chushihcaiquan(uname, level, jinbi, jingyan, jihuicishu, lssl, lssw)

                    #跳转到游戏本体，但用户退出游戏的时候退出这个函数
                    self.yxbt(uname,level,jinbi,jingyan,jihuicishu,lssl,lssw)
                    break


        else:                 #这里是表明，没有登陆过的用户去初始化数据，以及写入到用户登陆列表中
            file = open('userlogin.txt', mode="a")
            file.write(' ' + uname)
            file.close()

            #初始化用户数据（给新用户初始化数据文件）
            self.chushihcaiquan(uname,level,jinbi,jingyan,jihuicishu,lssl,lssw)

youxi = youxi()


'''
    功能类
'''
class gongneng():
    def fanyi(self):
        while True:
            haha = input('输入你想要翻译的单词或语句：')
            #检测用户输入是否为空
            if not haha.strip():
                print("您的输入为空")
                continue

            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
            date = {}  # 这里做一个字典，将我们请求要上传的信息全都写到date中，另外，如果我们在下面urlopen中使用date，那么默认使用的请求方法就是POST

            date['i'] = haha  # 从这里开始
            date['from'] = 'AUTO'
            date['to'] = 'AUTO'
            date['smartresult'] = 'dict'
            date['client'] = 'fanyideskweb'
            date['salt'] = '15755234720405'
            date['sign'] = '393a0a7bc1d6619962c71ae755574915'
            date['ts'] = '1575523472040'
            date['bv'] = 'bc250de095a39eeec212da07435b6924'
            date['doctype'] = 'json'
            date['version'] = '2.1'
            date['keyfrom'] = 'fanyi.web'
            date['action'] = 'FY_BY_CLICKBUTTION'  # 到这里结束，就是客户端的请求头部信息

            date = urllib.parse.urlencode(date).encode(
                'utf-8')  # 修改编码格式, .urlencode(data)就是将数据做成一个urlencode的文件个数，.encode('utf-8')就是将urlencode的文件格式做成一个utf-8的编码格式

            response = urllib.request.urlopen(url, date)  # 如果这里的date被赋值了，那么这个请求就是以POST模式去请求

            html = response.read().decode(
                'utf-8')  # .read()得到的是一个utf-8的编码形式的文件，  .decode('utf-8')就是将其他编码形式的文件更改为（utf-8的编码格式)，相当于，把.read()的编码文件，解码成一个utf-8的解码格式

            target = json.loads(html)  # 找到对应的键,因为有两次列表，所以用[0][0]，"tgt"是列表中的键，调用键，就可以得到值

            print(target['translateResult'][0][0]["tgt"])  # 找到对应的键,因为有两次列表，所以用[0][0]，"tgt"是列表中的键，调用键，就可以得到值
            temp = input('是否退出翻译（q） 回车继续')
            if temp == 'q' or temp == 'Q':
                break

#类实例化
gongneng = gongneng()

'''
    npc类
'''

class npc1():
    name = '强盗'
    hp = 10
    mp = 1
    exp = 20
    gold = 30
    #恼羞成怒，失败次数到达3次时，对你进行冲撞，经验值清零
    def jn(self,jingyan):
        jingyan = 0
        print('强盗释放技能：冲撞。清空您的经验值')
        return jingyan
class npc2():
    name = '扒手'
    hp = 5
    mp = 10
    exp = 20
    gold = 40
    #技能，妙手空空  偷取到您随机金钱
    def jn(self,jinbi):
        temp = random.randrange(jinbi)
        print('扒手释放技能：妙手空空')
        print('偷取您',temp,'个金币')
        return jinbi - temp

class npc3():
    name = '狐狸精怪'
    hp = 15
    mp = 30
    exp = 20
    gold = 5
    #技能，魅惑，对方提升了5点生命值
    def jn(self,hp):
        print('狐狸精怪释放技能: 魅惑  恢复5点生命值')
        return hp + 5



npc1 = npc1()
npc2 = npc2()
npc3 = npc3()

#主体函数（作为所有函数的引导）
def main():
    '''
    主体函数
    '''
    #初始化用户文件
    user.init()

    #进入程序
    while True:
        temp = input('登陆/注册(退出程序q）')
        if temp == '登陆' or temp == '登录':
            user.denglu()
        elif temp == '注册':
            user.zuce()
        elif temp == 'q' or temp == 'Q':
            exit()
        else:
            print('请正确输入')

if __name__ == '__main__':
    main()
