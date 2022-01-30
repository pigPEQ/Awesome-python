## Sass快速入门笔记

`sass`是一个开源的`CSS`预处理器，是`CSS`的超集，是更稳定和强大的`CSS`拓展语言，有助于减少`CSS`的重复，节省时间。

### 变量声明（$）

```scss
$color:blue;
#title:{
    fontSize:20px;
    color:$color;
}
```

编译之后：

```css
#title{
	fontSize:20px;
	color:blue;
}
```

### CSS嵌套

```scss
#container{
    padding:0 20;
    header{
        h1 { color: #333 }
    	p { margin-bottom: 1.4em }
    }
    mid,footer{
        fontSize:30px;
    }  
}
```

编译之后：

```css
#container {padding：0 20}
#container header h1 { color:#333 }
#container header p { margin-bottom:1.4em }
#container mid { fontSize:30px }
#container footer { fontSize:45px }
```

### 属性嵌套

```scss
#container{
	border:{ //属性之后添加冒号
	color:#000;
	style:solid;
	width:2px;
	}
}
```

编译之后：

```css
#container{
border-color:#000;
border-style:solid;
border-width:2px;
}
```

### 父选择器标识（&）

```scss
article a {
  color: blue;
  &:hover { color: red }
}
```

编译之后：

```css
article a {color： blue；}
article a：hover{color： red；}
```

### 导入Sass文件（@import）

- `css`有一个特别不常用的特性，即`@import`规则，它允许在一个`css`文件中导入其他`css`文件。然而，后果是只有执行到`@import`时，浏览器才会去下载其他`css`文件，这导致页面加载起来特别慢。

- `sass`也有一个`@import`规则，但不同的是，`sass`的`@import`规则在生成`css`文件时就把相关文件导入进来。

##### 导入局部文件

```scss
@import "themes/night-sky"             //局部文件的文件名以下划线开头，导入一个局部文件时可以不写文件全名，即省略下划线
```

##### 默认变量值（!default)

```scss
$fancybox-width: 400px !default;
.fancybox {
width: $fancybox-width;
}
```

##### 嵌套导入

局部文件`_blue-theme.scss`

```scss
aside {
  background: blue;
  color: white;
}
```

将局部文件导入`CSS`

```scss
.blue-theme{@import "blue-theme"}
//编译之后：
.blue-theme{
	aside {
  		background: blue;
  		color: white;
	}		
}
```

##### 原生`CSS`导入

 下列三种情况下会生成原生的`CSS@import`，尽管这会造成浏览器解析`css`时的额外下载： 

- 被导入文件的名字以`.css`结尾；
- 被导入文件的名字是一个URL地址（比如http://www.sass.hk/css/css.css），由此可用谷歌字体API提供的相应服务；
- 被导入文件的名字是`CSS`的`url()`值。

### 静默注释

该注释不会出现在生成的`css`文件中，语法同类c语言的注释一样，使用双斜杠（//）开头，注释内容直到行末。  

实际上`css`的标注注释（/* */）有时也会在生成的`css`文件中抹去，即标准注释出现在了原生`css`不允许的地方，比如`css`属性或选择器中， `sass`将不知如何将其生成到对应`css`文件中的相应位置，于是这些注释被抹掉。 

### 混合器（`@mixin`）

```scss
@mixin rounded-corners {
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  border-radius: 5px;
}
```

调用混合器`rounded-corners`

```scss
.test{
	fontSize：20px；
	background-color：green；
	@include rounded-corners;
}
编译之后：
.test{
	fontSize：20px；
	background-color：green；
	-moz-border-radius: 5px;
  	-webkit-border-radius: 5px;
  	border-radius: 5px;
}
```

 **语义化的类名亦可以帮你避免重复使用混合器** 

##### 混合器中的`CSS`规则

```scss
@mixin no-bullets {
  list-style: none;
  li {
    list-style-image: none;
    list-style-type: none;
    margin-left: 0px;
  }
}
```

```css
ul.plain {
  color: #444;
  @include no-bullets;
}
//编译之后：
ul.plain {
  color: #444;
  list-style: none;
}
ul.plain li {
  list-style-image: none;
  list-style-type: none;
  margin-left: 0px;
}
```

##### 给混合器传参（参数即可以赋值给`css`属性值的变量）

```scss
@mixin link-colors($normal, $hover, $visited) {
  color: $normal;
  &:hover { color: $hover; }
  &:visited { color: $visited; }
}
```

```scss
a {
  @include link-colors(blue, red, green);
}

//Sass最终生成的是：
a { color: blue; }
a:hover { color: red; }
a:visited { color: green; }
```

当你@include混合器时，有时候可能会很难区分每个参数是什么意思，参数之间是一个什么样的顺序。为了解决这个问题，`sass`允许通过语法`$name: value`的形式指定每个参数的值。这种形式的传参，参数顺序就不必再在乎了，只需要保证没有漏掉参数即可 。

### 选择器继承（`@extend`）

```scss
//通过选择器继承继承样式
.error {
  border: 1px solid red;
  background-color: #fdd;
}
.seriousError {
  @extend .error;
  border-width: 3px;
}
```

`.seriousError`不仅会继承`.error`自身的所有样式，任何跟`.error`有关的组合选择器样式也会被`.seriousError`以组合选择器的形式继承 。

```scss
//.seriousError从.error继承样式
.error a{  //应用到.seriousError a
  color: red;
  font-weight: 100;
}
h1.error { //应用到hl.seriousError
  font-size: 1.2rem;
}
```

`@extend`有两个要点

- 跟混合器相比，继承生成的`css`代码相对更少。因为继承仅仅是重复选择器，而不会重复属性，所以使用继承往往比混合器生成的`css`体积更小。如果你非常关心你站点的速度，请牢记这一点。
- 继承遵从`css`层叠的规则。当两个不同的`css`规则应用到同一个`html`元素上时，并且这两个不同的`css`规则对同一属性的修饰存在不同的值，`css`层叠规则会决定应用哪个样式。相当直观：通常权重更高的选择器胜出，如果权重相同，定义在后边的规则胜出。

 **不要在`css`规则中使用后代选择器去继承`css`规则 , 否则可能会让生成的`css`中包含大量的选择器复制 。**

