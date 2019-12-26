### flask 使用的前提条件--安装了专业版的pycharm



为爬虫做准备

```
file--- new --flask
```



实时显示页面元素

```python
from flask import Flask
#在flask库种导入了flask扩展类

#创建一个flask应用程序的实例，或者说实例化flask程序
app = Flask(__name__)
#在创建的过程种，需要传入__name__，它的作用是为了确定资源所在的位置

@app.route('/')
#定义路由以及视图函数（下面的方法就是视图函数)
#路由的定义是通过了装饰器@app的形式实现的
#当用户访问"/"所代表的页面的时候，就会在页面中显示下面视图函数中所要展现的内容

def hello_world():
	#在视图函数（定义我们能看到的内容的函数叫做视图函数）中
    #我们返回了一个hello world字符串
    #当这个函数被调用的时候，这个返回的内容会呈现在我们的页面上
    return 'Hello World!'

#启动程序
#这里我们主要运行该项目，只要执行下面的代码，就会运行一个小型的服务器
if __name__ == '__main__':
    app.run()
	#执行了app.run() 就会开始运行这个简易的服务器了
    #该服务器是由flask框架提供
```





```python
#当客户端想要获取到页面资源的时候，会通过浏览器发送http请求
#这个时候web服务器会把来自于客户端的请求都交给flask程序实例
#也就是我们刚才上面定义的app
#那么程序实例--》 app会使用到 werkzeug 来作为路由转发
#（辨别url请求和视图函数之间的对应关系）
#再根据每一个url的请求，找到对应的视图函数，并对其进行调用


#视图函数的作用：反馈指定的内容

#flask调用了视图函数之后，可以返回两种内容：
1，字符串内容： 将视图函数的返回值作为响应的内容返回给浏览器
2，html模板内容： 获取到数据之后，吧数据传入html模板文件当中
#模板引擎负责对这些数据进行处理，然后返回响应的数据给客户端

#如果要使用模板，一定要将html模板放在flask项目目录中的templates目录中(默认存在），并且需要从flask库中导入render_template

templates 存放html
static 图片视频音频

```



```python
路由如何增加请求方式的限定
默认情况下flask接收的是GET方式的请求
#那么如果我们想要让它也接收POST请求方法，怎么做？
那么就需要再装饰器设置路由的时候说明一下
@app.route(methods=GET/POST)
#需要注意的是GET和POST一定是大写的，如果你的编译器没有提示功能
#那么还要注意method后面有s结尾--methods
#默认情况下是支持的GET，如果需要增加POST或其他的方式方法，则需要自行指定，当你指定多个的时候，一定要写成列表形式
```







案例

```python
如何给路由传递参数
一般情况下我们web地址上，经常会出现如下的格式内容
127.0.0.1：5000/login/zxz
上面这种形式会再基础的域地址后跟上一些参数，比如上面示例中的zxz，这些参数数据最终要提交的到服务器进行处理
那么再处理这些请求的时候我们不可能单独为其指定一个新的路由
我们肯定希望不管提交的参数内容是什么，最终都交给同一个路由进行解析和处理
#那么我们下面就尝试使用一个视图函数来显示不同用户提交的参数信息
```

代码

```python
from flask import Flask
app =Flask(__name__)
@app.route('/')
def login():
    return "hahaha"
#这里我们添加一个路由方式
#这里的<>用来定义路由参数，再<>内需要给路由的参数起歌名字
@app.route('/login/<string:userid>')
#我们为第二个路由专门又写了一个函数
#这个函数当中需要接一个userid参，对应了路由当中的参数
#通俗的来讲，也就是当你浏览器地址栏上输入/login/参数这样的后缀时，我们就会调用下面的函数方法来处理

def get_userid(userid):
    #返回一个值，这个值就是从浏览器地址中接收到的参数
    #下面return中使用了格式化定义参数的方式
    #再字符串中使用%+字母定义了一个格式化的变量
    #再字符串后我们又用%加真正的变量名来对刚才的%字母进行赋值
    jyc=123
    return "用户编号：%s %g" %(userid,jyc)
if __name__ == '__main__':
    app.run()
```

访问

```
http://127.0.0.1:5000/login/test
```







```python
#之前我们一直再返回字符内容
#那么如何返回一个页面模板
#要知道，再左侧的项目框中，我们的flask项目中都会又两个文件夹
#1. static: 这个文件夹用来方页面中的各种静态资源，比如图片
#2. templates: 这个文件夹用来放置我们的html文件（模板）
#限制我们一起去这个目录中创建一个index.html的文件
#    可以再里面随便写点什么
#   然后我们需要再程序中导入 render_template

from flask import Flask,render_template
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def eiyouwei():
	return render_template('new.html')
if __name__ == 'main':
	app.run()
```



templates-->html file 创建一个html文件 new



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我的页面</title>
</head>
<body>

