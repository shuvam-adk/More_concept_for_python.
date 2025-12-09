##Python Sets
#..create a Set
myset = {"apple", "banana", "cherry"}
print(myset)

# ##..Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
 

##..Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


##..Example     True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


##..Example   False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


##..The set() Constructor
name=("shuvam","raja")
out_put=set(name)
print(out_put)


# ##...
# Python Collections (Arrays)   There are four collection data types in the Python programming language:

#..List =       is a collection which is ordered and changeable. Allows duplicate members.
#..Tuple =      is a collection which is ordered and unchangeable. Allows duplicate members.
#..Set =        is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#..Dictionary = is a collection which is ordered** and changeable. No duplicate members.


##..Python - Access Set Items
##..You cannot access items in a set by referring to an index or a key.But you can loop through the set
# items using a for loop, or ask if a specified value is present in a set, by using the in keyword.



#..Loop through the set, and print the values:
nam={"shuvam","raja","sajan"}
for i in nam:
    print(i)
    

place={"india","nepal","bhutan"}
for i in place:print(i)
print(i)


##..Check if "banana" is present in the set:

the_set={"cherry","banana","apple","coconut"}
print("banana"in  the_set)         ##..This will return True
print("coconut"in the_set)        ##..This will return True as well


##..
name={"shuvam","srk","salman","akshay","ranbir","rakhi"}
print("srk" in name)
print("shuv" in name)
print("kriti" in name)


###...Check if "banana" is NOT present in the set:

name={"suva","raja","sujan","babu","namu"}
print("sujan" not in name)                     ##..This will return False

##..
food={"pizza","momo","biryani","burger"}
print("burger" not in food)


##..Python - Add Set Items

name={"das","gas"}
name.add("home")
print(name)

##.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#..
var={"giraffe","tiger"}
var.add("shuvam")
print(var)


##...update() method.  in sets to add multiple items to a set
name={"shuvam","kriti","ram"}
cast={"adhikari","aacharye","karki"}
name.update(cast)
print(name)


##..
set_name={"red","blue"}
set_color={"yellow","green"}
set_name.update(set_color)
print(set_name)


###..Python - Remove Set Items    ..   To remove an item in a set, use the remove(), or the discard() method.

##..remove() method:
name={"shuvam","raj","kashyab"}
name.remove("shuvam")
print(name)

##...
car={"porche","prado","tata"}
car.remove("tata")
print(car)

##..
area={"ktm","hetauda","jhapa","kailali"}
area.remove("jhapa")
print(area)

##..
planates={"earth","mars","jupiter","pluto"}
planates.remove("earth")
print(planates)


###...discard() method:

name={"shuvam","saam","lala"}
name.discard("shuvam")
print(name)


###..
balls={"footbal","basketbal","tennisbal"}
balls.discard("tannisbal")
print(balls)


##..
family={"shuvam","animal='rht.adk' ","mithu","prakriti","swikriti"}
name=list( family)
family.discard("animal='rht.adk'")
print(family)
for i in name:
    print(i + " " +"adhikari") 
print(i)

##..The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


##..Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


##..Python - Loop Sets     You can loop through the set items by using a for loop:
fruits = {"apple", "banana", "cherry"}
for i in fruits:
    print(i)


# python -  Join Sets    and   Frozenset Methods are same 

# Join Sets  ,,   Frozenset Methods
# There are several ways to join two or more sets in Python.

# The   union() and update()   =      methods joins all items from both sets.
# The   intersection()         =      method keeps ONLY the duplicates.
# The   difference()           =      method keeps the items from the first set that are not in the other set(s).
# The   symmetric_difference() =      method keeps all items EXCEPT the duplicates.

# ##..Only learn these 4 operators (most important):

#....(|)  = Union (combine all unique items)

#.....(&) = Intersection (only common items)

#.....(-) =  Difference (items in first set only)

#.....(^) = Symmetric Difference (items in one set or the other, not both)


##..Union --- The union(|) method returns a new set with all items from both sets.
##...Whenever you need to put things together and remove repeats, use union( | )
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)  


##..
name={"shuvam","raj","shuvam","kriti"}
cast={"adhikari","karki","lama"}
full_name=name|cast
print(full_name)

##...
animal={"dog","cat","tiger"}
human={"shuvam","raja","sujan"}
living_being=animal|human
print(living_being)

##..
anime={"manga","naruto","onepiece"}
manga={"bleach","deathnote","dragon"} 
all_anime_society=anime|manga
print(all_anime_society)


##... update()
anime={"sasuke","kakashi","luffy"}
charavter={"zoro","naruto","goku"}
anime.update(charavter)
print(anime)


##..
koko={"my","name","is","shvam"}
ooko={"haha","iam","funny"}
koko.update(ooko)
print(koko)


##..(&) = Intersection (only common items)  It gives you ONLY the items that appear in BOTH sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3= set1 & set2
print(set3)

##...
set4={"shuvam","adhikari","kriti","jhapali","nandu"}
set5={"shuvam","raje","nandu","jhapali"}
set6=set4 & set5
print(set6)


##..
set9={"red","blue","black","white"}
set0={"yellow","red","black"}
set8=set9 & set0
print(set8)

##..
var={"s","h","o","v","a"}
rav={"s","a","rr","v"}
avr= var & rav
print(avr)


##...The intersection_update ("&=") method will also keep ONLY the duplicates,
#..&= keeps only matching items between two sets.


name={"shuvam","jaja","kaka","roma"}
name1={"shuvam","jojo","kaka","ramous"}
name &= name1
print(name)


##..
name={"sasa","kaka","ronaldo"}
name_2={"sasa","jaja","ronaldo"}
name &= name_2
print(name)

