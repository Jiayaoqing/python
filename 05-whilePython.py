i = 1  # 其实i就是指的是行数
while i < 5:
    j = 1  # 其实j就是指的是列数是什么
    while j < 10:
        print("*", end='')  # 每j个换一行
        #print("*")         # 不换行直接就是打印出来*号
        j += 1
    print("\n")
    i += 1
