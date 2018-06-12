'''def printinfo( name, age = 35 ):
   # 打印任何传入的字符串
   print("Name: ", name)
   print("Age ", age)
# 调用printinfo函数
#printinfo(name="miki" )
printinfo( age=9,name="miki" )  # 与顺序无关 主要是看函数的自定义的顺序才可以的'''
def printinfo(name,age):  # 形式参数和实参数 注意：带有默认值的参数一定要位于参数列表的最后面！！！！。
    print("Name:",name)
    print("Age:",age)
printinfo('贾耀清','23')
