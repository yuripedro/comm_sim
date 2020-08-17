import cumulant as hoc

list1 = [1, 2, 3,4,5,6,7,8,9,10]


cumulant = hoc.Cumulant()

a=cumulant.C80(list1,list1,list1,list1,list1,list1,list1,list1)
print(a)