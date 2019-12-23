## tkinter常用命令

### 1.开启底层窗口

```python
import tkinter as tk     #as别名，tk
win.tk.Tk()         #实例化，相当于我们使用calss类的实例化

win.mainloop()       #保证屏幕的刷新，屏幕是由一帧一帧组成，它的作用就循环这些帧，保证页面一直进行刷新，所以它的后面不能执行命令。一般是放到程序的结尾
```

效果图

![image-20191216133658832](image/image-20191216133658832.png)



### 2.设置窗口名称，并设置窗口的大小以及是否可以缩放

```python
import tkinter as tk
win=tk.Tk()

win.title('haha')     #窗口起名
win.geometry('800x600')   #800x600像素大小
win.resizable(0,0)
# 0代表不允许缩放，x轴和y轴，任何非0 的数字都代表可以缩放。 
#如: (0,1)  y轴可缩放
#如: (1,0) x轴可缩放

win.mainloop()       
```

效果图

![image-20191218133024815](image/image-20191218133024815.png)







### 3.给底层界面添加元素

#### 1. Label函数（标签） 显示文本输入

```python
import tkinter as tk
win=tk.Tk()
win.title('haha')     
win.geometry('800x600')   
win.resizable(0,0)

#这里先写一个Label标签，
lab = tk.Label(win ,text='欢迎使用' ,bg='black' ,fg='gold')

#win  这里是说明我们创建的标签是基于我们底层窗口win创建的，包含在win的窗口中
#text  标签要写的文本内容
#bg    标签的背景颜色
#fg    文本的字体颜色

lab.pack()    #简单来说就是把我们上面定义的标签显示出来

#但是我们经常需要将显示出来的标签清除，去显示新的东西
#lab.pack_forget()  

#所以就会用到，清除标签的功能,现在因为是显示和清除放到了一起，所以，上面的就不会显示，一般我们使用的时候是达成某条件的情况下去使用



win.mainloop()       
```

![image-20191218133009191](image/image-20191218133009191.png)





#### 2. Entry()函数   以交互式显示一个输入框

```python
import tkinter as tk
win =tk.Tk()
win.title('haha')
win.geometry('800x600')
win.resizable(0 ,0)


#定义Entry元素
Ent = tk.Entry(win,text='快来填满我')
Ent.pack()   #显示

#注意! 元素的放置顺序，决定了该元素的放置位置
#如下所示的Entry()元素因为在放置Lable之前被放置了，所以图形化上显示出来，它也是在Label元素上面的
#另外，我们应该发现，在该界面当中，每一个元素都自己独占了一行内容(默认)



win.mainloop()       
```

####   效果图

![image-20191218132834636](image/image-20191218132834636.png)





#### 4.将白色背景图片的背景改为透明色，方便插入图片后不影响背景

```python
# coding=utf-8
# matplotlib背景透明示例图
# python 3.5

import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import scipy.stats as stats

# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        # 设置标注文字及位置
        ax.text(rect.get_x() + rect.get_width() / 2, 0.03 + height, '%.4f' % height, ha='center', va='bottom')

    # 数据


testData = [[0.87, 0.40, 0.56],
            [0.97, 0.50, 0.33],
            [0.88, 0.30, 0.44],
            [0.25, 0.23, 0.17],
            [0.73, 0.33, 0.45]]

N = 3
width = 0.5
ind = np.arange(width, width * 6 * N, width * 6)

fig, ax = plt.subplots()
rectsTest1 = ax.bar(ind, (testData[0][0], testData[0][1], testData[0][2]), width, color=(0, 0, 1, 1),
                    edgecolor=(0, 0, 1, 1))

rectsTest2 = ax.bar(ind + width, (testData[1][0], testData[1][1], testData[1][2]), width, color=(1, 0, 0, 1),
                    edgecolor=(1, 0, 0, 1))

rectsTest3 = ax.bar(ind + 2 * width, (testData[2][0], testData[2][1], testData[2][2]), width, color=(0, 1, 0, 1),
                    edgecolor=(0, 1, 0, 1))

rectsTest4 = ax.bar(ind + 3 * width, (testData[3][0], testData[3][1], testData[3][2]), width, color=(1, 0.6471, 0, 1),
                    edgecolor=(1, 0.6471, 0, 1))

rectsTest5 = ax.bar(ind + 4 * width, (testData[4][0], testData[4][1], testData[4][2]), width,
                    color=(0.5804, 0, 0.8275, 1), edgecolor=(0.5804, 0, 0.8275, 1))

ax.set_xlim(0, 9.5)
ax.set_ylim(0, 1.4)
ax.set_ylabel('数值')
ax.yaxis.grid(True)
ax.set_xticks(ind + width * 2.5)
ax.set_xticklabels(('P', 'R', 'F'))

# 设置图例
legend = ax.legend((rectsTest1, rectsTest2, rectsTest3, rectsTest4, rectsTest5),
                   ('test1', 'test2', 'test3', 'test4', 'test5'))
frame = legend.get_frame()
frame.set_alpha(1)
frame.set_facecolor('none')  # 设置图例legend背景透明

# 给每个数据矩形标注数值
autolabel(rectsTest1)
autolabel(rectsTest2)
autolabel(rectsTest3)
autolabel(rectsTest4)
autolabel(rectsTest5)


#在这里修改要将背景白框改为透明的图片
plt.savefig('img\logs.png', format='png', bbox_inches='tight', transparent=True,
            dpi=600)  # bbox_inches='tight' 图片边界空白紧致, 背景透明
```





## 5. 加载动态图



```python
#首先引入pyglet包

import pyglet

#主方法源码：

# 在工作目录中选择一个gif动画文件

ag_file = "11.gif"

animation = pyglet.resource.animation(ag_file)

sprite = pyglet.sprite.Sprite(animation)

# 创建一个窗口并将其设置为图像大小

win = pyglet.window.Window(width=sprite.width, height=sprite.height)

# 设置窗口背景颜色 = r, g, b, alpha

# 每个值从 0.0 到 1.0

green = 0, 1, 0, 1      #不知道，不故宫应该是显示帧的

pyglet.gl.glClearColor(*green)

@win.event

def on_draw():

    win.clear()

    sprite.draw()

pyglet.app.run()
```



## 6  加载视频，不过没声音

```python
import numpy as np
import cv2

cap = cv2.VideoCapture('b.mpg')

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

```

