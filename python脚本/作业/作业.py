#第一题

#接收用户信息
test = input('请输入用户名，密码，地址，手机号，性别，年龄(以空格分割）')
test= test.split(' ')

#存储到字典
dic = {'username': test[0],
       'userpass': test[1],
       'address': test[2],
       'tel': test[3],
       'gender': test[4],
       'age': test[5]}

#输出给用户信息
print('您的用户名是:', dic['username'], '\n'
      '您的用户密码是:', dic['userpass'], '\n'
      '您的地址是:', dic['address'],'\n'
      '您的手机号是:', dic['tel'],'\n'
      '您的性别是:', dic['gender'],'\n'
      '您的年龄是:', dic['age'])

#第二题
#赋值0开头会报错，除非是字符串
listA = [2019, 12, 2]
listA.insert(3, dic)
listA.append('heihei')
print("您的地址是： " + listA[3]['address'])
