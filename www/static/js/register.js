window.onload = function (){
    var userName = document.querySelector("#userName");
    var password = document.querySelector("#password");
    var tPassword = document.querySelector("#t-password");
    var email = document.querySelector("#Email");
    var button = document.getElementById("button");
    var erroArr = document.getElementsByClassName("error-hint");
    var rightArr = document.getElementsByClassName("right-hint");
    var hintArr = document.getElementsByClassName("hint");
    var bool = false;


    userName.onfocus = function () {
        this.style.background = "#e4e4e4";
        rightArr[0].style.display = "none";
        erroArr[0].style.display = "none";
        hintArr[0].style.display = "block";
        hintArr[0].innerHTML = "用户名应为5~10位数字和字母组成";
        bool = true;

    }
    userName.onblur = function () {
        hintArr[0].style.display = "none";
        this.style.background = "";
        if (this.value.length < 1) {
            erroArr[0].innerHTML = '请输入用户名';
            erroArr[0].style.display = "block";
            bool = false;
        } else if (this.value.length < 5) {
            erroArr[0].innerHTML = '用户名过短';
            erroArr[0].style.display = "block";
            bool = false;
        } else {
            erroArr[0].style.display = "none";
            rightArr[0].innerHTML = "用户名可用";
            rightArr[0].style.display = "block";
        }
    }

    password.onfocus = function () {
        this.style.background = "#e4e4e4";
        if (userName.value.length < 1) {
            erroArr[0].style.display = "block";
            erroArr[0].innerHTML = '请输入用户名';
        }
        rightArr[1].style.display = "none";
        erroArr[1].style.display = "none";
        hintArr[1].style.display = "block";
        hintArr[1].innerHTML = "密码由6~10位字母和数字组成 ";
        bool = true;

    }
    password.onblur = function () {
        hintArr[1].style.display = "none";
        this.style.background = "";
        if (this.value.length < 1) {
            erroArr[1].innerHTML = '请输入密码';
            erroArr[1].style.display = "block";
            bool = false;
        } else if (this.value.length < 6) {
            erroArr[1].innerHTML = '密码过短';
            erroArr[1].style.display = "block";
            bool = false;
        } else {
            erroArr[1].style.display = "none";
            rightArr[1].innerHTML = "密码可用";
            rightArr[1].style.display = "block";
        }
    }
    tPassword.onfocus = function () {
        this.style.background = "#e4e4e4";
        if (userName.value.length < 1) {
            erroArr[0].style.display = "block";
            erroArr[0].innerHTML = '请输入用户名';
        }
        if (password.value.length < 1) {
            erroArr[1].style.display = "block";
            erroArr[1].innerHTML = '请输入密码';
        }
        rightArr[2].style.display = "none";
        erroArr[2].style.display = "none";
        hintArr[2].style.display = "block";
        hintArr[2].innerHTML = "密码由6~10位字母和数字组成 ";
        bool = true;

    }
    tPassword.onblur = function () {
        hintArr[2].style.display = "none";
        this.style.background = "";
        if (this.value != password.value) {
            erroArr[2].innerHTML = '两次密码不一致';
            erroArr[2].style.display = "block";
            bool = false;
        } else if (this.value.length < 1) {
            erroArr[2].innerHTML = '请输入密码';
            erroArr[2].style.display = "block";
            bool = false;
        } else if (this.value.length < 6) {
            erroArr[2].innerHTML = '密码过短';
            erroArr[2].style.display = "block";
            bool = false;
        }
        else {
            erroArr[2].style.display = "none";
            rightArr[2].innerHTML = "密码可用";
            rightArr[2].style.display = "block";
        }
    }
    email.onfocus = function () {
        this.style.background = "#e4e4e4";
        if (userName.value.length < 1) {
            erroArr[0].style.display = "block";
            erroArr[0].innerHTML = '请输入用户名';
        }
        if (password.value.length < 1) {
            erroArr[1].style.display = "block";
            erroArr[1].innerHTML = '请输入密码';
        }
        rightArr[3].style.display = "none";
        erroArr[3].style.display = "none";
        hintArr[3].style.display = "block";
        hintArr[3].innerHTML = "your-name@example.com";
    }
    email.onblur = function () {
        hintArr[3].style.display = "none";
        this.style.background = "";
    }


    button.onmouseover = function () {
        if (!bool) {
            button.removeAttribute("disabled");
            button.value = "信息有误";
            button.style.background = "#fa4850";
        } else {
            delete button.disabled;
            button.value = "立即注册！";
            button.style.background = "#27CBAB";
        }

    }
    document.onclick = function () {
        button.removeAttribute("disabled");
        button.value = "立即注册";
        button.style.background = "#27CBAB";
    }


    button.onclick = function () {
        //var str = 'userName=' + userName.innerHTML & 'password=' + password.innerHTML & 'email=' + email.innerHTML;
        var Name = userName.value;
        console.log(Name);
        ajax_tool_pro({
            url: "register.php",
            data:"Name="+Name,
            method: 'post',
            success: function (data) {
                userName.value = data;
            }
        })

}
    }






''