<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>注册页面</title>

    <style>
        * {
            margin: 0;
            padding: 0;
        }
        .title  {
            width: 100%;
            height: 63px;
            background-color: #27CBAB;
        }
        .title img {
            margin-left: 30px;
        }
        .w {
            width: 1200px;
            margin: 0 auto;
        }
        .bg {
            float: left;
            margin-top: 50px;
        }
        .bg img {
            width: 422px;
            height: 387px;
        }
        .inf {
            float: right;
            width: 500px;
            margin-right: 80px;
            position: relative;
        }
        .inf .wel {
            width: 400px;
            font-size: 50px;
            font-weight: 700;
            color: #27CBAB;
            margin: 60px auto -20px;
        }
        .inf .name,.password ,.e-mail ,.button{
            width: 400px;
            margin: 60px auto;
        }
        .inf input {
            width: 394px;
            height: 40px;
            font-size: 20px;
            padding-left: 6px;
        }
        .inf lable {
            display: inline-block;
            position: absolute;
            font-size: 20px;
            color: #c8c8c8;
            left: 60px;
            margin-top: -35px;
        }
        .inf .button {
            width: 200px;
            height: 60px;
        }
        .inf .button input {
            width: 200px;
            height: 60px;
            border-radius: 5px;
            background-color: #27CBAB;
            font-size: 20px;
            font-weight: 700;
            color: #fff;
        }
    </style>

</head>
<body>

    <div class="title">
        <img src="../static/images/logo.jpg" alt="">
    </div>
    <div class="w">
        <div class="bg">
            <img src="../static/images/rack.gif" alt="">
        </div>
        <div class="inf">
            <div class="wel">欢迎注册机械之家</div>
            <form action="register.php" method="post">
                <div class="name">
                <input type="text">
                <lable>昵称</lable>
                <div class="name-hint"></div>
                </div>
                <div class="password">
                    <input type="password">
                    <lable>密码</lable>
                     <div class="password-hint"></div>
                </div>
                <div class="e-mail">
                    <input type="text">
                    <lable>邮箱</lable>
                </div>
                <div class="button">
                    <input type="submit" value="立即注册">
                </div>
            </form>
        </div>
    </div>

</body>
</html>