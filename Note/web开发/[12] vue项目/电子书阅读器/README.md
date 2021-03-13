# *epubjs-ebook*   
![](https://img.shields.io/badge/epubjs-v0.3.85-brightgreen)![](https://img.shields.io/badge/vue--cli-v2.5.2-yellow)![](https://img.shields.io/badge/vue--router-v3.0.1-red)![](https://img.shields.io/badge/node--sass-4.12.0-blue)![](https://img.shields.io/badge/code--coverage-95%25-orange)

## *Build Setup*

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```
## *epubjs的核心工作原理*
<img src="/Note/web开发/vue项目/电子阅读器/imgs/epubjs.png">

## *踩坑与小结*
- 中途遇到了这样的报错`Module build failed: TypeError: this.getResolve is not a function at Object.loader`,这个错误的原因是安装的`sass-loader`的版本过高，导致编译失败，查了好久的错误，醉了这也可以，最后将8.0.0版本卸载了装了7.3.1版本就ok啦。
- get到解决`eslint`问题报错的方法.
  - **局部生效:** `/*eslint-disable xxxx*/`.
  - **全局生效:** eslint配置文件中新增一个rule `‘xxxx':'off’`后重启项目.
- `vue`文件模板设置，积累一下。  
  首选项-代码片段-`vue.json`中设置。
- `reset.scss`是为了消除不同浏览器默认样式的不一致性；
  `global.scss`是规定了整个项目的公共样式、公共方法、公共参数等；
  在`global.scss`中有一个公共的字体转换方法`px2rem`，实现`px`与`rem`之间的相互转换，`rem= px / fontSize`。
- 功能实现
  - **电子书解析与渲染：** 1.生成`book`对象 2.通过`book.renderTo`方法生成redition 3.`rendition.display`方法实现渲染；  
  - **翻页：** `rendition.prev`与`rendition.next`方法实现翻页；  
  - **字体设置：** 更改`rendition`的`themes`对象的`fontSize`；  
  - **主题设置：** 定义一组主题数组，数组中包含主题名称与样式，使用`themes`对象的`register`方法遍历主题数组去注册这些主题，调用时使用`themes.select`方法，向其传入主题名称作为参数；  
  - **进度条：** 需求分析之后需要异步实现，通过`epubjs`的钩子函数获取`book`的`locations`对象，`book.ready`返回一个`promise`对象，调用`then`方法返回一个`locations`对象，然后通过`locations`对象的`cfiFromPercentage`方法实现进度条数值转换为`location`,再用`rendition`对象的`display`方法解析location实现具体定位。  
  - **目录：** `book`的`navigation`对象实现，遍历`navigation.toc`展示目录。  

> For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