{#    div是一个块级元素（标签） 块级元素的特点是自己独占一行#}
{#    我们打开当前的页面，可能看不到任何的内容，为什么#}
{#    因为div默认的属性是透明的，我们可以把空的div看作一个空的塑料袋。#}
{#    再其中没有存放内容的时候，这个塑料袋是被压平的。 所以我们根本看不到}#}
{#    我们刚才向这个标签当中填充了内容abcdefg，但是再页面被允许后，只能看到我们写入其中的内容#}
{#    并不能看到这个标签到底长什么样子，那么想要看到它，需要通过标签的属性的设置#}
{#    比如设置该标签的颜色，使其不透明，设置标签的属性时#}
{#    可以使用两种方法，一种是古老的，直接再标签当中设置，一种叫做css层叠样式表，这种设定方式会写在页面的头部信息当中#}

    <div style="background-color:crimson">abcdefg</div>
    <div style="background-color:cornflowerblue">abcdefg</div>

</body>
</html>
```





### css层叠样式表

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我的页面</title>

{#    style标签，用来书写css样式或者js代码#}
{#    需要通过其中type属性来指明其中的代码类型#}
    <style type="text/css">
        .wjy{
            {#设置背景色#}
            background:dodgerblue;

            {#设置宽度，单位可以是px，也可以是em #}
            {#1em = 16px#}
            width: 600px;

            {#高度设置#}
            height:50px;

            {#设置标签中的内容垂直居中，行高#}
            line-height:50px;

            {#设置标签内文字内容的水平居中,#}
            text-align: center;

            {#设置字体大小#}
            font-size: 24px;
            {#字体颜色#}
            color:gold;
            font-family: '楷体';

            {#标签左浮动#}
            float: left;
        }


        {#呼唤idjingyang#}
        #jingyang{
            background: red;
            width: 700px;
            height:50px;
            {#为了保持和上一个div平行，也要进行左对齐#}
            float: left;
        }
        #zx{
            background: red;
            width: 700px;
            height:50px;
            {#为了保持和上一个div平行，也要进行左对齐#}
            float: left;



        }

    </style>

</head>
<body>

{#    可以使用两种方法，一种是古老的，直接再标签当中设置，一种叫做css层叠样式表，这种设定方式会写在页面的头部信息当中#}
{#想要使用css样式的形式设置标签的属性，需要给我们指定要设定样式的标签起个名字，起名字的方法又两种常见的方式，#}
{#一种是设置class，一种是设置id:  一个class名称可以给多个标签设置的  id名称是唯一的#}

    <div class="wjy">
            哈哈哈
    </div>

    <div id="jingyang">
            abcdefg

    </div>

    <div id="zx">
            abcdefg

    </div>

</body>
</html>
```



实验：

主程序

```python
#之前我们一直再返回字符内容
#那么如何返回一个页面模板
#要知道，再左侧的项目框中，我们的flask项目中都会又两个文件夹
#1. static: 这个文件夹用来方页面中的各种静态资源，比如图片
#2. templates: 这个文件夹用来放置我们的html文件（模板）
#限制我们一起去这个目录中创建一个index.html的文件
#    可以再里面随便写点什么
#   然后我们需要再程序中导入 render_template

from flask import Flask,render_template
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def eiyouwei():
	return render_template('moban.html')
if __name__ == 'main':
	app.run()
```

html主页文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我的页面</title>

{#    style标签，用来书写css样式或者js代码#}
{#    需要通过其中type属性来指明其中的代码类型#}
    <style type="text/css">
        .wjy{
            {#设置背景色#}
            background:dodgerblue;

            {#设置宽度，单位可以是px，也可以是em #}
            {#1em = 16px#}
            width: 304px;

            {#高度设置#}
            height:50px;

            {#设置标签中的内容垂直居中，行高#}
            line-height:50px;

            {#设置标签内文字内容的水平居中,#}
            text-align: center;

            {#设置字体大小#}
            font-size: 24px;
            {#字体颜色#}
            color:gold;
            font-family: '楷体';

            {#标签左浮动#}
            float: left;
        }


        {#呼唤idjingyang#}
        #jingyang{
            background: red;
            width: 304px;
            height:50px;
            {#为了保持和上一个div平行，也要进行左对齐#}
            float: left;
            {#设置标签中的内容垂直居中，行高#}
            line-height:50px;

            {#设置标签内文字内容的水平居中,#}
            text-align: center;
        }

        #zx{
            background: black;
            width: 304px;
            height:50px;
            {#为了保持和上一个div平行，也要进行左对齐#}
            float: left;
            {#设置标签中的内容垂直居中，行高#}
            line-height:50px;

            {#设置标签内文字内容的水平居中,#}
            text-align: center;
            {#设置字体大小#}
            font-size: 24px;
            {#字体颜色#}
            color:gold;
            font-family: '楷体';
        }

        #test1{
            background: brown;
            width: 304px;
            height:50px;
            {#为了保持和上一个div平行，也要进行左对齐#}
            float: left;
            {#设置标签中的内容垂直居中，行高#}
            line-height:50px;

            {#设置标签内文字内容的水平居中,#}
            text-align: center;
        }

        #test2{
            background: forestgreen;
            width: 304px;
            height:50px;
            {#为了保持和上一个div平行，也要进行左对齐#}
            float: left;
            {#设置标签中的内容垂直居中，行高#}
            line-height:50px;

            {#设置标签内文字内容的水平居中,#}
            text-align: center;
        }


    </style>

</head>
<body>

{#    可以使用两种方法，一种是古老的，直接再标签当中设置，一种叫做css层叠样式表，这种设定方式会写在页面的头部信息当中#}
{#想要使用css样式的形式设置标签的属性，需要给我们指定要设定样式的标签起个名字，起名字的方法又两种常见的方式，#}
{#一种是设置class，一种是设置id:  一个class名称可以给多个标签设置的  id名称是唯一的#}

    <div class="wjy">
            哈哈哈
    </div>

    <div id="jingyang">
            abcdefg

    </div>

    <div id="zx">
            abcdefg
    </div>

    <div id="test1">
            abcdefg
    </div>

    <div id="test2">
            abcdefg
    </div>



</body>
</html>
```

