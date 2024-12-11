my_dict = {'Igor': 1998, 'Lara' : 2001, 'Valentin': 1970}
print (my_dict)
print(my_dict['Igor'])
print(my_dict.get('Egor', 'Отсутствует'))
my_dict.update({'Mihail': 2014, 'Tor': 9999})
del my_dict['Lara']
print (my_dict)

my_set = {1,2,3,4,5,5,20,4,14,32,32, 'Enot', False, (2,4,8,16,32,64)}
print(set(my_set))
my_set.add(8)
my_set.add(17)
print(set(my_set))
my_set.remove(False)
print(set(my_set))
