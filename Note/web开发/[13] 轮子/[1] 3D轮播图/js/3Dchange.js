
var arr=['t7','t6','t5','t4','t3','t2','t1'];
var index=0;

$(".prev").click(()=>prevImg())
$(".next").click(()=>nextImg())


//定义上一张方法
function prevImg(){
    //将最后一个数添加到数组的开头，并在结尾删除这个数
    arr.unshift(arr[6]);
    arr.pop();
    //i为索引，e为当前元素
    $("li").each((i,e)=>{
        $(e).removeClass().addClass(arr[i]);
    })
    index--;
    if(index<0){
        index=6;
    }
    show();
}

//定义下一张方法
function nextImg(){
    //将最前面一个数添加到数组的末尾，并在头部删除这个数
    arr.push(arr[0]);
    arr.shift();

    $("li").each((i,e)=>{
        $(e).removeClass().addClass(arr[i]);
    })
    index++;
    if(index >6){
        index=0;
    }
    show();
}

//改变底下的颜色
function show(){
    /*
      $(".buttons span").eq(index).addClass("blue")  为当前索引值所在的span添加blue样式  
      .siblings().removeClass("blue"); 清除其他span拥有的blue样式
    */ 
    $(".buttons span").eq(index).addClass("blue").siblings().removeClass("blue");
}

// 点击图片触发上一张方法
$(document).on("click",".t2",()=>{
    prevImg();
    return false;//返回一个false值，让a标签不跳转
});

/*
on与click的区别，两者在静态绑定时没有区别，对于动态控件，只有on才能实现动态绑定

$(".t2").click(()=>{
    prevImg();
    return false;//返回一个false值，让a标签不跳转
});

上面这个只能实现t2的跳转
*/

// 点击图片触发下一张方法
$(document).on("click",".t4",()=>{
    nextImg();
    return false;//返回一个false值，让a标签不跳转
});

//增加定时器，鼠标移入清除定时器，移出加入定时器
var timer= setInterval(nextImg,5000);
$(".box").mouseover(()=>clearInterval(timer));
$(".box").mouseleave(()=>setInterval(nextImg,5000));