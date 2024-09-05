for item in [1,2,3,4] :
    print(item)

for item in range(100) :
    print(item)

for item in range(6,10) :
    print(item)

for item in range(1,10,2) :  # here 2 is the step that means the sequence will be broken and come after 2 step
    print(item)


n = int(input())
output = ''
if 1 <= n <= 150:
    for digit in range(1, n):
        output += digit.__str__()

print(output)
