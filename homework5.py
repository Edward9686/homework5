immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
# immutable_var[0] = 200, потому что это тип объекта tuple в нем нельзя менять числа и строки, только если в нём будет отдельный элемент - список
mutable_list = [1, 2, 'a', 'b']
mutable_list[2] = 'Hello'
mutable_list[0] = 66
mutable_list.extend(['New object'])
mutable_list.append(2024)
mutable_list.remove('b')
print(mutable_list)