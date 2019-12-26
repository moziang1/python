```
# -*- coding: utf-8 -*-

"""
Created on 2019/8/20

@author: eln

@requirements: PyCharm 2017.2; Python 3.5.6 |Anaconda 4.1.1 (64-bit)

@decription: 用 Python 制作一个电子相册
"""
import os
import sys
import threading
import tkinter as tk
import time
from PIL import ImageTk, Image




resolution = (1200, 600)  # 分辨率
Path = r'普攻动作图\\'  # 相册路径

Interval = 0.1  # 播放间隔.单位:s
Index = 0  # 当前照片计数

title = "电子相册"  # 窗口标题


def getfiles():
    """获取图片文件名。"""
    files = os.listdir(Path) #获取目录图片
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):  #将检测不到这3种图片类型时清除
            files.remove(x)
    return files      #将有效的图片返回给files

#调用函数，获取指定目录下的所有图片
files = getfiles()

scaler = Image.ANTIALIAS  # 设定 ANTIALIAS ，即抗锯齿
root = tk.Tk()  # 创建窗口
root.title(title)  # 设置窗口标题

img_in = Image.open(Path + files[0])  # 加载第一张图片

w, h = img_in.size  # 获取图片大小
size_new = (int(w * resolution[1] / h), resolution[1])   #铺满提前设定好的显示大小

img_out = img_in.resize(size_new, scaler)  # 重新设置大小

img = ImageTk.PhotoImage(img_out)  # 用 PhotoImage 打开图片
panel = tk.Label(root, image=img)  # Label 自适应图片大小
panel.pack(side="bottom", fill="both", expand="yes")




def image_change():
    """自动切换图片。"""
    try:
        global Index

        a = 0
        time.sleep(1)
        #while True:

        for i, x in enumerate(files):
            # 判断文件是否存在
            if not os.path.isfile(Path + '%s' % x):
                break

            if i != Index:  # 跳过已播放的图片
                continue

            print('自动处理图片', x, Index)  # python 3.5
            # print(unicode('自动处理图片 %s %d' % (x, Index), "utf8", errors="ignore"))  # python 2.7.15
            img_in = Image.open(Path + '%s' % x)
            w, h = img_in.size
            size_new = (int(w * resolution[1] / h), resolution[1])
            img_out = img_in.resize(size_new, scaler)
            img2 = ImageTk.PhotoImage(img_out)
            panel.configure(image=img2)
            panel.image = img2
            Index += 1
            if Index >= len(files):
                Index = 0
            time.sleep(Interval)

    except Exception as e:
        print("Exception: %s " % e)
        sys.exit(1)



t = threading.Thread(target=image_change)  # 创建图片切换线程
# python 可以通过 threading module 来创建新的线程，然而在创建线程的线程（父线程）关闭之后，相应的子线程可能却没有关闭
# 需要把 setDaemon 函数放在 start 函数前面解决此问题

t.start()  # 启动线程
root.mainloop()  # 窗口循环

```

