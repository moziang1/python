aa=open('userlist.txt',mode='rb')
result=aa.read().decode("utf-8")
list = result.split(' ')
print(list)