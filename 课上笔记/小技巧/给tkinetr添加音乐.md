```python
from tkinter import *

win = Tk()
win.title('haha')

import winsound
	#开始第一首音乐的播放
def s11():
    global ppp
    #播放音乐
    ppp = winsound.PlaySound(r"test.wav", winsound.SND_LOOP|winsound.SND_ASYNC)

	#切换到第二首音乐
def s12():
    global ppp
    winsound.PlaySound(ppp,winsound.SND_PURGE)  #关闭上一首音乐
    ppp = winsound.PlaySound(r"123.wav", winsound.SND_LOOP|winsound.SND_ASYNC)  #声音的循环播放winsound.SND_LOOP

    
    #停止正在播放的音乐
def s13():
    global ppp
    winsound.PlaySound(ppp,winsound.SND_PURGE)



#一个变量，放着就好
ppp = winsound.PlaySound(None,winsound.SND_NODEFAULT)




#开始音乐
b2 = Button(win, text = 'Play',  width = 8, command = s11)
b2.place(x=10,y=10)

#切换歌曲
c2 = Button(win, text = '切歌',  width = 8, command = s12)
c2.place(x=50,y=50)

#停止音乐
c3 = Button(win, text = '停歌',  width = 8, command = s13)
c3.place(x=80,y=80)


win.mainloop()
```

