import urllib.request
import os


def url_open(url):
    # 添加浏览器头部伪装
    headers = {  # 设置浏览器头部，需要加上要访问的目标地址是谁和浏览器的头部信息
        'Referer': 'https://www.mzitu.com/',
        'GET': url,
        'Host': 'www.mzitu.com',
        'User-Agent': 'Mozilla /5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

    # 请求目标
    # 请求方式
    # 请求主机
    # headers头部

    # 添加为伪装头部
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read()  # 因为后续可能使用的并不一定是图片还是链接，所以在这里先读出来，需要转换格式的在去转换
    return html  # 返回


def get_page(url):
    html = url_open(url).decode('utf-8')  # 我们把要访问的链接地址交给模块url_open 去伪装一下头部，
    # 因为是链接地址，格式可能无法识别，所以设置编码格式为utf-8
    print(html)
    a = html.find('page-numbers current') + 22  # html拿到的是当前网页的详细代码，使用find去查找代码中的'page-numbers current'字符串
    b = html.find('<', a)  # 查找<为了截至a的位置，找到a的位置后在找到的b的位置截至
    print(html[a:b])  # 验证
    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('data-original=')

    while a != -1:
        b = html.find('.jpg', a, a + 255)  # 以什么类型的图片，从什么开始，到什么结束（一个网页的图片很少有超过255个的）
        if b != -1:
            img_addrs.append(html[a + 15:b + 4])
        else:
            b = a + 15

        a = html.find('data-original=', b)
    print(img_addrs[a:b])
    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


# 创建文件夹，前10页
def download_mm(folder='OOXX', pages=11):  # 调用主函数， 设定folder的默认值为00XX  pages的默认值为11
    os.mkdir(folder)  # 调用os模块 创建目录OOXX
    os.chdir(folder)  # 切换进ooxx目录进行操作
    # 上面是切换存放数据的目录位置

    url = 'https://www.mzitu.com/'  # 定义要访问的地址
    page_num = int(get_page(url))  # 将访问的地址交给 get_page处理并将得到的数值调整为整形

    for i in range(pages):
        page_num += i

        page_url = url + 'page/' + str(page_num) + '/'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__ == '__main__':
    download_mm()

