<?php
	// 准备一个数组 用来保存 多个用户名
	$mySQL = array("123456","111111","1234567","12121212");

	// 获取 提交过来的 用户名
	$postName = $_POST['userName'];

	// 判断 是否存在于数组中
	/*
		参数1: 查询的内容
		参数2 数组
	*/
	$isIn = in_array($postName,$mySQL);
    echo $isIn;
 ?>