window.onload = function () {

    var userName = document.querySelector("#userName");
    var password = document.querySelector("#password");
    var button = document.getElementById("button");
    var erroArr = document.getElementsByClassName("error-hint");
    var rightArr = document.getElementsByClassName("right-hint");


    userName.onfocus = function () {
        this.style.background = "#e4e4e4";
        rightArr[0].style.display = "none";
        erroArr[0].style.display = "none";

    }
    userName.onblur = function () {
        this.style.background = "";
        if (this.value.length < 1) {
            erroArr[0].innerHTML = '请输入用户名';
            erroArr[0].style.display = "block";
        }  else if(this.value!="0"){
            erroArr[0].innerHTML = '用户名不存在';
            erroArr[0].style.display = "block";
        }else{
            erroArr[0].style.display = "none";
            rightArr[0].innerHTML = "用户名正确";
            rightArr[0].style.display = "block";
        }
    }

    password.onfocus = function () {
        this.style.background = "#e4e4e4";
        if (userName.value.length < 1) {
            erroArr[0].style.display = "block";
            erroArr[0].innerHTML = '请输入用户名';
        }

    }
    password.onblur = function () {
        this.style.background = "";
        if (this.value.length < 1) {
            erroArr[1].innerHTML = '请输入密码';
            erroArr[1].style.display = "block";
        } else if(this.value!="123456") {
            erroArr[1].innerHTML = '密码错误';
            erroArr[1].style.display = "block";
        }else {

        }
    }

    button.onclick = function () {
        var str = 'userName=' + userName.value&'password='+password.value;
        ajax_tool_pro({
            //url: "../../templates/register.php",
            url:"",
            data: str,
            method: 'post',
            success: function (data) {
                //接受数据
            }
        })
    }
}







