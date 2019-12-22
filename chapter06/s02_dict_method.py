# dict常见用法
old_dict = {
    'Justin': {'Ingenic':'Soc'},
    'Lily': {'Mstar': 'App'}
}
print(old_dict)

# copy: 浅拷贝,用于字典的拷贝
new_dict = old_dict.copy()
print(new_dict)

# 修改了new_dict里面的值，old_dict里面的值也被修改了
new_dict['Justin']['Ingenic'] = 'Solution'
print(old_dict)
print(new_dict)

# 深拷贝
import copy
deep_dict = copy.deepcopy(old_dict)
deep_dict['Justin']['Ingenic'] = 'Network'
print(old_dict)
print(deep_dict)

# fromkeys: 用于将一个列表元素变为字典的key
my_list = ['Justin', 'Lily']
fromkeys_dict = dict.fromkeys(my_list, {'Ingenic':'Solution'})
print(fromkeys_dict)

# get: 用于若没有对应的key，返回默认值
my_get_value = old_dict.get('ptkang', {})
print(my_get_value)
my_get_value = old_dict.get('Justin', {})
print(my_get_value)

# items方法: 用于拆包
for key, value in old_dict.items():
    print(key, value)

# setdefaults
defaults_dict_value = old_dict.setdefault('ptkang', {'Hanwuji': 'Soc'})
print(defaults_dict_value)
print(old_dict)

# update
# 放置字典
old_dict.update({'Tom':{'Tengxun':'QQ'}})
print(old_dict)
# 放置key-value
old_dict.update(Mick={'ali':'taobao'})
print(old_dict)
# list里面放tuple的方式
old_dict.update([('Tick', {'baidu':'search'})])
print(old_dict)
# tuple里面放tuple的方式，tuple后必须再加一个,
old_dict.update((('Mary', {'toutiao':'video'}), ))
print(old_dict)



