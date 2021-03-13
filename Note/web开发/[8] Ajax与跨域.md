## Ajax

#### 同步和异步

- 同步：必须等待前面的任务完成后，才能继续后面的任务。
- 异步：不受前面任务的影响。

#### 发送Ajax请求的步骤

- 创建异步对象`XMLHttpRequest`，测试浏览器的兼容性问题；
- 使用`open()`方法设置请求参数。`open（'请求的方法(get/post)'，'请求的url'，'是否异步(true/false)'）`；
- 发送请求；
- 注册`onreadystatechange`事件，当状态改变就会调用该方法；
- 获取返回的数据。

#### get请求

```javascript
//创建异步对象，测试浏览器兼容性
if (window.XMLHttpRequest){
   var xhr = new XMLHttpRequest();
}
else{
   var  xhr = new ActiveXObjet('Microsoft',XMLHttp);
}

//使用open方法设置参数
xhr.open('get',url);

//发送异步请求
xhr.send();

//注册onreadystatechange事件
xhr.onreadystatechange = function(){
    if(xhr.readyState == 4 && xhr.status == 200){
        //获取返回的内容，修改显示
        console.log('数据返回成功');
        console.log(xhr.responseText);
    }
}
```

#### post请求

```javascript
//创建异步对象，测试浏览器兼容性
if (window.XMLHttpRequest){
   var xhr = new XMLHttpRequest;
}
else{
   var xhr = new ActiveXObjet('Microsoft',XMLHttp);
}

//使用open方法设置参数
xhr.open('post',url);

//使用open方法必须添加HTTP头
xhr.setRequestHeader('"Content-type", "application/x-www-form-urlencoded"')

//发送异步请求,send方法中传入想要发送的数据
xhr.send('username=xxx&age=25');

//注册onreadystatechange事件
xhr.onreadystatechange = function(){
    if(xhr.readyState == 4 && xhr.status == 200){
        //获取返回的内容，修改显示
        console.log('数据返回成功');
        console.log(xhr.responseText);
    }
}
```

#### `onreadystatechange`事件

 注册 `onreadystatechange` 事件后，每当 `readyState` 属性改变时，就会调用 `onreadystatechange` 函数。 

`readyState`:

- 0：请求未初始化；
- 1：服务器连接已建立；
- 2：请求已接受；
- 3：请求处理中；
- 4：请求已完成，且响应就绪。

`status`：

- 200：ok；
- 404：未找到页面。

#### ajax请求解析xml

`get_xml.php`(包含`star.xml`文件):

```php
<?php
    //设置返回的为xml
   header('content-type:text/xml;charest：utf-8') ；
    
    //读取xml并返回 php自带了一个file_get_content读取xml的方法
    echo file_get_content(info/star.xml)
?>   
```

`get_xml.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<input type="button" value="获取xml" id="getxml">
</body>
    
<script>
    document.getElementById("getxml").onclick = function(){
        var xhr = new XMLHttpRequest();
        xhr.open('get','getxml.php');
        xhr.send();
        xhr.onreadystatechange=function(){
            if(xhr.readyState == 4 && xhr.status == 200){
                console.log(xhr.responseText);
			   console.log(ajax.responseXML);
			   console.log(ajax.responseXML.querySelector('kuzi').innerHTML);
			   console.log(window.document);
            }
        }
    }
</script>
</html>
```

#### ajax请求解析json

`student.json`:

```json
{
    'name':'zhangsan',
    'age':20,
    'sex':'male'
}
```

`get_json.php`:

```php
<?php
    //读取json并返回 
    echo file_get_content(info/student.json)
?>   
```

