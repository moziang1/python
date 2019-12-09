import urllib.request

url = 'http://www.whatismyip.com.tw'

proxy_support = urllib.request.ProxyHandler({'http':'118.24.172.149:1080'})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')]

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)