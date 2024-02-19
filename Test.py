n = int(input())
list = []
while n != 0:
    list.append(n)
    n = int(input())
list1 = list.copy()
list2 = []
for i in range(len(list)):
    m = 0
    while list[i] != 0:
        m += list[i] % 10
        list[i] //= 10
    list2.append(m)
    

ind = list2.index(max(list2))
print(list1[ind])