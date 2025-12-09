#Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.

my_tuple = ("apple", "banana", "cherry")  #..This is tuple( )
print(my_tuple)


#..Allow Duplicates  .. Since tuples are indexed, they can have items with the same value:
##..
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


##..Tuple Length   The  syntax of the length is  this = " print(len(thistuple)) "

name=("shuvam")
print(len(name))


##..Create Tuple With One Item        /  thistuple = ("apple",)
##..To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)    #..The comma help to recognize the tupple.
print(type(thistuple))


##...Tuple Items - Data Types
##..Example
##..  String , int and boolean data types:
tuple1 = ("apple", "banana", "cherry")     #..string
tuple2 = (1, 5, 7, 9, 3)                   #..int
tuple3 = (True, False, False)              #..bollen


##..Python Collections (Arrays)

#..There are four collection data types in the Python programming language:

#..List   =   is a collection which is ordered and changeable. Allows duplicate members.
#..Tuple  =   is a collection which is ordered and unchangeable. Allows duplicate members.
#..Set    =   is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#..Dictionary     is a collection which is ordered** and changeable. No duplicate members.


##..Python - Access Tuple Items
##...Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

##..Range of Indexes in tuples =
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])     #..The output will be like this  ('cherry', 'orange', 'kiwi')


##...Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

##..Check if Item Exists

##..To determine if a specified item is present in a tuple use the in keyword:

variable=("shuvam","adhikari","kritik","aashu")
if "aashu" in variable:
    print("yes,'aashu is in tupple..")
else:
    print("No,'aashu is not in the tupple.. ' sorry '")
print()


##..Python - Update Tuples   /  Tuples are unchangeable,

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds.
##..Change Tuple Values..  You can convert the tuple into a list, change the list, and convert the list back into a tuple.


##.
auto=("car","jet","bike","tractor")   ##..Tuple immmutable va ko reason le  tupple lai list  banaoune list() function use gare ra 
val=list(auto)           ##..Yo ma gare ko jasto ..
val[2]="bullet"            ##.. Yo bullet list  ma add garyo value[2] vane ko chai "bike" ko sata ma bullet add garye ko ho ..
auto=tuple(val)       ##..Auto lai feri tuple ma convert gareko
print(auto)            ##..Ani print gareko 


##...Another Example..

x = ("apple", "banana", "cherry")      #..Create a tuple
y = list(x)                       #..Convert the tuple into a list 
y[1] = "kiwi"                    #..Change an element in the list
x = tuple(y)                     ##..Convert list back to tuple
print(x)                         #..Print the new tuple


##..
name=("car","bike","tractor")
val=list(name)
val[2]="jet"
name=tuple(val)
print(name)



##..Add Items
thistuple=("apple", "banana", "cherry")
my_list=list(thistuple)
my_list.append("orange")
thistuple=tuple(my_list)
print(thistuple)


##..
variable=("apple","cherry","papaya")
new_list=list(variable)
new_list.append("grapes")
variable=tuple(new_list)
print(variable)


###...Remove Items..
the_tuple=("apple", "banana", "cherry")
change=list(the_tuple)
change.remove("apple")
the_tuple=tuple(change)
print(the_tuple)


##...The del keyword can delete the tuple completely
the_stup = ("apple", "banana", "cherry")
del the_stup                     # Deletes the tuple entirely



##..
name=("shuvaa","kaka")
del name


##....Python - Unpack Tuples
#..Packing a tuple:
fruits = ("apple", "banana", "cherry")

##....Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)         #..The output will be like this  apple
print(yellow)       #..The output will be like this  banana
print(red)         #..The output will be like this  ['cherry', 'strawberry', 'raspberry']

## Think of it like this:
## First, assign "apple" to green
## Then assign "banana" to yellow
## Then take all the remaining fruits and put them into a list called red

##..
record=["shuvam","apf","adkshuvam27@gmail.com",9846952720,"hetauda","makawanpur"]
(val1,val2,val3,*val4)=record
print(val1)        #..The output will be like this shuvam
print(val2)        #..The output will be like this apf
print(val3)        #..The output will be like this adkshuvam27@gmail.com
print(val4)        #..The output will be like this [9846952720, 'hetauda', 'makawanpur']


###...Python - Loop Tuples     Loop Through a Tuple You can loop through the tuple items by using a for loop.

the_tuple=("shuvam","sag","masa")
for i in the_tuple:
  print(i)
  
##..
light=("mero","name","is","shuvam","adhikari")
for i in light:
    print(i)
      
##
var_2=(1,2,3,4,5)
for i in var_2:
    print(i)
    
##..Use the range() and len() functions to create a suitable iterable.
val_3=("value","of","python")
for i in range(len(val_3)):
    print(val_3[i])

##..
ball=("value","is the","best","value")
for i in range(len(ball)):
    print(ball[i])



###...Python - Join Tuples

name=("shuvam" , "adhikari") 
age=23,                            ##..Yo 23  paxi ko 23, comma ko k use ho berse ??

total= name + age
print(total)               ##..The output will be like this ('shuvam', 'adhikari', 23)



##..
name=("shuvam","kriti","samrat")
age=22,24,25
total=name + age
print(total)



##..Multiply Tuples....If you want to multiply the content of a tuple a given number of times, you can use the * operator:

fruits=("apple","cherry","banana")
value=fruits*2
print(value)


##..
name=("shuvam" " ")
multi_value=name*3
print(multi_value)


###...Python - Tuple Methods




