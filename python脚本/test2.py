import requests as req
import re
import pprint as pp

heads = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.kuaidaili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1)'
}
ssn = req.Session()
ssn.headers = heads

ptn表 = re.compile(r'<div[^>]*?id="list".*?'
                  r'(<table[^>]*>.*?</table>)',
                  re.X | re.S)
ptn行 = re.compile(r'<tr[^>]*>.*?</tr>', re.S)
ptn格 = re.compile(r'<td[^>]*>(.*?)</td>', re.S)

url = "http://www.kuaidaili.com/free/inha/"
Proxys = [['IP', 'PORT', '类型', '响应速度', '最后验证时间']]
for i in range(1, 6):  # 抓取 5 页
    rsp = ssn.get(url + str(i))
    rsp.encodeing = 'utf-8'
    html = rsp.text
    表 = ptn表.findall(html)
    行 = ptn行.findall(表[0])
    for td in 行[1:]:
        td = ptn格.findall(td)
        td.pop(4)
        td.pop(2)
        Proxys.append(td)

pp.pprint(Proxys)
input('暂停')
