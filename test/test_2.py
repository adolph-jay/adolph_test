

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#     if len(w) > 6:
#         words.insert(0, w)


# for i in range(5):
#     print(i)

# p = (4, 5)
# x, y = p
# print("x = ",x)
# print("y = ",y)
# print('------------------------------------------------------\n')


# data = ['ACME', 50, 91.1, (2012, 12, 21)]
# name, shares, price, date = data
# print('name = ', name)
# print('shares = ', shares)
# print('date = ', date)
# print('price = ', price)
# print('-------------------------------------------------------\n')


# data = ['ACME', 50, 91.1, (2012, 12, 21)]
# name, shares, price, (year, mon, day) = data
# print('name = ', name)
# print('shares = ', shares)
# # print('date = ', date)
# print('price = ', price)
# print('year = ', year)
# print('mon = ', mon)
# print('day = ', day)
# print('-------------------------------------------------------\n')


# p = (4, 5)
# x, y = p
# print(x)
# print(y)
# print(x, y)
# print('---------------------------------------------------------\n\n')


# s = 'hello'
# a, b, c, d, e = s
# print(a, b, c, d, e)
# print('------------------------------------------------------------\n')


# data = ['ACME', 50, 91.1, (2012, 12, 21)]
# _, sahres, prince, _ = data
# print(sahres, prince)
# print('-----------------------------------------------------------\n')


# record = ('David', 'dave@example.com', '773-555-1212', '847-555-1212')
# name, email, *phone_numbers = record
# print(name, email, phone_numbers)
# print('-------------------------------------------------------------\n')


# sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
# *travels_qtrs, current = sales_record
# travel_avg = sum(travels_qtrs)/len(travels_qtrs)
# # print(return avg_comparision(travel_avg, current))
# print(travel_avg, current)
# print('-----------------------------------------------------------\n')


# from collections import deque
#
#
# def search(lines, pattern, history = 5):
#     previous_lines = deque(maxlen=history)
#     for li in lines:
#         if pattern in li:
#             yield li, previous_lines
#         previous_lines.append(li)
#
#
# if __name__ == '__main__':
#     with open(r'../../cookbook/somefile.txt') as f:
#         for line, prevlines in search(f, 'python', 5):
#             for plines in prevlines:
#                 print(pline, end='')
#                 print('-' * 20)

'''
# from collections import deque
# q = deque(maxlen = 3)
# q.append(1)
# q.append(2)
# q.append(3)
# print(q)
# q.append(4)
# print(q)
# q.append(5)
# print(q)
'''

'''
# import heapq

# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))
'''


'''
import  heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
print(nums)
a = []
for i in range(len(nums)):
    print(heapq.heappop(nums))
'''

'''
user_name = 'Jack'
user_age = '16'
print("读者名：", user_name, "年龄：", user_age, sep = ';')
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")
'''
#
# f = open("E:\Python_Code\poem.txt", "w")   # 打开文件以便写入
# print('沧海月明珠有泪', file=f)
# print('蓝田日暖玉生烟', file=f)
# f.close()
#
# import keyword
#
# print(keyword.kwlist)

'''
import  math
import  cmath

a = 999999999999999999999999999999999999999999
print(type(a))

ac1 = 3 + 0.2j
print(ac1, end="")
print(type(ac1), end="")

ac2 = 4 - 0.1j
print(ac2)

print(ac1 + ac2)
print(ac1*ac2)

ac3 = cmath.sqrt(-1)
print(ac3)
'''
'''
print(dir(str))
# print(help(str))


a = 'It is a dog'
print(a.title())
print(a.lower())
print(a.upper())


b = '   a dog, please give it to me,thank you!    '
print(b.strip())
print(b.lstrip())
print(b.rstrip())

print(5/0.5)
'''
'''
a_tuple = ('123', 'name', 'dog', '323234', '4.2')
print(a_tuple[1:3])
print(a_tuple[-3: -1])
print(a_tuple[1:-2])
print(a_tuple[-3:4])

b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b_tuple[2:8:2])
print(b_tuple[2:8:3])
print(b_tuple[2:-2:2])
print(a_tuple+b_tuple)
print(a_tuple)
print(b_tuple)
print(a_tuple*3)


vals =  1, 2, 3
print(vals)

a, b, c =vals
print(a, b, c)
print(dir(list))
'''

