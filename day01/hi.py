alist = [1,2,3,4,"bob"]

#拓展 接收一个可迭代对象 将可迭代对象的每一个元素添加到列表末尾
# alist.extend('nihao')
# print(alist)

# alist.clear()
# print(alist)

#统计元素在列表中出现的次数、
# res = alist.count('bob')
# print(res)

#删除指定索引值的内容 返回被删除的元素
# res = alist.pop(2)
# print(res)
# print(alist)

#pop()删除末尾的元素 返回被删除的内容
# res = alist.pop()
# print(res)
# print(alist)

# alist.reverse()
# print(alist)

#从小到大排序 要求列表中的数据的类型相同
#reverse=True从大到小排序
# alist.sort(reverse=False)
# print(alist)

#insert(ind,val) ind插入数据的位置  val要插入的数据
# alist.insert(1,'bob')
# print(alist)

#获取指定元素的索引值 如果不存在 报错
# res = alist.index('bob')
# print(res)

alist.append(100)
print(alist)
alist.remove(2)
print(alist)