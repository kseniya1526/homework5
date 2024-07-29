immutable_var = (1, 2, 3, 'a', 'b', 'c')
print(immutable_var, type(immutable_var))
print(immutable_var)
#immutable_var[0] = 100
#print(immutable_var)
#Кортеж относится к неизменяемым типам данных, в отличие от списка, поэтому мы не можем изменить данные внутри кортежа
muttable_list = ['carrot', 'potato', 'tomato']
print(muttable_list)
muttable_list[0] = 'cucumber'
muttable_list[1] = 'cabbage'
muttable_list[2] = 'onion'
print(muttable_list)

