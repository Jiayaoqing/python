'''
使用replace()函数可以将指定的字符串替换其他的字符串，
并生成新的字符串。默认情况下，会将字符串所有的指定字符串替换为目标字符串，
也可以指定第三个参数，最多替换次数。
'''
s = "abadeag"
s1 = s.replace("a", "1", 3)  # a换成1 换2个就ok  最多替换次数。
s2 = s.strip("g")  # 将指定收尾字符串都删除掉，可以使用strip()函数，如果不指定字符，默认是删除两侧空格。
                    # lstrip()和rstrip()删除左侧和右侧指定字符。
s3 = s.center(20, '*')         # 使用center()、ljust()、rjust()可以在指定长度的空间中，居中，左对齐，右对齐。
s4 = s.partition('d')          # 分割字符串函数：使用partition(str)函数可以将字符串分成三部分，str之前，str和str之后。
s5 = s.isdigit()
                                #isalpha()函数可以检测字符串是否都是字母，如果都是字母则返回True，否则返回False.
                                #  isdigit()函数可以检测字符串是否都是数字，如果是则返回True,否则返回False.
                                # isalnum()函数检测字符串是否由字母和数字组成.
                                # isspace()函数检测字符串是否全是空格.
                                # 使用count(str)可以统计字符串str出现的次数。
s6 = s.count('a')
print(s6)