##..
man={"shuvam","ramu","saju"}
nam_2={"shuvam","kaka"}
man &= nam_2
print(man)


##...diffrence (-) =  Difference (items in first set only)
name={"shuvam","raja","sujan","kashyab","huku"}
name_2={"shuvam","kashyab","sujan","sasa"}
out_put=name - name_2
print(out_put)

##..Yesle chai afnu diffrence matra dekhauxa

##..
name={"apple","banana","cherry","mango"}
name_2={"banana","cherry"}
out_put = name-name_2
print(out_put)                          ##..    This will print {'apple', 'mango'}



##..(^) = Symmetric Difference (items in one set or the other, not both)

set_1={"shuvam","raj","kashyab","sujan"}
set_2={"shuvam","sajyan","raj","kashyab"}
out_put = set_1 ^ set_2
print(out_put)                                  ##..This will print {'sajyan', 'sujan'}



##..
value_1={"apple","cherry","banana","mango"}
value_2={"apple","mango","cherry"}
out_value= value_1 ^ value_2
print(out_value)


##...Python frozenset    .. frozenset is an immutable version of a set.  ❌❌❌❌❌❌❌❌ ❌❌❌❌❌❌❌❌
##...Remember: Use frozenset when you need an unchanging collection of unique items that can be used as a key or stored in a set!



##...Set Methods...


# Set Methods
# Python has a set of built-in methods that you can use on sets.

#..Method                	    Shortcut	             Description

#.....add()	 	                                         Adds an element to the set
#.....clear()	                                	     Removes all the elements from the set
#.....copy()	 	                                     Returns a copy of the set
#....difference()	               -	                 Returns a set containing the difference between two or more sets
#....discard()                                           Remove the specified item
#....intersection()	               &	                 Returns a set, that is the intersection of two other sets
#....isdisjoint()	 	                                 Returns whether two sets have a intersection or not
#....issubset()	                   <=	                 Returns True if all items of this set is present in another set
#....pop()	 	                                         Removes an element from the set
#....remove()        	 	                             Removes the specified element
#....symmetric_difference()	       ^	                 Returns a set with the symmetric differences of two sets
#....union()	                   |	                 Return a set containing the union of sets
#....update()	                   |=	                 Update the set with the union of this set and others




#.....add()	 	                                 Adds an element to the set....
#..1. add() - Add single element

name={"shuvam","raj"}
name.add("kriti")
print(name)                  #..The output will be {'shuvam', 'raj', 'kriti'}


##..clear()	                                	     Removes all the elements from 
#.. clear() - Remove all elements
name={"animal","human"}
name.clear()
print(name)                   #..The output will be set()


##..copy()                      Returns a copy of the set...
#..3. copy() - Create copy of a set

set_1={"apple","cherry","banana"}
set_2=set_1.copy()
print(set_2)               #..The output will be {'apple', 'cherry', 'banana'}


##..difference()	        "-"	   Returns a set containing the difference between two or more sets...
#..4. difference() (-) - Elements in A but not in B

elements_1={"apple","banana","coconut"}
elements_2={"banana","coconut","date"}
difference = elements_1 - elements_2
print(difference)                           #..The output will be {'apple'}


##..discard()                   Remove the specified item...
#..5. discard() - Remove specified element..
var={"shuvam","kritika","karina"}
var.discard("karina")
print(var)                #..The output will be {'shuvam', 'kritika'}



#...intersection()	        "&"	   Returns a set, that is the intersection of two other sets...
#..6. intersection() (&) - Elements common to A and B

num={1,2,3,4,5}
num_2={4,5,6,7,8}
common=num & num_2
print(common)                #..The output will be {4, 5}


##....isdisjoint()	 	                 Returns whether two sets have a intersection or not...
##..7. isdisjoint() - Check if two sets have no elements in common

name={"shuvam","raj"}
name_2={"kriti","raj"}
out_put=name.isdisjoint(name_2)
print(out_put)                      #..The output will be False because 'raj' is common in both sets


##....issubset()	                   <=	                 Returns True if all items of this set is present in another set... 
##..8. issubset()             (<=)                    - Check if set A is subset of B

num={1,2,3,4,5,6,7}
num_2={4,5}
num_3=num_2 <= num
print(num_3)                     #..The output will be True because all elements of num_2 are present in num


#...pop()	 	                                         Removes an element from the set...
##..9. pop() - Remove and return an arbitrary set element
name={"shuvam","raj"}
out_put=name.pop()
print(out_put)               #..The output will be either 'shuvam' or 'raj' as sets are unordered


##..remove()                       Removes the specified element...
##..10. remove() - Remove specified element

name={"shuvam","raj","kriti"}
name.remove("shuvam")
print(name)               #..The output will be {'raj', 'kriti'}

#...symmetric_difference()	       ^	                 Returns a set with the symmetric differences of two sets...
##..11. symmetric_difference() (^) - Elements in A or B but not both
name={"shuvam","raj","kriti"}
name_2={"shuvam","rajya","kriti"}
out_put= name ^ name_2
print(out_put)             #..The output will be {'rajya'}



##..union()	                   |	                 Return a set containing the union of sets...
#..12. union() - Combine two sets

num={1,2,3,4,5}
name_2={6,7,8,9}
out_put= num | name_2
print(out_put)             #..The output will be {1, 2, 3, 4, 5, 6, 7, 8, 9}



##..update()	                   |=	                 Update the set with the union of this set and others...
##..13. update() - Add elements from another set

name={"shuvam","syam"}
name_2={"kriti","karina"}
name |= name_2
print(name)               #..The output will be {'shuvam', 'syam', 'kriti', 'karina'}







