'''
    异常处理:即使代码报错，还要继续运行
'''
# try：
#     a = [1,2,3,4]
#     a[1]
#     print("1")
# except:
#     print("2")

# print("3")

"""
    调用方法
    def : 关键字
    方法名字：不能以特殊符号和数字开头，用小写的字母开头
"""

# def jiafa(a1,a2):
#     sum = a1 + a2
#     return sum 

# a = 1
# b = 2
# c = 3

# # s1 = a + b
# # s2 = a + c
# # s3 = b + c

# s1 = jiafa(a,b)
# s2 = jiafa(a,c)
# s3 = jiafa(b,c)

# print (s1,s2,s3)

"""
    包：有很多功能组成的代码集合，可以跟我们提供很多很多很多有用的功能。
    可以直接调用
    分类：
    自带包—— ——官方包
    第三方包—— ——非官方包（selenium/requests/pymysql/Appium-Python-Client）
    第三方包—— ——pip/pip3(pip3会比pip更稳定，解决一些冲突)，用管理员身份打开cmd
    命令：pip3 -V
          
    #安装命令   install 包名
    pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple some-package      #-i：在国内下载  链接：源（清华源）
    pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
    pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
    pip install Appium-Python-Client -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
"""

"""
    导入
"""
    from test.a import b