##.Change the value from "apple" to "kiwi", in the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"
print(fruits)


##What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']           ###.. ya k vo vanda [1:2] garda mylist ko 0,1,2 cha tya [1:2] yo anusar apple aaudaina cherry ni aaudaina 
print(mylist[2])                       ##.so ( apple,kiwi,mango,cherry ) vo  aba tala print gar vane ko  cha 2 aba yo value bata 0,1,2 = 2 k  cha mango so output will be mango.



##..
fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)
print(fruits)


##..Insert the missing part of the while loop below to loop through the items of a list.

mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1


##Fill in the missing parts to complete the list comprehension:


fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]
print(newlist)

# Original list with 3 fruits
fruits = ['apple', 'banana', 'cherry']

# Create new list with only items that are 'banana'
newlist = [x for x in fruits if x == 'banana']
# This means: "For each item x in fruits, add x to newlist only if x equals 'banana'"

# Step-by-step:
# 1. x='apple' → apple=='banana'? NO → skip
# 2. x='banana' → banana=='banana'? YES → add to newlist
# 3. x='cherry' → cherry=='banana'? NO → skip

print(newlist)  # Output: ['banana']

# fruits stays unchanged: ['apple', 'banana', 'cherry']
# newlist contains only: ['banana']



##..




