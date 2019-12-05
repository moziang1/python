import json
import random
import time
import hashlib
import requests
from tkinter import *
from tkinter.scrolledtext import *
# 导入模块时用import  json, random, time, hashlib, requests这样用逗号隔开，一行代码导入更方便

root = Tk()
root.title('有道翻译')
frame = Frame(root)
frame.pack(padx=10, pady=20)

req = Label(frame, text='请输入你要翻译的文字：', pady=10)
req.pack(anchor=W)

# 输入栏加入滚动条，方便超长文本的浏览
t1 = ScrolledText(frame, width = 70, height = 10)
t1.pack()
r = ''

def translate():
    # 如果你是自己写的翻译代码，你会明白这个global的作用的
    # 这个global折磨了我很久才决定最终还是把它加上，不加结果会完全不同
    global r
    inp = t1.get(1.0, END)
    inp_list = inp.splitlines()
    inp_text = [i for i in inp_list if i != '']
    e = '\n'.join(inp_text)
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
              'Cookie':'OUTFOX_SEARCH_USER_ID=1266238201@110.255.206.232',
              'Referer':'http://fanyi.youdao.com/?keyfrom=dict2.top'}
    client = 'fanyideskweb'
    ts = int(time.time()*1000)
    salt = str(ts * 10 + random.randint(1, 10))
    sign = hashlib.md5((client + e + salt + "@6f#X3=cCuncYssPsuRUE").encode('utf-8')).hexdigest()
    bv = '9d1e6a4f9d4241fb7947f623cc9e4efa'
    Form_Data={}
    Form_Data['i'] = e
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = client
    Form_Data['salt'] = salt
    Form_Data['sign'] = sign
    Form_Data['ts'] = ts
    Form_Data['bv'] = bv
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_CLICKBUTTION'
    '''
    长词典用下面这个办法更好看一些，代码量也能少一些
    Form_Date = {
        'i':e,
        'from':'AUTO',
        ...
        'action':'FY_BY_CLICKBUTTION'
    }
    '''
    translate_result = requests.request(method='POST', url=url, data=Form_Data, headers=headers).text
    result = json.loads(translate_result)
    translateresult = result['translateResult']
    r = ''
    for i in translateresult:
        r += i[0]['tgt'] + '\n'
    t2.configure(state=NORMAL)
    t2.delete(1.0, END)
    t2.insert(INSERT, r)
    t2.configure(state=DISABLED)

Button(frame, text='开始翻译', command=translate).pack(pady=10)

res = Label(frame, text='翻译结果：')
res.pack(anchor=W)
# 输出栏同样加入滚动条，方便超长文本的浏览
t2 = ScrolledText(frame, width=70, height=10, background='gainsboro')
t2.pack()


mainloop()