immutable_var = 21,45, "Urban",False
print(immutable_var)
immutable_var[3] = True # кортеж является неизменяемым объектом, по данной причине элементы, находящиеся в нем нельзя изменить
mutable_list = [21,45, "Urban",False]
mutable_list[3] = True
mutable_list.append(mutable_list[0]*mutable_list[1])
print(mutable_list)