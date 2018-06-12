i = 1
while i < 3:
    age = input("请输入自己的年龄：\n")
    if int(age) > 18:
        print("哥，已成年，网吧可以去了!")
    else:
        print("未成年！不可以去网吧！")
        i += 1