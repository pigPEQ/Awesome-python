<template>
<div class='ebook'>
    <TitleBar :ifTitleAndMenuShow="ifTitleAndMenuShow"></TitleBar>
    <div class="read-wrapper">
        <div id="read">
            <div class="mask">
                <div class="left" @click="prevPage"></div>
                <div class="center" @click="toggleTitleAndMenu"></div>
                <div class="right" @click="nextPage"></div>
            </div>
        </div>
    </div>
        <MenuBar :ifTitleAndMenuShow="ifTitleAndMenuShow" 
                 :fontSizeList="fontSizeList" 
                 :defaultFontSize="defaultFontSize" 
                 @changeFontSize='changeFontSize' 
                 :themeList="themeList"
                 :defaultTheme="defaultTheme"
                 @setTheme="setTheme"
                 :bookAvailable="bookAvailable"
                 @onProgressChange="onProgressChange"
                 @JumpTo="JumpTo"
                 :navigation="navigation"
                 ref="MenuBar" >
        </MenuBar>
</div>
</template>

<script>
import TitleBar from '@/components/TitleBar'
import MenuBar from '@/components/MenuBar'
import Epub from 'epubjs'
const DOWNLOAD_URL ='/static/typescript-handbook.epub'
/*eslint-disable xxxx*/
export default {
    components:{
        TitleBar,
        MenuBar
    },
    data(){
        return{
            ifTitleAndMenuShow: false,
            fontSizeList:[
                { fontSize:12 },
                { fontSize:14 },
                { fontSize:16 },
                { fontSize:18 },
                { fontSize:20 },
                { fontSize:22 },
                { fontSize:24 }
            ],
            defaultFontSize:16,
            themeList:[
                {
                    name:'default',
                    style:{
                        body:{
                            'color': '#000','background':'#fff'
                        }
                    }
                },
                {
                    name:'eye',
                    style:{
                        body:{
                            'color': '#000','background':'#ceeaba'
                        }
                    }
                },
                {
                    name:'night',
                    style:{
                        body:{
                            'color': '#fff','background':'#000'
                        }
                    }
                },
                {
                    name:'gold',
                    style:{
                        body:{
                            'color': '#000','background':'rgb(241,236,226)'
                        }
                    }
                }
            ],
            defaultTheme:0,
            //图书是否处于可用状态
            bookAvailable:false,
            navigation:null
        }
    },
    methods:{
        //根据链接跳转指定位置
        JumpTo(href){
            this.rendition.display(href);
            this.hideTitleAndMenu();
        },
        hideTitleAndMenu(){
            //隐藏标题栏和菜单栏
            this.ifTitleAndMenuShow=false;
            //隐藏设置栏
            this.$refs.MenuBar.hideSetting();
            //隐藏目录
            this.$refs.MenuBar.hideContent();
        },
        //progress 进度条的数值（0-100）
        onProgressChange(progress){
            const percentage =progress/100;
            const location =percentage>0? this.locations.cfiFromPercentage(percentage):0;
            this.rendition.display(location)
        },
        setTheme(index){
            this.themes.select(this.themeList[index].name);
            this.defaultTheme =index;
        },
        registerTheme(){
            this.themeList.forEach(theme => {
                this.themes.register(theme.name,theme.style)
            })
        },
        changeFontSize(fontSize){
            this.defaultFontSize =fontSize;
            if(this.themes){
                this.themes.fontSize(fontSize + 'px');
            }
        },
        toggleTitleAndMenu(){
            this.ifTitleAndMenuShow =!this.ifTitleAndMenuShow;
            if(!this.ifTitleAndMenuShow){
                this.$refs.MenuBar.hideSetting()
            }
        },
        prevPage(){
            //rendition.prev
            if(this.rendition){
                this.rendition.prev();
            }
        },
        nextPage(){
            //rendition.next
            if(this.rendition){
                this.rendition.next();
            }
        },
        //电子书的解析与渲染
        showEpub(){
            //生成Ebook
            this.book = new Epub(DOWNLOAD_URL)
            console.log(this.book)
            //生成Rendition，通过book.renderTo
           this.rendition = this.book.renderTo('read',{
                width:window.innerWidth,
                height:window.innerHeight
            })
            //rendition.display渲染电子书
            this.rendition.display();
            //获取themes对象
            this.themes=this.rendition.themes;
            //设置默认字体
            this.changeFontSize(this.defaultFontSize);
            //this.themes.register(name,styles)
            //this.themes.select(name)
            this.registerTheme();
            this.setTheme(this.defaultTheme);
            //获取locations对象
            //通过epubjs的钩子函数来实现
            this.book.ready.then(()=>{
                 this.navigation = this.book.navigation;
                return this.book.locations.generate();           
            }).then(result=>{
            this.locations =this.book.locations;
            this.bookAvailable=true;
            })
        }
    },
    mounted (){
        this.showEpub()
    }
}
</script>

<style lang='scss' scoped>
@import 'assets/styles/global';
.ebook{
    position: relative;
    .read-wrapper{
        .mask{
        position: absolute;
        top:0;
        left: 0;
        display: flex;
        z-index: 100;
        width: 100%;
        height: 100%;
        .left{
            flex: 0 0 px2rem(120);

        }
        .center{
            flex:1;

        }
        .right{
             flex: 0 0 px2rem(120);
        }

       }   
    }
}
</style>