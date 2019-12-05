import urllib.request
import urllib.parse  # parse现在不属于request的范围的模块了，所以要单独添加
import json


while True:
    temp = input('您是否开始翻译')
    haha = input('输入你想要翻译的单词或语句：')
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

    html = response.read().decode('utf-8')  # .read()得到的是一个utf-8的编码形式的文件，  .decode('utf-8')就是将其他编码形式的文件更改为（utf-8的编码格式)，相当于，把.read()的编码文件，解码成一个utf-8的解码格式

    target = json.loads(html)  # 找到对应的键,因为有两次列表，所以用[0][0]，"tgt"是列表中的键，调用键，就可以得到值

    print(target['translateResult'][0][0]["tgt"])#找到对应的键,因为有两次列表，所以用[0][0]，"tgt"是列表中的键，调用键，就可以得到值
