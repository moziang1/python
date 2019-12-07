loadfile = open('userlist.txt', mode='rb')  # 只读打开文件
list = loadfile.read().decode("utf-8")
result = list.split(' ')  # 将用户列表信息做成列表存在