loadfile = open('userlist.txt', mode='rb')  # ֻ�����ļ�
list = loadfile.read().decode("utf-8")
result = list.split(' ')  # ���û��б���Ϣ�����б����