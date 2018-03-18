window.onload = function (){
    var userName = document.querySelector("#rUserName");
    var password = document.querySelector("#rPassword");
    var tPassword = document.querySelector("#t-rPassword");
    var email = document.querySelector("#rEmail");
    var button = document.getElementById("button");
    var erroArr = document.getElementsByClassName("error-hint");
    var rightArr = document.getElementsByClassName("right-hint");
    var hintArr = document.getElementsByClassName("hint");
    var iconImgArr = document.getElementsByClassName("icon_img");
    var bool = false;
    userName.onfocus = function () {
        this.style.background = "#e4e4e4";
        rightArr[0].style.display = "none";
        erroArr[0].style.display = "none";
        hintArr[0].style.display = "block";
        hintArr[0].innerHTML = "用户名应为5~10位数字和字母组成";
        iconImgArr[0].src = "../static/images/account.png";
        bool = true;
    };
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
        }else{
                        erroArr[0].style.display = "none";
                        rightArr[0].innerHTML = "用户名可用";
                        rightArr[0].style.display = "block";
                        iconImgArr[0].src = "../static/images/account_b.png";
            //$.ajax({
            //    url:"test-SQL.php",
            //    data:"userName="+userName.value,
            //    type:"post",
            //    success: function (data) {
            //        if(data) {
            //            erroArr[0].innerHTML = '用户名已被使用';
            //            erroArr[0].style.display = "block";
            //            bool = false;
            //        }else{
            //            erroArr[0].style.display = "none";
            //            rightArr[0].innerHTML = "用户名可用";
            //            rightArr[0].style.display = "block";
            //            iconImgArr[0].src = "../static/images/account_b.png";
            //        }
            //    }
            //});
        }
    };
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
        iconImgArr[1].src = "../static/images/password.png";
        bool = true;
    };
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
            iconImgArr[1].src = "../static/images/password_b.png";
        }
        //if(password.value===this.value&&password.value!=null&&this!==null){
        //    erroArr[2].style.display = "none";
        //    rightArr[2].innerHTML = "密码一致";
        //    rightArr[2].style.display = "block";
        //    iconImgArr[2].src = "../static/images/password_b.png";
        //}
    };
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
        hintArr[2].innerHTML = "请确认您的密码";
        iconImgArr[2].src = "../static/images/password.png";
        bool = true;
    };
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
            rightArr[2].innerHTML = "密码一致";
            rightArr[2].style.display = "block";
            iconImgArr[2].src = "../static/images/password_b.png";
        }
    };
    email.onfocus = function () {
        erroArr[3].style.display = "none";
        this.style.background = "#e4e4e4";
        if (userName.value.length < 1) {
            erroArr[0].style.display = "block";
            erroArr[0].innerHTML = '请输入用户名';
        }
        if (password.value.length < 1) {
            erroArr[1].style.display = "block";
            erroArr[1].innerHTML = '请输入密码';
        }
        if (password.value.length < 1) {
            erroArr[2].style.display = "block";
            erroArr[2].innerHTML = '请输入密码';
        }
        rightArr[3].style.display = "none";
        erroArr[3].style.display = "none";
        hintArr[3].style.display = "block";
        hintArr[3].innerHTML = "your-name@example.com";
    };
    email.onblur = function () {
        hintArr[3].style.display = "none";
        this.style.background = "#fff";
        var reg = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/;
        if (reg.test(email.value)) {
            erroArr[3].style.display = "none";
            rightArr[3].style.display = "block";
            rightArr[3].innerHTML = "邮箱格式正确";
            iconImgArr[3].src = "../static/images/email_b.png";
        } else {
            erroArr[3].style.display = "block";
            erroArr[3].innerHTML = "邮箱格式不正确";
            bool = false;
        }
    };
    button.onmouseover = function () {
        if (!bool) {
            button.disabled = "disabled";
            button.value = "信息有误";
            button.style.background = "#fa4850";
        } else {
            button.removeAttribute("disabled");
            button.value = "立即注册";
            button.style.background = "#27CBAB";
        }
    };
    document.onclick = function () {
        button.removeAttribute("disabled");
        button.value = "立即注册";
        button.style.background = "#27CBAB";
    };
    $(button).on("click", function () {
        var str = {"name":userName.value,
                    "passwd":CryptoJS.SHA1(email.value + ':' + password.value).toString(),
                    "email":email.value};
        $.ajax({
            url:"/api/users",
            data:JSON.stringify(str),
            contentType:"application/json",
            type:"post",
            success:function (data){
                //console.log(data);
	    
            if (data.error){ //若data.data存在，表明API调用错误
	    button.value = data.message;
            }
	   else{
	    window.location.href="/login";}
	    
            }
        })
    })
};

