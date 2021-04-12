### Django中的MVT

1. Model：模型，负责与数据库的交互。
2. View：视图，负责接收请求，处理业务逻辑，返回结果。
3. Template：模板，负责前端页面的封装。

<details>
<summary>📌&nbsp;&nbsp;思维导图</summary>
</br>

![MVT](/Note/Django/res/MVT.png)
</details>

## Model

<details>
<summary>📌&nbsp;&nbsp;思维导图</summary>
</br>

![Model](/Note/Django/res/Model.png)
</details>

## VIEW

<details>
<summary>📌&nbsp;&nbsp;思维导图</summary>
</br>

![View](/Note/Django/res/View.png)
</details>

## Template

<details>
<summary>📌&nbsp;&nbsp;思维导图</summary>
</br>

![Template](/Note/Django/res/Template.png)
</details>

### 视图：

- 接收请求
  1.学习如何从请求中获取对我们(服务器)有用的数据
  2.请求地址：http://127.0.0.1:8000/10/100/
  1.2.1 使用正则表达式的组提取
  		位置参数：url(r'(\d+)/(\d+)/')
  		视图函数：def test(request, num1, num2)
  		注意：正则的组的顺序对应函数的参数顺序（request除外）

关键字参数：url(r'(?P<num1>\d+)/(?P<num2>\d+)/')
			视图函数：def test(request, num1, num2)
			注意：正则的关键字需要和视图函数的参数保持一致（request除外）
	

1.3 请求报文信息：request = HttpRequest()
		path = request.path (path == /10/100/)>(此方法实现太过复杂)
	
1.3.1 请求地址：http://127.0.0.1:8000/10/100/?a=10&b=20
			GET属性：专注于获取查询字符串，跟请求方法没有关系
			GET属性返回值：QueryDict类型的对象，类似于python的字典而已
			GET属性取查询字符串：query_dict = request.GET
			GET属性当中获取查询字符串的具体信息：
				query_dict.get('key') : 一键一值
				query_dict.getlist('key') : 一键多值
	
1.3.2 如果要获取的信息在请求体（表单）中：发送的是POST请求
			POST属性：专注于获取请求体（表单）
			POST属性返回值：QueryDict类型的对象，类似于python的字典而已
			POST属性取请求体（表单）：query_dict = request.POST
			POST属性当中获取请求体（表单）的具体信息：
				query_dict.get('key') : 一键一值
				query_dict.getlist('key') : 一键多值

2.处理逻辑

3.响应结果
3.1 学习如何响应结果给客户端，具体的需要学习什么时候响应什么数据给客户端
3.2 相关的类
HttpResponse()   		
父类   
响应字符串,普通字符串，html格式的字符串
Content-Type : text/html
		
JsonResponse()
子类
响应JSON数据的，经常跟ajax做交互的，因为ajax只认得json
Content-Type : application/json

HttpResponseRedirect('/path/')  
子类
当服务器处理完某种逻辑，不需要用户点击界面，即可把该响应交给浏览器，浏览器收到该响应，读取响应当中的地址信息，最后跳转到响应当中的地址。
比如：登陆成功之后，跳转到网站的主页
提示：点击登录按钮的本质，不是跳转界面，是将登陆表单信息发送给服务器，服务器处理登陆成功，响应重定向给浏览器，浏览器自动跳转页面
提示: window.locatin=''  <a href=''> 都可以打开新的界面，但是他们需要用户手动的触发事件
render(‘模板’) 也是属于响应的一种，但是，他是一个函数，返回HttpResponse() 类型的对象