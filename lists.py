#! /usr/bin/python3

myList = []
myList.append(1)
myList.append(2)
myList.append(3)

print(myList[0])
print(myList[1])
print(myList[2])

myOtherList = [4,5,6,7]

for x in myOtherList:
    print(x)

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append([1,2,3]) # Doesn't work. Try concatenation sometime?
numbers.append(4)
numbers.append(5)
numbers.append(6)
strings.append("hello")
strings.append("world")
second_name = names[1]

print(numbers)
print(strings)
print("2nd name is %s." % second_name)
