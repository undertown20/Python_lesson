list_1 = [4, -3, 6, -4, -11, 18, 13, 16, 9, 12, -3, 24, 99, 21]
list_2 = [i for i in list_1 if  i >= 0 and i%4 and not i%3]
print(list_2)