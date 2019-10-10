list1 = ['apple', 'peach', 'banana', 'coconut', 'pear']
list2 = ['watermelon', 'lemon', 'apple', 'banana', 'mandarin']
dublicates = [fruit for fruit in list1 if fruit in list2]
print(dublicates)