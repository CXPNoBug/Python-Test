# 异常捕获
# try:
#     year = int(input('输入年份：'))
# except ValueError:
#     print('年份要输入数字')
#
# a=123
# a.append()

# except (ValueError,AttributeError,KeyError) # 捕获多个异常

# 捕获异常并打印异常信息
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('0不能作为除数 %s' % e)

# 自定义异常
try:
    raise NameError('HelloError')
except NameError:
    print('my custom error')

# 捕获异常，finally 最终执行
try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()
