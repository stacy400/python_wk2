#creating a empty list
my_list=[]
#adding elements into a list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
print("my_list:",my_list)
#extending the list
list=[50, 60, 70]
my_list.extend(list)
print("my extended list:",my_list)
#deleting and sorting the list
del my_list[-1]
my_list.sort()
print(my_list)
#printing index of a list
position = my_list.index(30)
print("the index position is:",position) 