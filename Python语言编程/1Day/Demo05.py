#序列
'''
列表[]:元素有序，可重复，可以进行添加、删除、更新、查询
元组():只能查询
字典{}:键值对方式存储---可以进行添加、删除、更新、查询
集合set{}:元素无序，去重  添加，删除，更新，查询---交集，并集，差集的运算
range:range(参数1，参数2，参数3)
'''

listA=[9,6,7,4,4,6,6,8]
print(listA)
#添加元素
#在尾部追加
listA.append(9)
print(listA,len(listA))
#任意位置添加
listA.insert(0,3)
print(listA,len(listA))

#更新元素
listA[0]=44
print(listA)

#删除
listA.remove(9) #根据值删除
print(listA)
listA.pop(0) #根据位置删除
print(listA)

#查询 起始位置    结束位置（左闭右开）    步长
print(listA[3:])

#元组
tuple=(4,5,6,3,7,7)
print(tuple[0])
print(list(tuple))

#字典
dicts={"name":"xiaoming","age":23}
print(dicts.keys())
print(dicts.values())
print(dicts.items())
print(dicts.get("name"))
print(dicts["name"])
dicts["name"]="xiaoli"
print(dicts)
dicts.pop("name")
print(dicts)

#set集合
set1={4,4,5,6,7}
print(set1)
set2={3,4,5,2,1}
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)

