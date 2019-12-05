import sys
import os

# 打开文件
filename = input('请输入文件的完整路径:')
try:
    f = open(filename)
    filewords = f.read()
except FileNotFoundError:
    print('打不开%s' % filename)
    sys.exit()

# 输入替换的内容
old_words = input('请输入要替换的内容:')
if old_words not in filewords:
    print('%s文件里没有%s' % (os.path.basename(filename), old_words))
    sys.exit()

# 输入替换成的内容
new_words = input('请输入替换成的内容:')

with open(filename, 'w') as f:
    f.write(filewords.replace(old_words, new_words))
