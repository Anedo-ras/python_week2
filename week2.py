#question 1
my_list = []
#question 2
my_list.append([10,20,30,40])
print(my_list)

#question 3
my_list = [10,20,30,40]
my_list.insert(1,15)
print(my_list)

#question 4
my_list = [10,15,20,30,40]
another_list =[50,60,70]
my_list.extend(another_list)
print(my_list)

#question5
my_list = [10,15,20,30,40,50,60,70]
my_list.pop(-1)
print(my_list)

#question6
my_list = [10,15,20,30,40,50,60]
my_list.sort()
print(my_list)

#question 7
my_list = [10,15,20,30,40,50,60]
index_30 = my_list.index(30)
print(index_30)