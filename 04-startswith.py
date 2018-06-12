'''检查字符串是否是以指定字符串开头, 是则返回 True，否则返回 False.
检查字符串是否以指定字符串结束，如果是返回True,否则返回 False.
'''
s = "abcdefgh"
a = s.startswith('a')  # 以及需要传入的参数:string.function(args).
b = s.endswith('g')
print(a, b)