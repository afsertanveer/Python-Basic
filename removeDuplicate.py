numbers = [1,2,3,4,4,5,5,3,2,3]
for number in numbers :
    if numbers.count(number)>1 :
        numbers.remove(number)

print(numbers)
numbers = [1,2,3,4,4,5,5,3,2,3]
unques = []

for number in numbers :
    if number not in unques :
        unques.append(number)

print(unques)