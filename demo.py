'''
第一节

                python的方法
1、print()         打印输出

2、input()         捕获输入值，将输入的值赋值给变量        使用input输入的数据格式都是字符串

a = input ("请输入数字")
b = input ("请输入数字")
print(a+b)

3、type()          数据的转换          #数据转换的规律：1、任何数据都可以转换成字符串  2、字符串类型转成其他格式，需要满足[长得像]这个条件  3、小数和整数可以互相转换

a = int (input("请输入数字："))
b = int (input("请输入数字："))
print(a+b)

4、len()            获取数据的长度     数字和布尔值是没有长度的概念
'''
#a = len("jhfjhjdsjdhjsffh")
#print("字数是：",a)

#text = len(input("请输入文章内容"))
#print("字数是：",text)
#//text = input("请输入文章内容")
#print("字数是：",len(text))



'''
python 的数据格式
字符串 /str            print("你好")
整数 /int              print(222)
小数 /float            print(2.33)
布尔值  /bool          print(True,False)  区分大小写
元组   /tuple          print(())
数组   /list           print([])
字典  /dict            print({})
空   /none type        print(None)


python的加减运算符
python的运算符合常规的数学规律
+  -  *  /  %  


python 的判断符号
<   >   ==  !=  in  is  

python 逻辑关联符号
and or

布尔值——真真为真，真假为假

python的重要概念————变量和赋值
变量名的要求：小写字母开头，不能使用保留字段（关键字），不要写符号，下划线除外

'''












#print("hello world")

"""
元组的作用是用来装数据的，我们可以把数据装在元组里面。
每个变量都是存在内存中的
每个放在元组里的数据，电脑都会给它自动编号，这个标号就叫做下标。
计算机数数都是从0开始的
"""
"""元组
a=()  定义了一个叫做a的变量，然后把一个空的元组，复制给了a

a = (1,2,3,"哈哈","嘻嘻",True)
print(a[3])/a[-3]   []里是下标
print(a.index("哈哈"))#打印”哈哈“的下标
print(a.count("哈哈"))#打印“哈哈”的个数

b = (a,"哈哈",("嘻嘻","嘿嘿"))
print(b[0])#打印b数组中坐标为0的元素

print(b[0][5])
"""
#数组
"""
元组和数组的操作是一模一样的
元组不可以修改，数组可以修改
"""
"""
a = [1,2,3,"哈哈","嘻嘻",True,]
#下标取值都用[]，调用方法都用()
a.append(False)#追加（只能追加一个值—）
a.extend(("今天吃啥"))#追加数组，可以实现数组的合并
print (a)

"""
#字典的格式是 键值对格式 key:value
#字典没有下标的概念

'''
a={
    "name":"张三",
    "age":18,
    "address":"成都",
    "info":{},
    "girlfriend":["小红花","小白","小黄"],# girlfriend是键，[]里的内容是值对
    "brother":("小刚","小黑")
}




print(a["girlfriend"][2])
print(a["brother"][0])

print(a["girlfriend1"]) # 当key不存在时，代码会报错
print(a.get("girlfriend1")) # 当key不存在时，会返回空


update 修改字典
key充当了一个变量
如果key存在，那么就修改
如果key不存在，那么就新增




#a.update(name22="李四") 
a["name"]="李四"    #key是name，存在，会将原来的值改成李四
a["name22"]="李四"  #key是name22，不存在，会新增
del a["name"]  #删除key为name的数据
print(a)
print(a[0])

'''