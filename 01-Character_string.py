str1 = "a"*30  # 字符串的创立这几种方法
'''	[:] 提取从开头到结尾的整个字符串;
	[start:] 提取从start开始到结尾的所有字符串;
	[:end] 从开头提取到end-1之间所有字符;
	[start:end] 从start提取到end-1;
	[start:end:step] 从start到end-1,每step个字符提取一个.
'''
str2 = 'Jiayaoqing'
str22 = str2[:]
str3 = '''
          123455
          7890
          123ghfhgfd'''
print(str1)
print(str2)
print(str22)
a = len(str22)
print(str3)
print("a")
