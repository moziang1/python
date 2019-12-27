关于俄罗斯方块的代码

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



html代码



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我的页面</title>

{#    style标签，用来书写css样式或者js代码#}
{#    需要通过其中type属性来指明其中的代码类型#}
    <style type="text/css">

        {#定位黑色背景板，作为整体框架的背景，不浮动#}
        .bigmon{
            {#设置背景色#}
            background:black;

            {#设置宽度，单位可以是px，也可以是em #}
            {#1em = 16px#}
            width: 80%;

            {#高度设置#}
            height:400px;

        }

        {#定义3个区域占地90%（一个占30） 用于构建页面主体框架#}
        .sma110ne{
            width: 30%;
            height: 400px;
            {#background: seagreen;#}
            {#上面这个是代表3个框框的颜色#}
            float: left;

        }

        {#两个区域占总面积10%，(一个5%) ，用于形象分割上面的3个主体区域#}
        .jiange{
            width: 5%;
            height: 400px;
            {#background: antiquewhite;#}
            {#上面这个上述代表中间两条杠杠的颜色#}
            float: left;
        }


        {##################定义3个主体区域的大小###########################}
        .kj1{
            width: 200px;
            height: 200px;
            {#background: red;#}
            margin: 0 auto;
            margin-top: 100px;
        }

        .kj2{
            width: 300px;
            height: 200px;
            {#background: red;#}
            margin: 0 auto;
            margin-top: 100px;
        }

        .kj3{
            width: 200px;
            height: 300px;
            {#background: red;#}
            margin: 0 auto;
            margin-top: 50px;
        }


        {############################定义第一个主体区域的4个小元素数据（正方形）#################################}
        .kj1-1{
            width: 100px;
            height: 100px;
            background: red;
            float: left;
        }
        .kj1-2{
            width: 100px;
            height: 100px;
            background: dodgerblue;
            float: left;
        }
        .kj1-3{
            width: 100px;
            height: 100px;
            background: antiquewhite;
            float: left;
        }
        .kj1-4{
            width: 100px;
            height: 100px;
            background: brown;
            float: left;
        }

        {###################################定义第二个主体的4个小元素数据######################################}
        .kj2-1{
            width: 100px;
            height: 100px;
            background: aqua;
            {##float: left;#}
            margin: 0 auto;
            {###居中#}
        }
        .kj2-2{
            width: 100px;
            height: 100px;
            background: dodgerblue;
            float: left;
        }
        .kj2-3{
            width: 100px;
            height: 100px;
            background: antiquewhite;
            float: left;
        }
        .kj2-4{
            width: 100px;
            height: 100px;
            background: brown;
            float: left;
        }

        {###################################定义第三个主体的4个小元素数据######################################}

        .kj3-1{
            width: 100px;
            height: 100px;
            background: aqua;
            #float: left;

        }
        .kj3-2{
            width: 100px;
            height: 100px;
            background: dodgerblue;
            float: left;
        }
        .kj3-3{
            width: 100px;
            height: 100px;
            background: antiquewhite;
            float: left;
        }
        .kj3-4{

            width: 100px;
            height: 100px;
            background: brown;
            float: left;
        }


    </style>

</head>
<body>

{#    #定义背景板，随大小自调整#}
    <div class="bigmon">

{#    定义主体区域一#}
    <div class="sma110ne">
        <div class="kj1">
            <div class="kj1-1"></div>
            <div class="kj1-2"></div>
            <div class="kj1-3"></div>
            <div class="kj1-4"></div>
        </div>
    </div>

{#    分割两个主体区域#}
    <div class="jiange"></div>

{#    定义主体区域二#}
    <div class="sma110ne">
        <div class="kj2">
            <div class="kj2-1"></div>
            <div class="kj2-2"></div>
            <div class="kj2-3"></div>
            <div class="kj2-4"></div>
        </div>
    </div>

{#   分割两个主体区域#}
    <div class="jiange"></div>

{#    定义主体区域三#}
    <div class="sma110ne">
                <div class="kj3">
                    <div class="kj3-1"></div>
                    <div class="kj3-2"></div>
                    <div class="kj3-3"></div>
                    <div class="kj3-4"></div>
                </div>
    </div>


{#    #以上所有内容都是包含在class bigmon中的，所以在这里包含#}
    </div>


</body>
</html>
```







实验二

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我的页面</title>

{#    style标签，用来书写css样式或者js代码#}
{#    需要通过其中type属性来指明其中的代码类型#}
    <style type="text/css">

        {#定位黑色背景板，作为整体框架的背景，不浮动#}
        .bigmon{
            {#设置背景色#}
            background:black;

            width: 50%;

            {#高度设置#}
            height:400px;
            margin: 0 auto;

        }

        {#定义3个区域占地90%（一个占30） 用于构建页面主体框架#}
        .sma110ne{
            width: 19%;
            height: 400px;
            background: seagreen;
            {#上面这个是代表3个框框的颜色#}
            float: left;

        }

        {#两个区域占总面积10%，(一个5%) ，用于形象分割上面的3个主体区域#}
        .jiange{
            width: 8%;
            height: 400px;
            background: antiquewhite;
            {#上面这个上述代表中间两条杠杠的颜色#}
            float: left;
        }


        {##################定义3个主体区域的大小###########################}
        .kj1{
            width: 20px;
            height: 20px;
            margin: 0 auto;
            margin-top: 100px;
        }

        .kj2{
            width: 30px;
            height: 20px;
            margin: 0 auto;
            margin-top: 100px;
        }

        .kj3{
            width: 20px;
            height: 30px;
            margin: 0 auto;
            margin-top: 50px;
        }

        .kj4{
            width: 20px;
            height: 30px;
            margin: 0 auto;
            margin-top: 50px;
        }


    </style>

</head>
<body>

{#    #定义背景板，随大小自调整#}
    <div class="bigmon">

{#    定义主体区域一#}
    <div class="sma110ne">
        <div class="kj1">图片</div>
    </div>


{#    分割两个主体区域#}
    <div class="jiange"></div>

{#    定义主体区域二#}
    <div class="sma110ne">
        <div class="kj2">图片</div>
    </div>

{#   分割两个主体区域#}
    <div class="jiange"></div>



{#    定义主体区域三#}
    <div class="sma110ne">
                <div class="kj3"> 图片</div>
    </div>
    <div class="jiange"></div>


{#    定义主体区域寺#}
    <div class="sma110ne">
        <div class="kj4"> 图片</div>
    </div>


{#    #以上所有内容都是包含在class bigmon中的，所以在这里包含#}
    </div>


</body>
</html>
```

