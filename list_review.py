'''
list複習
list是可以同時儲存多個不同型態的資料型態，中文稱作串列
'''

#創造list，儲存多種值
a = ['Python', 1, 3.5]

#取出list內容，用index(索引)取值，0代表第一個，以此類推
print(a[0])
print(a[1])
print(a[2])

#list內容的新增刪除
#append會心曾在最後面
a.append('new')
print(a)

#remove是指定內容物刪除
a.remove("Python")
print(a)

#可以使用for迴圈取出list當中的物品
for i in a:
    print(i)


#list in list，list當中也可以再加入list
a.append(['w','r'])
print(a)