## python链接数据库

数据库授权，python安装pyMysql模块

```
grant all on *.* to 'root'@'%' identified by '123.com';
```

防火墙放行

```
firewall-cmd --permanent --add-port=3306/udp
firewall-cmd --permanent --add-port=3306/tcp
```



#python链接数据库格式

```python
变量名=pymysql.connect(host='数据库服务器地址',port=3306
					,user='数据库用户名'
					,passwd='数据库密码'
					,charset='编码格式')
```



### 使用格式

```python
import pymysql

#创建数据库链接
db=pymysql.connect(host='192.168.1.1'
                   ,port=3306,user='root'
                   ,passwd='123.com'
                   ,charset='utf8')


#创建指针，指针用来对是菊科进行详细操作
#使用cursor()方法
cursor=db.cursor()

#对指针设定的具体操作，使用了方法execute()括号内里写的是
#具体的sql语句，这里写的selectl version()是查看数据库版本的方法
cursor.execute('select version()')

#fetchone()这个方法用来获取指针操作后返回的单条的结果
data=cursor.fetchone()

#打印结果data (#  %s,表示格式化字符串，把字符串转换为字符
#案例

#如果不格式化，那么data就为一个字符串形式的数字，
#如database version:('data',)

#,在这里使用格式化对象为字符，
#那么输出就是database version: 5.6.36)

print('database version: %s' % data)

#关闭与数据库的链接
db.close
```







### 数据库的增删改查

```
insert插入（对数据库内容的增加）

delete删除（对数据库内容的删除）

update更新（对数据库内容的更新）

select 选择（对数据库内容的选择）
```

## #增操作-插入insert  

#前情提要

```mysql
#创建数据库
create database zxz;

#切换至数据库zxz
use zxz

#创建一个表
create table zuser( zid int(4) auto_increment primary key, zname varchar(20) not null unique,  zpwd varchar(20) not null);
```

编辑代码

```python
import pymysql

#创建数据库链接
db=pymysql.connect(host='192.168.1.1',port=3306,
                     user='root',
                     passwd='123.com',
                     charset='utf8',db='zxz')
                     
#应用数据库连接
cursor=db.cursor()

#用户的用户名和密码
na=input("输入用户名：")
pw=input("输入密码：")

#创建插入语句 这里后面使用"""+na+""" 3引号只是为了保证它是作为一个变量使用
#sql="""insert into zxz.zuser(zname,zpwd)values('"""+na+"""','"""+pw+"""')"""

#但是上面的方法"很多，导致很容易报错，我们可以使用格式解决
sql="insert into zxz.zuser(zname,zpwd) values(%s,%s)" % (na,pw)

#尝试执行sql语句
try:
    cursor.execute(sql)  #提交到我们的数据
    db.commit()
except:
    db.rollback()  #如果报错的话，则回滚数据库
    print("连接数据库错误！！！")
```

查询表

```mysql
show tables;
select * from zuser;
```





## #查询语句select

```python
import pymysql

# 创建数据库链接
db = pymysql.connect(host='192.168.1.1', port=3306,
                       user='root',
                       passwd='123.com',
                       charset='utf8', db='zxz')

# 应用数据库连接
cursor = db.cursor()
sql = 'select * from zuser;'


# 异常排查尝试
try:
    cursor.execute(sql)  # 执行sql语句
    results = cursor.fetchall()
    # 这里使用查询多条语句 fetchall()
    # 它查询的结果不一定只是一条，它得到的值可能是如下类型
    #((1, '123', '123'), (2, 'haha', '123.com'))  是一个嵌套集合

    #我们使用for循环，遍历拿去这个集合中的小集合
    for row in results:
        userid = row[0]
        username = row[1]
        userpawd = row[2]
        print('用户ID',userid,'用户名称',username,'用户密码',userpawd)


except:
    print("连接错误")

#关闭数据库连接
db.close()
```



### 小练习： 在数据库中创建一个表 sjbinfo

#该表字段如下：

```
#用户名-密码-等级-金币-经验，连胜次数-隐藏连胜

#尝试让用户注册账户，当用户注册后，使用用户注册的名称和密码，

#以及默认0等级-0经验-0金币-0连胜。  向表内插入一条数据

#插入成功的话，通过查询将插入后的数据表中的所有内容显示出来

#显示过程，应该将每一个字段拆分开显示，用户名：xxx 密码: xxx
```





```python
import pymysql

# 创建数据库链接
db = pymysql.connect(host='192.168.1.1', port=3306,
                     user='root',
                     passwd='123.com',
                     charset='utf8', db='zxz')


# 应用数据库连接
cursor = db.cursor()

# 在zxz库中创建表（存储用户信息）                                 
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
db.close()
```

