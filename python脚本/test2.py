import pymysql

# 创建数据库链接
db = pymysql.connect(host='192.168.1.1', port=3306,
                     user='root',
                     passwd='123.com',
                     charset='utf8', db='zxz')

# 应用数据库连接
cursor = db.cursor()

# 创建插入语句 这里后面使用"""+na+""" 3引号只是为了保证它是作为一个变量使用
sql = 'create table sjbinfo( ID int(4) auto_increment primary key \
        ,zname varchar(20) not null unique \
        ,zpwd varchar(20) not null \
        ,level int(4) \
        ,jinbi int(4)\
        ,jingyan int(4) \
        ,lscs int(4)\
        ,ycls int(4));'

# 尝试执行sql语句
try:
    cursor.execute(sql)  # 提交到我们的数据
    db.commit()
except:
    db.rollback()  # 如果报错的话，则回滚数据库
    print("已有该表")

# 用户的用户名和密码
na = input("输入用户名：")
pw = input("输入密码：")

# 初始值
level = '0'
jinbi = '0'
jingyan = '0'
lscs = '0'
ycls = '0'

# 创建插入语句 (将用户密码及初始值都写入到对应的字段)
sql = "insert into zxz.sjbinfo(zname,zpwd,level,jinbi,jingyan,lscs,ycls) values(%s,%s,%s,%s,%s,%s,%s)" % (
na, pw, level, jinbi, jingyan, lscs, ycls)

# 尝试执行sql语句
try:
    cursor.execute(sql)  # 提交到我们的数据
    db.commit()
except:
    db.rollback()  # 如果报错的话，则回滚数据库
    print("连接数据库错误！！！")

# 查询用户数据
sql = 'select * from sjbinfo ;'

# 异常排查尝试
try:
    cursor.execute(sql)  # 执行sql语句
    results = cursor.fetchall()

    # 我们使用for循环，遍历拿去这个集合中的小集合
    for row in results:
        if na in row:
            userid = row[0]
            username = row[1]
            userpawd = row[2]
            level = row[3]
            jinbi = row[4]
            jingyan = row[5]
            lscs = row[6]
            print('用户ID', userid \
                  , '用户名', username \
                  , '密码', userpawd \
                  , '等级', level \
                  , '金币', jinbi \
                  , '经验', jingyan \
                  , '连胜', lscs)


except:
    print("连接错误")

# 关闭程序对数据库的链接
#db.close()