numbers=[1,2,3,4,5]

#print items on separate line

for item in numbers:
    print(item)

#explains how we can also use while loop but how it's less efficient!
i = 0
while i<len(numbers):
    print(numbers[i])
    i=i+1