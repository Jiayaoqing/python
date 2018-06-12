"""
 if xxx1:
	事情1
elif xxx2:
	事情2
elif xxx3:
	事情3


说明:
当xxx1满足时，执行事情1，然后整个if结束
当xxx1不满足时，那么判断xxx2，如果xxx2满足，则执行事情2，然后整个if结束
当xxx1不满足时，xxx2也不满足，如果xxx3满足，则执行事情3，然后整个if结束

"""
age = input("请输入年龄：\n")
if int(age) > 18:
    print("成年了")
elif int(age) == 18:
    print("成年")
elif int(age) < 18:
#else:
    print("未成年")