# a_list = list(range(1, 8))
# a_list.reverse()
# print(a_list)

'''
scores = {'语文': 89, '数学': 92, "英语": 93}
print(scores)
empty_dict = {}
print(empty_dict)

dict2 = {(20,30): 'good', 30: 'bad'}
print(dict2)

dict3 = dict(spinach = 1.39, cabbage = 2.59)
print(dict3)
'''

'''
scores = {'语文': 89}
print(scores['语文'])
scores['数学'] = 93
scores['英语'] = 94
print(scores)
del scores['语文']
print(scores)
print(scores['数学'])
print('--------------------------------------------------------------\n')

cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 3.8}
cars['BENS'] = 4.3
cars['AUDI'] = 7.5
print(cars)
print('AUDI' in cars)
print('PORSCHE' in cars)
print('LAMBORGHIHI' not in cars)
print(dir(dict))

# cars.clear()
# print(cars)

print(cars.get('BMW'))
print(cars.get('dcasdc'))
# print(cars['POSTURE'])
# print(cars.pop('AUDI'))
# print(cars)

print(cars.popitem())
print(cars)
'''


# cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# print(cars.setdefault('PORSCHE', 9.2))
# print(cars)
# print(cars.setdefault('BMW', 3.4))
# print(cars)

'''
a_dict = dict.fromkeys(['a', 'b'])
print(a_dict)

b_dict = dict.fromkeys((13, 17))
print(b_dict)

c_dict = dict.fromkeys((13, 17), 'good')
print(c_dict)

temp = '书名是：%(name)s, 价格是：%(price)010.2f, 出版社是：%(publish)s'
book = {'name': '疯狂Python讲义', 'price': 88.9, 'publish': '电子社'}
print(temp % book)
book = {'name': '疯狂Python讲义', 'price': 78.9, 'publish': '电子社'}
print(temp % book)
'''

'''
s_age = input("请输入您的年龄：")
age = int(s_age)
if age > 20:
    print("年龄已经大于20岁了")
    print("20岁以上的人应该学会承担责任……")
else:
    print("你还小，再等几年")
'''


# b = 5
# if b > 4:
#     print("b大于4")
# else:
#     b -= -1
# print("b不大于4")


'''
age = 28
if age > 60:
    print("老年人")
elif age > 40:
    print("中年人")
elif age > 20:
    pass
    # print("青年人")
else:
    print("少年人")
'''
#
# s_age = input("请输入您的年龄：")
# age = int(s_age)
# assert 20 < age < 80
# print("您输入的年龄在20和80之间")

'''
count_i = 0
while count_i < 10:
    print("count:", count_i)
    count_i += 1
print("循环结束")
'''
#
# count_i2 = 0
# while count_i2 < 10:
#     print("不停执行的死循环:", count_i2)
#     count_i2 -=1
# print("永远无法跳出的循环体")

'''
count_i = 0
while count_i < 10:
    print('count_i的值', count_i)
    count_i += 1
'''

'''
a_tuple = ('fkit', 'crazyit', 'Charlie')
i = 0
while i < len(a_tuple):
    print(a_tuple[i])
    i += 1
'''

'''
src_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
a_list = [] # 保存能被3整除的元素
b_list = [] # 保存能够被3除余1的元素、
c_list = [] # 保存能够被3除余2的元素
while len(src_list) > 0:
    ele = src_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele % 3 ==1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print("整除3:", a_list)
print("除以3余1：", b_list)
print("除以3余2：", c_list)
'''

'''
s_max = input("请输入您想计算的阶乘：")
mx = int(s_max)
result = 1
for num in range(1, mx + 1):
    result *= num
print(result)
'''

