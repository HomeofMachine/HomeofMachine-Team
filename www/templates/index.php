<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="../static/css/css.css">
    <script src="../static/js/jquery1.0.0.1.js"></script>
    <script src="../static/js/slide.js"></script>

</head>
<style>
    * {
        margin: 0;
        padding: 0;
    }
    a {
        text-decoration: none;
    }
    ul,ol,li {
        list-style: none;
    }
    .header {
        width: 1200px;
        height: 140px;
        margin: 0 auto;
        position: relative;
    }
    .header-l {
        position: absolute;
        width: 151px;
        height: 63px;
        display: block;
        float: left;
        margin-top: 36px;
    }
    .header-search {
        width: 520px;
        height: 70px;
        position: absolute;
        float: left;
        left: 50%;
        margin-left: -260px;
        margin-top: 36px;
    }
    .header-search input {
        width: 440px;
        height: 40px;
        border: 2px solid #27CBAB;
        margin-bottom: 5px;
    }
    .header-search .button {
        width: 76px;
        height: 44px;
        float: right;
        background: #27CBAB;
    }
    .header-search .button span {
        color: #fff;
        display: block;
        font-size: 18px;
        line-height: 44px;
        text-align: center;
        margin: 0 auto;
    }
    .header-search a {
        display: block;
        float: left;
        margin-right: 35px;
        color: #c8c8c8;
    }
    .header-r {
        position: absolute;
        right: 0;
        width: 162px;
        height: 38px;
        margin-top: 36px;
    }
    .header-r .register {
        width: 80px;
        height: 38px;
        float: left;
        border: 1px solid #27CBAB;
        border-right: none;
    }
    .header-r .login {
        width: 80px;
        height: 38px;
        float: right;
        border: 1px solid #27CBAB;
        border-left: none;
    }
    .header-r a {
        display: block;
        font-size: 18px;
        line-height: 38px;
        color: #27CBAB;
        text-align: center;
        margin: 0 auto;
    }
    .header-r .header-r-current {
        background-color: #27CBAB;
    }
    .header-r .header-r-current a {
        color: #fff;
    }
    /*头部区域结束*/


    /*nav部分开始*/

    .nav {
        width: 100%;
        height: 44px;
        background-color: #27CBAB;
    }
    .nav .nav-content {
        width: 1200px;
        margin: 0 auto;
        position: relative;
    }
    .nav-content-all {
        width: 142px;
        height: 34px;
        padding-left: 30px;
        padding-top: 10px;
        font-size: 16px;
        color: #ffffff;
        background: #00B38A;
        position: absolute;
    }
    .nav-content-all span {
        display: inline-block;
        position: absolute;
        width: 14px;
        height: 7px;
        left: 110px;
        top: 10px;
    }
    .nav .nav-content .nav-ul {
        position: absolute;
        left: 172px;
    }
    .nav .nav-content .nav-ul li {
        float: left;
        color: #fff;
        font-size: 16px;
        line-height: 44px;
    }
    .nav .nav-content .nav-ul li a {
        float: left;
        color: #fff;
        font-size: 16px;
        line-height: 44px;
        padding: 0 35px;
    }
    .nav .nav-content .nav-all-ul {
        width: 170px;
        position: absolute;
        background: #27CBAB;
        border: 1px solid #c8c8c8;
        border-top: none;
        left: 0;
        top: 44px;
    }
    .nav .nav-content .nav-all-ul li {
        height: 50px;
        line-height: 50px;
        padding-left: 50px;
    }


    /*footer部分开始*/
    .footer {
        width: 100%;
        height: 250px;
        position: relative;
    }
    .footer .footer-content {
        width: 1200px;
        background-color: #ccc;
        margin: 0 auto;
    }
    .footer .footer-content .footer-l {
        float: left;
        position: absolute;
        height: 250px;
    }
    .footer .footer-content .footer-l .logo {
        position: absolute;
        top: 40px;
    }
    .footer .footer-content .footer-l .top {
        position: absolute;
        top: 120px;
    }
    .footer .footer-content .footer-l .top i {
        position: absolute;
        width: 22px;
        height: 17px;
        top: 2px;
        background: url("../static/images/qq.png") no-repeat;
    }
    .footer .footer-content .footer-l .top span {
        position: absolute;
        display: inline-block;
        width: 180px;
        height: 24px;
        line-height: 24px;
        margin-left: 40px;
        color: #27CBAB;
        font-size: 18px;
    }
    .footer .footer-content .footer-l .bottom {
        position: absolute;
        top: 160px;
    }
    .footer .footer-content .footer-l .bottom i {
        position: absolute;
        width: 22px;
        height: 17px;
        top: 2px;
        left: 1px;
        background: url("../static/images/qq.png") no-repeat -22px;
    }
    .footer .footer-content .footer-l .bottom span {
        position: absolute;
        display: inline-block;
        color: #27CBAB;
        font-size: 18px;
        width: 180px;
        height: 24px;
        line-height: 24px;
        margin-left: 40px;
    }
    .footer .footer-r {
        float: right;
        height: 250px;
        margin-top: 20px;
        position: absolute;
        right: 300px;
    }
    .footer .footer-r .big-ul {
        height: 200px;
    }
    .footer .footer-r .big-ul li {
        float: left;
        width: 200px;
        height: 200px;
    }
    .footer .footer-r .big-ul li ul {
        position: absolute;
        width: 200px;
        height: 200px;
    }
    .footer .footer-r .big-ul li ul li {
        width: 200px;
        height: 50px;
        line-height: 50px;
        font-size: 16px;

    }
    .footer .footer-r .big-ul li ul .first-title {

        font-size: 18px;
        color: #c8c8c8;
    }
    /*footer部分结束*/
    .link {
        width: 100%;
        height: 200px;
        position: relative;
}

    .footer-bottom {
        height: 193px;
        margin-top: 20px;
        border-top: 1px solid #E5E5E5;
        padding: 20px 0 30px;
        text-align: center;
    }
    .footer-bottom-link {
        margin-bottom: 10px;
    }
    .footer-bottom-link a {
        margin: 0 10px;
        font-size: 14px;
        color: #000;
    }
    #first-a {
        margin-left: 0;
    }
    #last-a {
        margin-right: 0;
    }
    .footer-botom-copyright {
        margin-top: 16px;
        font-size: 14px;
    }
