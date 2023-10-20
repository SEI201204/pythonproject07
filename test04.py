# ------ List คือ ข้อมูลหลายข้อมูล คนละชนิดได้ ซ้ำกันได้ และมีลำดับ อีกทั้งแก้ไขได้ด้วย ------
#           0    1     2     3      4          5 
my_list1 = [10 , 20 , True , 10 , 'SAU' , [20,'IoT']]
#           6    5     4     3      2          1         ติด -   

# การเข้าถึงข้อมูลใน list เพื่อเอาข้อมูลมาใช้ หรือแก้ไขค่าข้อมูลให้มันใหม่
# เข้าถึงทีละข้อมูล
print(my_list1[4]) # SAU
print(my_list1[-3]) # 10
print(my_list1[5]) # [20,'IoT']
print(my_list1[-1]) # [20,'IoT']
print(my_list1[5][1]) # IoT

# เข้าถึงทีละหลายข้อมูล Slicing ผลลัพธ์เป็น list
print(my_list1[1:4]) # 20,True,10
print(my_list1[3:]) # 10,SAU,[20,'IoT']
print(my_list1[:3]) # 10,20,True

# เข้าถึงทุกข้อมูล
for info in my_list1 :
    print(info, end=',')
    
print()

print(my_list1)
my_list1[4] = 'Thailand'
print(my_list1)

# List Method
my_list2 = [10 , 20 , True , 10 , 'SAU' , [20,'IoT']]
my_list2.append('wow')
print(my_list2)
my_list2.append([111,222,333])
print(my_list2)
my_list2.extend([444,555])
print(my_list2)
my_list2.remove(10) # เอาตัวแรกที่หาเจอออก
my_list2.remove('SAU')
my_list2.remove([111,222,333])
print(my_list2)
my_list2.pop()
my_list2.pop()
my_list2.pop()
print(my_list2)
my_list2.pop(2) # 2 คือ 10 True หาย
print(my_list2)

# List Function -> len(), min(), max()
my_list3 = [10,20,10,30,True]
print(len(my_list3)) # 5
print(min(my_list3))
print(max(my_list3))