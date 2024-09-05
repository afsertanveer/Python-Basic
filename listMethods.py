from maxNumber import number

numbers = [5,1,9,4,5,3,6]
numbers.append(13)
numbers.insert(2,15)
#numbers.remove(5) # remove the first appearance
# numbers.clear() clear the full array
numbers.pop() # remove the last item
print(numbers.index(5)) # return the index of the first appearance
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(5))
numbers2  = numbers.copy()
print(numbers2,numbers)
numbers.pop()
print(numbers2,numbers)