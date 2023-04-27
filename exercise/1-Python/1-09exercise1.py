set1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
set2 = set()

set1.add('add')
set2.add('first')
print(set1)
print(set2)
set1.update([1,3])
print(set1)
set1.remove('apple')
print(set1)
set1.discard('orange')
print(set1)

print('--------')
print(len(set1))
if 'banana' in set1:
    print('banana在集合一中')
else:
    print('banana不在集合一中')
