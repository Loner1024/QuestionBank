from hashlib import md5

a = '测试'
a = md5(a.encode('utf-8'))
print(a.hexdigest())