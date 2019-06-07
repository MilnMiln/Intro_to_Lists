#! /usr/bin/python3

myList = []
myList.append(1)
myList.append(2)
myList.append(3)

print("Element 0 of",myList,"is:",myList[0])

myOtherList = [5,6,7]

for x in myOtherList:		
    print(x)

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

#numbers.append([1,2,3]) # Doesn't work.
numbers.extend(myList)
numbers.append(4)
numbers.extend(myOtherList)

strings.append("hello")
strings.append("world")
second_name = names[1]

print(numbers)
print(strings)
print("2nd name is: %s" % second_name)