</style>

<body>
<!--头部区域开始-->
<div class="header">
    <div class="header-l">
        <img src="../static/images/logo.png" alt="">
    </div>
    <div class="header-search">
        <input type="text">
        <div class="button">
            <span>搜索</span>
        </div>
        <div class="recommend">
            <a href="#">发动机</a>
            <a href="#">二维图纸</a>
            <a href="#">机械之家</a>
            <a href="#">啦啦啦</a>
            <a href="#">加速器</a>
        </div>
    </div>
    <div class="header-r">
        <div><a href="#">
        <?php
        echo $_POST['userName'].'您好，机械之家欢迎您！'
        ?>
        </a></div>
    </div>
</div>
<!--头部区域结束-->


<!--导航部分开始-->
<div class="nav">
    <div class="nav-content">
        <div class="nav-content-all">
            全部分类<span><img src="../static/images/sj.png" alt=""></span>
            <ul class="nav-all-ul">
                <li>软件教程</li>
                <li>行业资料</li>
                <li>二维图纸</li>
                <li>三维图纸</li>
                <li>考研交流</li>
                <li>PPT模板</li>
                <li>简历模板</li>
            </ul>
        </div>
        <ul class="nav-ul">
            <li><a href="#">软件教程</a></li>
            <li><a href="#">行业资料</a></li>
            <li><a href="#">图纸下载</a></li>
            <li><a href="#">考研交流</a></li>
        </ul>
    </div>
</div>
<!--导航部分结束-->


<!--banner部分开始-->
<div class="banner" id="banner">
    <div class="wrap" id="wrap">
        <div class="slide" id="slide">
            <ul>
                <!--五张图片-->
                <li class="slide-li"><a href="#"><img src="../static/images/index001.jpg" alt=""/></a></li>
                <li class="slide-li"><a href="#"><img src="../static/images/index002.jpg" alt=""/></a></li>
                <li class="slide-li"><a href="#"><img src="../static/images/index003.jpg" alt=""/></a></li>
                <li class="slide-li"><a href="#"><img src="../static/images/index004.jpg" alt=""/></a></li>
                <li class="slide-li"><a href="#"><img src="../static/images/index005.jpg" alt=""/></a></li>
            </ul>
            <!--左右切换按钮-->
            <div class="arrow" id="arrow">
                <a href="javascript:;" class="prev"></a>
                <a href="javascript:;" class="next"></a>
            </div>
        </div>
    </div>
</div>

<!--banner部分结束-->


<!--footer部分开始-->
<div class="footer">
    <div class="footer-content">
        <div class="footer-l">
            <img src="../static/images/logo.png" alt="" class="logo">
            <div class="top"><i></i><span>995542247</span></div>
            <div class="bottom"><i></i><span>400-820-8820</span></div>
        </div>
        <div class="footer-r">
            <ul class="big-ul">
                <li>
                    <ul>
                        <li class="first-title">了解我们</li>
                        <li>关于我们</li>
                        <li>联系我们</li>
                        <li>售后服务</li>
                    </ul>
                </li>
                <li>
                    <ul>
                        <li class="first-title">服务协议</li>
                        <li>版权声明</li>
                        <li>投诉举报</li>
                        <li>出售作品</li>
                    </ul>
                </li>
                <li>
                    <ul>
                        <li class="first-title">资料专区</li>
                        <li>图纸下载</li>
                        <li>模板专区</li>
                        <li>考研信息</li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</div>

<div class="footer-bottom w">
    <div class="footer-bottom-link">
        <a href="#" id="first-a">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">关于我们</a>|
        <a href="#">English Site</a>|
        <a href="#" id="last-a">Media & IR</a>
    </div>
    <div class="footer-bottom-copyright">
        京公网安备 11000002000088号|京ICP证070359号|互联网药品信息服务资格证编号(京)-经营性-2014-0008|新出发京零 字第大120007号<br>
        互联网出版许可证编号新出网证(京)字150号|出版物经营许可证|网络文化经营许可证京网文[2014]2148-348号|违法和不良信息举报电话：4006561155<br>
        Copyright © 2004 - 2017  机械JX.com 版权所有|消费者维权热线：4006067733经营证照<br>
    </div>
</div>
</body>
</html>