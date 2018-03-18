window.onload = function () {

    var sEmail = document.querySelector("#sEmail");
    var sPassword = document.querySelector("#sPassword");
    var button = document.getElementById("button");
    var erroArr = document.getElementsByClassName("error-hint");
    var rightArr = document.getElementsByClassName("right-hint");
    var hintArr = document.getElementsByClassName("hint");
    var iconImgArr = document.getElementsByClassName("icon_img");
    var bool = false;

    sEmail.onfocus = function () {
        this.style.background = "#e4e4e4";
        erroArr[0].style.display = "none";
        rightArr[0].style.display = "none";
        hintArr[0].style.display = "block";
        hintArr[0].innerHTML = "请输入注册时使用的邮箱"

    }
    sEmail.onblur = function () {
        this.style.background = "";
        hintArr[0].style.display = "none";
        var reg = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/;
        if (this.value.length < 1) {
            erroArr[0].innerHTML = '请输入邮箱';
            erroArr[0].style.display = "block";
            bool = false;
        }else if(reg.test(sEmail.value)){
            erroArr[0].style.display = "none";
            rightArr[0].style.display = "block";
            rightArr[0].innerHTML = "邮箱格式正确";
            bool = true;
            iconImgArr[0].src = "../static/images/email_b.png";
        }else {
            hintArr[0].style.display = "none";
            erroArr[0].style.display = "block";
            erroArr[0].innerHTML = "邮箱格式错误";
            bool = false;
        }
    }

    sPassword.onfocus = function () {
        this.style.background = "#e4e4e4";
        erroArr[1].style.display = "none";
        rightArr[1].style.display = "none";
        hintArr[1].style.display = "block";
        hintArr[1].innerHTML = "请输入您的密码";
        if (sEmail.value.length < 1) {
            erroArr[0].style.display = "block";
            erroArr[0].innerHTML = '请输入邮箱';
            bool = false;
        }
    }
    sPassword.onblur = function () {
        this.style.background = "";
        hintArr[1].style.display = "none";
        if (this.value.length < 1) {
            erroArr[1].innerHTML = '请输入密码';
            erroArr[1].style.display = "block";
            bool = false;
        }else {
            iconImgArr[1].src = "../static/images/password_b.png";
            bool = true;
        }
    }
    button.onmouseover = function(){
        if (!bool) {
            button.disabled = "disabled";
            button.value = "信息有误";
            button.style.background = "#fa4850";
        } else {
            button.removeAttribute("disabled");
            button.value = "登录";
            button.style.background = "#27CBAB";
        }
    }
    document.onclick = function () {
        button.removeAttribute("disabled");
        button.value = "登录";
        button.style.background = "#27CBAB";
    };
    button.onclick = function () {
        //var str = 'userName=' + userName.value&'password='+password.value;
        //ajax_tool_pro({
        //    url:"",
        //    data: str,
        //    method: 'post',
        //    success: function (data) {
        //        //接受数据
        //    }
        //})
        var str = {
            "email": sEmail.value,
            "passwd": CryptoJS.SHA1(sEmail.value + ':' + sPassword.value).toString()
        };
        $.ajax({
            url:"/api/authenticate",
            type:"post",
            data:JSON.stringify(str),
	    dataType:"json",
            contentType:"application/json",
            success: function(data){
            //console.log(data);
            if (data.error){ //若data.data存在，表明API调用错误
	    button.value = data.message;
            }
	    else{
	    window.location.href="/?id="+data.name;
	    }
	    //var res = JSON.parse(data).name;
	
                //console.log(JSON.parse(data).name);
                //var headerR = document.getElementsByClassName("header-r")[0];
                //var signOut = document.getElementById("signOut");
                //var userName = document.getElementById("userName");
                //
                //var strArr = JSON.parse(data);
                //var Name = strArr.name;
                //headerR.style.display = "none";
                //signOut.style.display = "block";
                //userName.innerHTML = strArr.name;
               //window.location.href="/?id="+data.name;
            }
        })
    }
}