`get_json.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<input type="button" value="获取json" id="getjson">
</body>
    
<script>
    document.getElementById("getjson").onclick=function(){
        var xhr = new XMLHttpRequest();
        xhr.open('get','get_json.php');
        xhr.send();
        xhr.onreadystatechange=function(){
            if(xhr.readyState == 4 && xhr.status == 200){
          		console.log(xhr.responseText);
                //把json对象转化为js对象
                var jsObj= Json.parse(xhr.responseText);
                console.log(jsObj);
                //字符串拼接
                var str = '';
                str+='ul';
                str+='li'+jsObj.name+'li';
                str+='li'+jsObj.age+'li';
                str+='li'+jsObj.set+'li';
                //显示在页面上
                document.body.innerHTML=str;
            }
        }
    }
</script>
```

#### jQuery中的ajax

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<input type="button" value="点击" id="btn">
</body>
<script src='jquery-1.11.2.js'></script>
<script>
	$(function(){
        $("#btn").click(function(){
            $.ajax({
                type:'get',//请求的方式
                url:'hello.php',//请求地址
                datatype:'text',//数据类型
                success:function(argument){}//请求成功执行的方法
                error:function(argument){}//请求失败执行的方法
 				beforeSend:function (argument) {},// 在发送请求之前调用,可以做一些验证之类的处理
            })
    	}
       }
    })
</script>
```

#### 将get和post请求进行封装

`ajax_tool.js`:

```javascript
function ajax_tool(method,url,data,success){
    var xhr= new XMLHttpRequest();
    if (method == 'get'){ 
        if(data){  //如果有值，进行字符串拼接，get发送数据的格式是xxx.php?username=18;
            url+='?；
       	    url+=data;
        }
        xhr.open('get',url);
        xhr.send();
    }
    else{
        //post的url不需要修改
        xhr.open('post',url);
        xhr.setRequestHeader('Content-type',"application/x-www-form-urlencoded");
        if(data){
            xhr.send(data);
        }else
        {
            xhr.send();
        }
    }
    
    //注册onreadystatechange事件
    xhr.onreadystatechange=function(){
        if(xhr.readyState == 4 &&xhr.status ==200){
            success(xhr.responseText);//success是传入的方法，数据是里面的，那么数据由此传递到外面
        }
    }
}
```

`test_get.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<input type="button" value="点击" id="btn">
</body>
<!--导入封装的ajax_tool.js-->
<script src='ajax_tool.js'></script>
<script>
    document.getElementById("btn").onclick=function(){
        var test=ajax.tool('get','test_get.php','name=zhangsan&skill=code',function(data){
            console.log(data);
        });
        console.log(test);
    }
</script>
```



## 同源与跨域

同源策略：是浏览器的一种安全策略，同源指的是同协议、同域名、同端口号。

### JSONP

`jsonp`：带有补丁的`json`，动态插入`<script>`标签，利用`<script src=""></script>`标签的可跨域性，由服务器返回一个预先定义好的`JS`函数的调用，并将服务器数据以该函数参数的形式传递过来。

**`jsonp`只能以`get`方式请求**

1. A客户端代码

```php+HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	
</body>
</html>
<script>
	function fn(data){
        console.log(data);
    }
</script>
//利用script标签发送了一个get请求到了01.php中
//A客户端请求的是B服务器上的01.php页面
//callback1是A与B之间的约定，约定后将执行fn
<script type="text/javascript" src="http://192.168.141.137/01.php?callback1=fn"></script>
```

2. B服务器端代码

```php
<?php
    $callback=$_GET['callback1'];//callback1是A与B的约定

	$arr = array ['zhangsan','lisi','wangwu']
	//echo输出的内容即是返回给客户端A的内容，保存在A中的data中
	//json_encode方法是将php对象转为json对象
    echo $ncallback.`(`.json_encode($arr).`)`
?>
```

3. A中的输出结果

```
mycallBack("zhangsan","lisi","wangwu")
```

### 常见的跨域技术

- `jsonp`动态插入`script`标签
- `H5`中新的`API` `window.postMessage`，多窗口及`IFrame`
- `CORS`(跨域资源共享)发送`ajax`请求
- `img`的`src`属性
- `iframe`框架