# for i in range(1, 5):
#     print("i:", i)

'''
a_tuple = ('crazyit', 'fkit', 'Charlie')
for ele in a_tuple:
    print('当前元素是：', ele)
'''

'''
src_list = [12, 45, 3.4, 13, 'a', 4, 56, 'crazyit', 109.5]
my_sum = 0
my_count = 0
for ele in src_list:
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)
        my_sum += ele
        my_count += 1
print('总和：', my_sum)
print('平均数：', my_sum / my_count)
'''

'''
my_dict = {'语文': 89, '数学': 92, '英语': 80}
# 通过item()方法遍历所有的key-value对
# 由于item方法返回的列表元素是 key-value对，因此要声明两个变量
for key, value in my_dict.items():
    print('key:',key)
    print('value:', value)
print('--------------------------------------------')
# 通过key()方法遍历所有的key
for key in my_dict.keys():
    print('key:', key)
    print('value:', my_dict[key])
print('---------------------------------------------')
# 通过value()方法遍历所有的value
for value in my_dict.values():
    print('value:', value)
'''

'''
src_list = [12, 45, 3.4, 12, 'fkit', 45, 3.4, 'fkit', 45, 3.4]
statistics = {}
for ele in src_list:
    if ele in statistics:
        statistics[ele] += 1
    else:
        statistics[ele] = 1
for ele, count in statistics.items():
    print("%s 出现的次数为：%d" % (ele, count))
'''

'''
count_i = 0
while count_i < 5:
    print('count_i小于5：', count_i)
    count_i += 1
else:
    print('count_i大于或等于5：', count_i)
'''

'''
a_list = [330, 1.4, 50, 'fkit', -3.5]
for ele in a_list:
    print('元素：', ele)
else:
    print('else块：', ele)
'''

'''
for i in range(0, 5):
    j = 0
    while j < 3:
        print("i的值为：%d, j的值为：%d" % (j, j))
        j += 1
'''

'''
a_range = range(10)
a_list = [x*x for x in a_range]
print(a_list)

b_list = [x*x for x in a_range if x % 2 == 0]
print(b_list)

# 使用for表达式创建生成器
c_generator = (x * x for x in a_range if x % 2 == 0)
# 使用for循环迭代生成器
for i in c_generator:
    print(i, end='\t')
print()
'''

# d_list = [(x, y) for x in range(5) for y in range(4)]
# print(d_list)

'''
dd_list = []
for x in range(5):
    for y in range(4):
        dd_list.append((x, y))
        print(dd_list)
'''

'''
e_list = [[x, y, z] for x in range(5) for y in range(4) for z in range(6)]
print(e_list)
print(len(e_list))
print(type(e_list))
'''

'''
src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b = [3, 5, 7, 11]
# 只要y能整除x,就将她们配对在一起
result = [(x, y ) for x in src_b for y in src_a if y % x == 0]
print(result)
'''

'''
books = ['语文', '数学', '英语']
prices = [78, 87, 98]
for book, price in zip(books, prices):
    print("%s 的价格是： %5.2f" % (book, price))
'''

# for i in range(0, 10):
#     print("i的值是：", i)
#     if i == 2:
#         break


'''
for i in range(0, 10):
    print("i的值是：", i)
    if i == 2:
        break
    else:
        print('else块：', i)
'''

'''
exit_flag = False
#外层循环
for i in range(0, 5):
    #内层循环
    for j in range(0, 3):
        print("i的值为：%d, j的值为： %d" % (i, j))
        if j ==1:
            exit_flag = True
            break
    if exit_flag:
        break
'''


'''
for i in range(0, 3):
    print("i的值是：", i)
    if i  == 1:
        continue
    print("continue后的输出语句")
'''



def test():
    for i in range(10):
        for j in range(10):
            print("i的值是：%d, j的值是：%d" % (i, j))
            if j == 1:
                return
            print("return后的输出语句")
test()










