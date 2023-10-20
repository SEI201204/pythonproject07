# Primitive Data Type
# Number , Boolean , String

# Non-Primitive Cata Type / Collection / DaTa Structure ข้อมูลชนิดไม่พื้นฐาน
# List , Tuple , Set , Dictionary

# Data Type จะเอามาใช้กับการเขียนโปรแกรมในเรื่อง ตัวแปร พารามิเตอร์ ฟังก์ชั่น/เมธอด

# ------ List คือ ข้อมูลหลายข้อมูล คนละชนิดได้ ซ้ำกันได้ และมีลำดับ อีกทั้งแก้ไขได้ด้วย ------
#           0    1     2     3      4          5 
my_list1 = [10 , 20 , True , 10 , 'SAU' , [20 , 'IoT']]
#           6    5     4     3      2          1         ติด -    

# ------ Tuple คือ ข้อมูลหลายข้อมูล คนละชนิดได้ ซ้ำกันได้ และมีลำดับ แต่แก้ไขไม่ได้ด้วย เพิ่ม ลบก็ไม่ได้ ------
#            0     1     2     3     4          5
my_tuple1 = (10 , 20 , True , 10 , 'SAU' , (20 , 'IoT'))
#            6     5     4     3     2          1         ติด -    

# ------ Set คือ ข้อมูลหลายข้อมูล คนละชนิดได้ ซ้ำกันไม่ได้(หากซ้ำถือว่าเป็นตัวเดียวกัน) และไม่มีลำดับ และแก้ไขไม่ได้ด้วย แต่เพิ่ม ลบ ได้ ------
my_set1 = {10 , 20 , True , 10 , 'SAU'(20 , 'IoT')}

# ***** Dictionary คือ ข้อมูลหลายข้อมูล ที่เป็น key;value แก้ไขได้ ไม่มีลำดับ ซ้ำได้ *****
# key เป็น String/Integer ส่วน value เป็นอะไรก็ได้ (number,String,boolean,list,tuple,set,dictionary )
my_dictionary1 = {'name':'mod' , 'age':30 , 555:999 , 'flag':True , 'wow':[10,20,30]}