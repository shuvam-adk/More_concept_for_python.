##..>>.>>> In this file we uplode important things to remember.......>>>>

#....1 >>>
import sys
print(sys.version)

#...2 >>>>.

##...SYS FullForm = sys stands for System


#..3 >>>  Indentation

#..Correct Indentation: ("print agadi ko gap..")
# if 5<8:
#     print("Five is less then eight ")
  

#..4 >>>  function  
#print() is a function.
print()                          #.....Function with NO input
print("Hello")                   #.....Function with string input
print("Hello", "World")          #.....Function with multiple inputs
#print(name)                     #.....Function with variable input


#..5 >>>  Arguments = The information you give to a function

print("name")                              #......name is an argument
print("Hi,shuvam adhikari ")               #......Hi,shuvam adhikari  this whole thing is an argument


#..6 >>>  What is the use of this     ( end=" " )

a=("Shuvam")
s=("Adhikari")
d=("is")
f=("doing")
g=("well. ")              #... The output will be like this... (  Shuvam Adhikari is doing well. )  
print(a,s,d,f,g,end= " ")



#..7 >>>  .Mix Text and Numbers        

mix_text=["One:",1,"Two:",2,"Three:",3,"Four:",4,"Five:",5,"six:",6,"Seven:",7,]

print(mix_text)                            #..>>> The output will be lke this ("One:",1,"Two:",2,"Three:",3,"Four:",4,"Five:",5,"six:",6,"Seven:",7)
                
                                    
                        
#..8 >>> CASTING  = Changing a value from one type to another type   

a=9393     # This is an integer value 
s=float(a)         #    We change int value into float value..
print(s)


#..9 >>> Get the Type = (You can gat the data type of a variable with the like  print(TYPE(....))

a=28
s=21.2
print(type(a))  # If you want's to find the type like this you can do like this  print(type(...))
print(type(s))


#..10 >>>..Multi Words Variable Names 

# Camel Case
myVariableName= "kriti"                      #....(As you can see the first letter is small and remaning are capital)
print(myVariableName)

# Pascal case  (Each word starts with capital letter.) Like this

MyName = "raj"       # like this the first both letters are  capital  "MyName"
AgeOfMyFriend = 22     
DayOfTheDay  = "what"
print(MyName,AgeOfMyFriend, DayOfTheDay, end = " ")

###..Snake Case    (In this  Case we do like this name_of_the_charaacter ) like this 

my_variables_is_this="what is this "   # We do some thing like this is snake case   we do under score 
print(my_variables_is_this)


#..11 >>>.Global Variables  (def..)    (YO  AJAI BUJNI   AAYENA MALAI .????)   ❌❌❌❌❌❌❌❌

x="name"
def n():       # n = function name  j rakhe ni hunxa  , def = keyword to define a function  ,  (:)=WHERE the function instructions BEGIN 
  print("my"+ " "+ x +" is shuvam adhikari .")
n()


#..12 >>>.python Built-in Data Types........
#         Text Type          =     	  str                              n="shuvam"
#         Numeric Types      =  	  int, float, complex              int=123   ,  float = 10.23    ,   complex = 
#         Sequence Types     = 	      list, tuple, range               list = [ ]   ,  tuple =()      ,
#         Mapping Type       =	      dict                             q={"name":"shuvam","age":92} 
#         Set Types          =    	  set, frozenset                   set={"name":shuvam,"age":23}    ,
#         Boolean Type       = 	      bool                             True , false
#         Binary Types       =	      bytes, bytearray, memoryview
#         None Type          =	      NoneType


#..13 >>> Getting the Data Type

#string

a="hello vai"     #<class 'str'>
print(type(a))

#intiger
a=20
print(type(a))    #<class 'int'>

#list
a=["apple","banana","cabage","mango"]    #<class 'list'>
print(a)

#tuple
a=("apple","banana","cabage","mango")    #<class 'tuple'>
print(a)
#set
a={"apple","banana","mango"}    #<class 'set'>
print(a)

#  range
w=range(21)
print(w)

#.dictionery
q={"name":"shuvam","age":92}
print(q)



#..14 >>> Random Number 
import random
print(random.randrange(1,23))       # Yesle chai 1 bata 23 samako ma random number output ma nikalxa..


#..15 >>> Multiline Strings  ("""   .. .. . . ..  """)

name=""" MY name is shuvam adhikari ,
I am from hetauda,
I will be back."""
print(name)

#..16 >>> Check String    and   Check if NOT  
a=("my name is shuvam ")      
print("my"in a)                       #...  ( yo check string  " in " le check garxa  xa ki nai value vane ra.

c=("Hi my name is shuvam ..")
print("kriti" not in  c)              #..( yo check if not  string  " not in " le check garxa  xa ki nai value vane ra.


#..17 >>> Use it in an if statement:  ("if  statement ")
txt="i am the person you are  looking for "
if " pers " in txt:
 print(" yes, it is in the txt" )
else:
     print("not in the txt ")
     
     
#..18 >>>..Python - Slicing Strings

q=("hello my boy ")
print(q[2: ])              #.The output will be  ( llo my boy )   #.. Slicing vane ko chai  yesati nai ho as you  can see ...

#.
a="hi shuvam  my name is  kriti adhikari "
print(a[2: ])   # as you can seee i  give the space to print the  all value from the variable...


#..19 >>>.Negative Indexing  ( Use negative indexes to start the slice from the end of the string: )

h="hi raja ko chora rajkumar"
print(h[ :-17])                  #...Yo k hoo vanda aru time ma jasto negative index ma ( index 0 bata  haina -1 bata suru hunxa ra paxadi bata huncha  )


#..20 >>> Python - Modify Strings    >>>  (variable. upper()) 

hi="my name is shuvam adhikari "
print(hi.upper())                  # yo upper() function le   sabai case lai upper case ma change garxa..

#.Lower Case  
var="MY NAME IS SHUVAM ADHIKARI "
print(var.lower())                  #..yo lower() function le   sabai case lai lower case ma change garxa..


#..21 >>> Remove Whitespace , text.strip()  yo le chai  agadi ko ra paxade ko space lai hataoucha.

name="   Shuvam,adhiakri    "
print(name.strip())

#..22 >>> Replace String  variable.replace function("a","b") this replace a thing to what thing you just give command to replace

#...#variable.replace function("a","b")

p="my name is kritik adhikari"
print(p.replace ("kritik","shuvam") )           #..The output will be ("my name is shuvam adhikari")

#..23 >>>  .Split String 

##... variable.split(" ")  yo ho ka ra k lai split garn evane ho 
a="hello vai raja"
print(a.split("e"))                               #..#..The output will be ['h', 'llo vai raja']


#..24 >>> Python - String Concatenation To combine, two strings you can use the + operator. Merge variable a with variable b into variable c:
#..like this..
intro="Hi"
name="shuavm"
last_name="adhikari"
full_name= intro +" "+name + " "+ last_name
print(full_name)                                        #..The output will be ( Hi shuavm adhikari )


#..25 >>> . 55..Python - Format - Strings we cannot combine strings and numbers  thats why we use ( f" ) string
#.like this 
age = 36
#This will not  produce an error:
txt =f"My name is John, I am:'{age}', years old"
print(txt)                                                 #..The output will be ( My name is John, I am:'36', years old )

#..26 >>>..Placeholders and Modifiers

name="shuvam"
last_name="adhikARI"
print(f"Uper_case : {name.upper()},{last_name}")                          #..The output will be (" Uper_case : SHUVAM,adhikARI ")


#..27 >>>..Python - Escape Characters   ( \" .. ..   \") we do this .

name="my name is \"Shuvam\" adhikari ."
print(name)                                                            #..The output will be (  my name is "Shuvam" adhikari .)


#..28 >>>..  .Python - String Methods  ( there are so many  like )

#..# #..Python String capitalize() Method  ... (The capitalize() method returns a string where the first character is upper case, and the rest is lower case.)
name="shuvam Adhikari "
print(name.capitalize())   # this will halp to capitalize the first letter like this ( Shuvam adhikari )


#.Python String casefold() Method ... (The casefold() method returns a string where all the characters are lower case.)

a="SIJIOFN"
print(a.casefold())                          #.The output will be like this ( sijiofn )

#.# Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
print(txt)


#..29 >>>..Python Booleans   (Booleans represent one of two values: True or False.)

#..
print(10>3) #( 10 is greater than 3)   #The output will be   ( True ) 

#.
print(20==18)  # ( 20 is equal equal ti 18)               #.#The output will be   ( False ) 



#..30 >>> #..//The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#..31 >>> ..In Arithmetic operators there are =  

# # Addition            x + y	
# #..Subtraction        x - y	
# #..Multiplication     x * y
# #..Division           x / y
# #..Modulus	          x % y
# #..Exponentiation     x ** y
# #..Floor division	  x // y


#..32 >>>... In Assignment operator there are  =  Operators like  this =

# #1..     =	        x = 5	         x = 5	
# #2..    +=	        x += 3	         x = x + 3	
# #3..    -=	        x -= 3    	     x = x - 3	
# #4..    *=	        x *= 3	         x = x * 3	
# #5..    /=	        x /= 3	         x = x / 3	
# #6..    %=	        x %= 3	         x = x % 3	
# #7..    //=	        x //= 3	         x = x // 3	
# #8..    **=	        x **= 3	         x = x ** 3	
# #9..    &=	        x &= 3	         x = x & 3	
# #10..   |=	        x |= 3	         x = x | 3	
# #11..   ^=	        x ^= 3	         x = x ^ 3	
# #12..   >>=	        x >>= 3	         x = x >> 3	
# #13..   <<=	        x <<= 3	         x = x << 3	
# #14..   :=	       print(x := 3)	 x = 3
# #.                                    print(x)


#..33 >>>.The Walrus Operator                         ❌❌❌❌❌❌❌❌
# name="shuvam adhikari "
# if(name := input("Enter your real name :")) != " ":
#   print(f"hello {name}")

#..This is the easy way to understanding this .... example of the Walrus operation 

# #Normal = (just saving):
# x = 5 + 3        # SAVE the result of 5+3 as x

# # Walrus := (do and save):
# if (y := 5 + 3) > 6:  # DO 5+3 AND SAVE as y, then check if >6
#     print(y)


#..34 >>>..Python Comparison Operators


# #..  Operator        	 Name	                  Example	
# #       ==	             Equal	                   x == y	
# #       !=	           Not equal	               x != y	
# #       >	          Greater than	               x > y	
# #       <	           Less than	               x < y	
# #       >=	      Greater than or equal to	       x >= y	
# #       <=	       Less than or equal to	       x <= y

x = 5
y = 3

print(x == y)    #(5 and 3 is not equal ==  so it willl get false )
print(x != y)      #("Just asking "Are they different?"  k yo 5 and 3  farak cha ta  vane ko ho like ya 5 and 5 va ko vaye false aaunthyo kina vane  farak chain atyo duita ma )
print(x > y)       #(" x > y means: "Is x BIGGER than y? ")
print(x < y)       #("x < y means: "Is x SMALLER  than y?")
print(x >= y)      #(" x >= y means: "Is x BIGGER OR EQUAL to y? ")
print(x <= y)      #(" x <= y means: "Is x SMALLER OR EQUAL to y? " )



x = 5    # 🟰
y = 3    # 🟰
print(x != y)  # "Is 5 different from 3?" → YES! → True


#..35 >>>..Chaining Comparison Operators

x = 5
print(1 < x < 10)                 #..The output will be ( True )

# #..Think of it like this:
# #..We have number 5
# #..We ask: "Is 5 between 1 and 10?"
# #..Look: 1 ← 5 → 10 → YES, 5 is between them!
# #..So answer is: True ✅


#..36 >>>.........Logical Operators
# #Logical operators are used to combine conditional statements:

# #     Operator	                    Description	                                         Example	
# #       and 	             Returns True if both statements are true	                    x < 5 and  x < 10	
# #        or	         Returns True if one of the statements is true	                x < 5 or x < 4	
# #       not	         Reverse the result, returns False if the result is true	     not(x < 5 and x < 10)


#..37 >>>... Identity Operators  :-  Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, 
#  with the same memory location:

#             Operator	                    Description	                          Example 
#                                                                
#                is         	    Returns True if both variables                x is y
#                                       are the same object	                    
#                                                                  	
#              is not	             Returns True if both variables              x is not y
#                                      are not the same object	                
 


#..38 >>>  The is operator returns True if both variables point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)      #..Returns True if both variable  are the same objec
print(x is y)       #,, reaturn False
print(x == y)       #..Reaturn true cause same look.


#Cookie Example:

# x = ["apple", "banana"]   Bake cookie "x"

# y = ["apple", "banana"]    Bake identical cookie "y"

# z = x =  Give cookie "x" a second name "z"

# Results:
# x is z = Same cookie? ✅ True
# x is y = Same cookie? ❌ False (different cookies)
# x == y = Same look? ✅ True (look identical)
# Simple rule:
# is = Same object?
# == = Same contents?



#..39 >>>..Membership Operators  = Membership operators are used to test if a sequence is presented in an object:


##..       Operator                       Description	                                     Example	
##..          in 	               Returns True if a sequence with the                   
#                                specified value is present in the object                    x in y     
          	
##..        not in	              Returns True if a sequence with the specified
#                                    value is not present in the object                     x not in y



#Check if "banana" is present in a list: using (in) operator 

fruits=["banana","apple","cherry"]
print("apple" in fruits)



#..Check if "pineapple" is NOT present in a list: (using not in) operator
fruits=["apple","banana","grapes"]
print("coconut"  not in fruits )



#..40 >>>...Python Bitwise Operators    #..Bitwise operators are used to compare (binary) numbers:

##              Operator	       Name	                                              Description	                                              Example	
#         	         
##..               &               AND	                                 Sets each bit to 1 if both bits are 1                        	          x & y	
#          	        
##..               |                OR	                                  Sets each bit to 1 if one of two                           
#                                                                                   bits is 1	                                                  x   | y	
#          	         
##..               ^               XOR	                                Sets each bit to 1 if only one of two
#                                                                                   bits is 1	                                                    x ^ y	
#         	                                     
##..               ~               NOT	                                        Inverts all the bits	                                             ~x	
#          	     
##..               <<           Zero fill left shift	                 Shift left by pushing zeros in from 
#                                                                    the right and let the leftmost bits fall off                                    x << 2	
#                  
##..               >>          Signed right shift	              Shift right by pushing copies of the leftmost bit in  
#                                                                  from the left, and let the rightmost bits fall off	                             x >> 2



#..42 >>>...Bitwise operator like =  ( & , | , ^ , ~ , << , >> )  This are the operators and some examples  as well..

#.. using of  "&" operator..
q=3
w=5
print(q  &  w)                         #..yo buje ko xaina ajai try garnu parcha


#..using of  "|" operator.


q=3
w=5
print(q  |  w)


#..using of  "^" operator.


q=34
w=53
print(q  ^  w)


#..using of  "~" operator.
w=73
e=32
print(~w,~e)

#..using of  "<<" operator.
w=44
y=33
print(w<<y)

#..using of  ">>" operator.
w=45
q=66
print(w>>q)


#..43 >>>...Python Operator Precedence   # it means that in order like [ / , * , + , - ] etc..


a=20
s=5
print((a/s)-(a+s))   # Parentheses () = FIRST PRIORITY  and other after that ..

#..Precedence Order...

#...   ()                        = Parentheses                              (ALWAYS FIRST)
 
#...   **                        =  Exponents                                (powers)

#...   * ,  /                    =  Multiplication & Division

#...   + , -                     =  Addition & Subtraction

#...   == , > , <                =  Comparisons                           (equal, greater, less)

#..   and , or, not              =  Basic Logic



#..Examples like this...

##...  ( ** )         =  Exponents   ( " The second number tells you how many times to multiply the first number by itself." )
#..like.

print(2 ** 3)  # 2 × 2 × 2 = 8 (2 appears 3 times)
print(4 ** 2)   
print(5 ** 3)  # 5 have to multiply it self for 3 times like ( 5 * 5 * 5 = 125 )


#..and , or, not  =  Basic Logic

#.. and = 	Returns True if both statements are true
#..or =	Returns True if one of the statements is true
#..or = Reverse the result, returns False if the result is true



#..44 >>>..Python Lists = " Lists are used to store multiple items in a single variable. "
#..some example..

the_list=["apple","banana","cherry"]  # this is the  called list..
print(the_list)



#..45 >>>....Python Collections (Arrays)

# There are four collection data types in the Python programming language:

#... List   "[]"     = is a collection which is ordered and changeable. Allows duplicate members.
#... Tuple   "()"    = is a collection which is ordered and unchangeable. Allows duplicate members.
#... Set      "{}"   = is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#... Dictionary      = is a collection which is ordered** and changeable. No duplicate members.



#..46 >>>..Python - Access List Items
s=["a","s","f","g","d","s"]
print(s[4])


#..47 >>>Negative Indexing = ( -1 refers to the last item, -2 refers to the second last item etc. )
a=["haha","dada","wawa","jaja","qoqo"]
print(a[-3],a[-4])


#..48 >>>..78...Range of Indexes      ( ":" we use slicing method this the sign of slicing method )

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])  # It will retaurn  "cherry", "orange", "kiwi" ... .


#... Note: The search will start at index 2 (included) and end at index 5 (not included).

txt=["s","h","u","v","a","m"]
print(txt[  0 : ])


#..49 >>>...Range of Negative Indexes

txt=["sh","uv","am","ad","hi","ka","ri"]
print(txt[-7:-4])


#..50 >>>..Check if Item Exist
var=["shuvam is a good guy.. "]
if "prank" in var:
    print("yes the name prank in txt ")
else:
   print("I am just kidding..")
   
   
#..51 >>>...Python - Change List Items  (" To change the value of a specific item, refer to the index number:")


a=["shuvam","kriti","raj","hari"]
a[2] = "ram"
print(a)    # Ya  k huncha vane ram saga  raj o replace va ok ho  ( The out put will be like this ['shuvam', 'kriti', 'ram', 'hari'])

#..
name=["a","c","c1","c","d","e"]
name[1]="b"
name[2]="c"
name[3]="d"
name[4]="e"
name[5]="f"

print(name)


#..52 >>>...Change a Range of Item Values

name=["apple","shuvam","banana","cherry","mango"]
name[1:3]=["kriti","maya"]
print(name)        # The output will be like this = ['apple', 'kriti', 'maya', 'cherry', 'mango']


#..53 >>>..Insert Items  ( variable . insert(where , "value")) like ..

##.
name=["shuvam","kriti","ashu"]
name.insert(1,"Adhikari")
name.insert(3,"Adhiakri")
print(name)


#..54 >>>...Python - Add List Items
##..Append Items  ( To add an item to the end of the list, use the append() method:)

name=["name","level"]
name.append("adhikari")
print(name)

#..
name=["shuvam","keitik","raj"]
name.append("adhikari")
name.append("acharya")
name.append("rai")
print(name)


#..55 >>>..Insert Items  ( To insert a list item at a specified index, use the insert() method. )
#..the variable. insert (where to add like index num , " what we are adding ")
#.. like this    the_list.insert(0,"parrot")

the_list=["tiger","lion","hippo"]
the_list.insert(0,"parrot")
print(the_list)

#..
may=["name","boy"]
may.insert(0,"shuvam")
print(may)



#..56 >>>...Extend List  ( a.extend(b) ) variable.1 . extande(variable.2)

##>..
name=["bike","car","bye-cycle"]
chr=["raj","shuvam"]
name.extend(chr)
print(name)


##>..
a=["lalmon","banana","cow","dog"]
b=["eagle","fox","giraf"]
a.extend(b)
print(a)



#..57 >>>..Add Any Iterable  The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).


name=["aashish","ra","shuvam"]
tupl=("name","it","example")
name.extend(tupl)
print(name)



#..58 >>>..Python - Remove List Items         variable.remove("item")
#..Remove Specified Item

name=["shuvam","raj","basnet"]
name.remove("raj")
print(name)


#..59 >>>..Remove Specified Index  ( The pop() method removes the specified index )

#..variable.pop(2) select index item to remove

#..
mna=["raja","ko", "xora "," is ","good"]
mna.pop(2)
print(mna)                #..The output will be ['raja', 'ko', ' is ', 'good']



#..60 >>>..The del keyword also removes the specified index:

#..del variable name  ( it will remove the lise)

##....
name=["del","function","will","delete ","the","name","list"]
del name    

##..yo function le list lai nai delete gardyo...


#..62 >>>....Clear the List

##..variable.clear() it will clear the list and give empty box

##..
this = ["apple", "banana", "cherry"]
this.clear()
print(this)                       #.. the output will be [] this



#..63 >>>...For...Loop Through a List      You can loop through the list items by using a for loop:
#..Syntax  = for i in range():


#..
name=["shuvam","kriti","sajan","wander","women"]
for i in name:
    print(i)



###..
name="shuvam"
for i in name:
  print(i)



#..
this_list = ["apple", "banana", "cherry"]     ##.. yo vane ko tha chadaicha
for i in range(len(this_list)):               ##..for vane ko loop laga ko ho (i) vane ko value ho paxi print garna lai .,range(3) vane ko creates numbers: 0, 1, 2
  print(this_list[i])                                     ##..len(thelist) le chai  kati wata cha count garnna lai help  garcha..



#..
name=["shuvam","riti","babu"]
for i in range(len(name)):
  print(name[i])



#..64 >>>.....Using a While Loop......

num=0
while num <=4:
    print("shuvam")
    num +=1
    
##..

i=0
while (i<4):
    print(i)
    i=i+1

##..
i=0
while i<4:
    print("You are doing well")
    i=i+1
    
##..
i=1
while i<11:
    print(6*i)
    i=i+1
  

#..65 >>>..Python - 
# List Comprehensions..List comprehension is just a shorter way to write the same logic as the traditional for-loop.


##..#SO what is this vanda 

##..yo..and 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]

print(new_list)  # ['apple', 'banana', 'mango']

#.Yo autai ho optional ho jun tarika le garda ni huncha 
##malai yo tareka maan paryo 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)  # ['apple', 'banana', 'mango']



#..66 >>>..###..Python - Sort Lists =  List objects have a sort() method that will sort the list alphanumerically
##.Iportant info ...

##.sort() - A method that works only on lists and changes the original list
##sorted() - A function that works on any iterable (list, tuple, string, etc.) and

##..
name=["shuva","ajaa","cant"]
name.sort()
print(name)

###...
value=(2,43,1,6,7,5,4)
sorted(value)
print(sorted(value))


#..67 >>>..#.Sort Descending...It is the procss of "Arrange things from BIGGEST to SMALLEST in a simple way"
##..lik this...

##..
number=[2,3,12,45,6,54,23]
number.sort(reverse=True)
print(number)


##..
var=["shuvam","aasdish","dacs","python"]
var.sort(reverse=True)        ###...This is the output (thulo bata sanu jane) ['shuvam', 'python', 'dacs', 'aasdish']
print(var)    


##...
name=["shuv","aadi","baspa"]
name.sort(reverse=True)
print(name)


##..
value=["car","jeep","van","prado"]
value.sort(reverse=True)
print(value)



#..68 >>>...Customize Sort Function...❌❌❌❌❌❌❌❌❌❌

def value(i):
  return  abs(i-50)           ##..abs() stands for "absolute value"  (positive distance from zero)
the_list=[100,31,44,65]
the_list.sort(key=value)
print(the_list)


#..69 >>>.Case Insensitive Sort..(" ↑ uppercase first   ↑ lowercase second")
##..
my_list=["Shuvam","adhikari","is","A","good","Man"]
my_list.sort()
print(my_list)

##..

variable=["Hi","my","Name","Is","shuvam","adhikari"]
variable.sort()
print(variable)


#..70 >>>...   variable.sort(key= str.lower)  
##..
var=["HU","SASA","asg","cat"]
var.sort(key=str.lower)
print(var)

##...
variable=["nana","ASA","bsg","cat"]
variable.sort(key=str.lower)
print(variable)


#..71 >>>..Reverse Order   (  reverse()  )
##.
name=["aabishek","raj","hari","syam"]
name.reverse()
print(name)


##...
var=["a","s","w","e","t"]
var.reverse()
print(var)


#..72 >>>....Python - Copy Lists  =  Use the copy() method
##...You can use the built-in List method copy() to copy a list.

###..
var=["shuvam","raja","rara"]
my_list=var.copy()             ##..The out put will be like this ['shuvam', 'raja', 'rara']
print(my_list)            ##..  You can use the built-in List method copy() to copy a list.


##...
value=["shu","haha","dada","kaka"]
output=value.copy()
print(output)


#..73 >>>..Use the list() method  .. Another way to make a copy is to use the built-in method list().

neo=["shu","uhs","kook"]
var=list(neo)              ##..The out put will be like this  ['shu', 'uhs', 'kook']
print(var)

##..
name=["apple","potato"]
output=list(name)
print(output)


###...
animal=["tiger","lion","croco"]
animal_copoy =animal.copy()           ##..The out put will be like this ['tiger', 'lion', 'croco']
print(animal_copoy)


###..
anime=["onepiece","jojo","demon_slayer"]
character=anime.copy()
print(character)



#..74 >>>..Use the slice Operator..     Make a copy of a list with the : operator:

anme=["haha","code","dodo"]
var_ie=anme[:]
print(var_ie)                     ##The output will be like this ['haha', 'code', 'dodo']


##..75.>>>..##.....Python - Join Lists      One of the easiest ways are by using the + operator.

a=["a","s","d"]
b=[1,2,3]
c=a+b
print(c)


a=["saaa","kask","dasa"]
b=[2,3,4,5]
c=(a+b)
print(c)

##..76.>>>..Append list2 into list1:

list_1 = ["a", "b" , "c"]
list_2 = [1, 2, 3]

for i in list_2:
  list_1.append(i)
print(list_1)



##..77.>> extend()  the purpose is to add elements from one list to another list:

var=["as","you","can"]
var_2=[1,2,33,4]
var.extend(var_2)
print(var)


##..
rae=["sgu","saa","dkdk"]
rae_2=[1,2,34,4]
rae.extend(rae_2)
print(rae)


##..78.>>..Python - List Methods
###.. List Methods
###.... Python has a set of built-in methods that you can use on lists.

##....   Method	          Description
###...   append()	      Adds an element at the end of the list
##....   clear()	      Removes all the elements from the list
##....   copy()	        Returns a copy of the list
##....   count()	      Returns the number of elements with the specified value
##....   extend()	      Add the elements of a list (or any iterable), to the end of the current list
##....   index()	      Returns the index of the first element with the specified value
##....   insert()	      Adds an element at the specified position
##....   pop()	        Removes the element at the specified position
##....   remove()	      Removes the item with the specified value
##....   reverse()	    Reverses the order of the list
##....   sort()	        Sorts the list


##..1. append() - Add single element at end
fruits=["apple","banana"]
fruits.append("cherry")
print(fruits)                 ##..The output will be like this ["apple", "banana", "cherry"]


##..2. extend() - Add multiple elements at end
name=["shuvam","raja"]
name.extend(["kaka","haha"])
print(name)                     ##..The output will be like this ['shuvam', 'raja', 'kaka', 'haha']


##..3. insert() - Add element at specific position
place=["ktm","jhapa","lalitpur"]
place.insert(1,"hetauda")
print(place)                         ##..The output will be like this ['ktm', 'hetauda', 'jhapa', 'lalitpur']


##..4. remove() - Remove first matching value
name=["shuva","ram","kaka"]
name.remove("ram")
print(name)                         ##..The output will be like this ['shuva', 'kaka']


##..5. pop() - Remove element at index (or last)
name=["shuva","kaku","gaga","naga"]
name.pop(2)
print(name)                       ##..The output will be like this  ['shuva', 'kaku', 'naga']


##..6. clear() - Remove all elements..
animal=["tiger","lion","hippo","snake"]
animal.clear()
print(animal)                    ##..The output will be like this  []

##...7. index() - Find position of element

anme=["shuva","raja","wowo","rajiv"]      #..0,1,2,3  this are the index inside the  list [ ]
output=anme.index("raja")
print(output)                    ##The output will be like this  " 1 "

##..8. count() - Count occurrences    #..it will count   the value we given by
num=[1,2,3,4,3,6,3,3,3]
output=num.count(3)      
print(output)              ##The output will be like this "5"  there is 5 "3" inside the list 


##..9. copy() - Create shallow copy
name=["animal","daam","fafa"]
output=name.copy()
print(output)              ##..The output will be like this ['animal', 'daam', 'fafa']


##..10. reverse() - Reverse list order
val=[1,2,3,4,5,6,7,8]
val.reverse()
print(val)               # ##..The output will be like this [8, 7, 6, 5, 4, 3, 2, 1]


##..11. sort() - Sort list

grades = [85, 92, 78, 90]
grades.sort()                # [78, 85, 90, 92]  yesle sano bata thulo ma lancha 
grades.sort(reverse=True)    # [92, 90, 85, 78]  yesle thulo bata sano ma lancha 


##..79..>>..Tuple

my_tuple = ("apple", "banana", "cherry")  #..This is tuple( )
print(my_tuple)


#.
##...Tuple Items - Data Types
##..Example
##..  String , int and boolean data types:
tuple_1 = ("apple", "banana", "cherry")     #..string
tuple_2 = (1, 5, 7, 9, 3)                   #..int
tuple_3 = (True, False, False)              #..bollen


##..
##..Python Collections (Arrays)

#..There are four collection data types in the Python programming language:

#..List   =   is a collection which is ordered and changeable. Allows duplicate members.
#..Tuple  =   is a collection which is ordered and unchangeable. Allows duplicate members.
#..Set    =   is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#..Dictionary     is a collection which is ordered** and changeable. No duplicate members.



##..80>>>..##..Python - Update Tuples   /  Tuples are unchangeable,
##.
##.
auto=("car","jet","bike","tractor")   ##..Tuple immmutable va ko reason le  tupple lai list  banaoune list() function use gare ra 
value=list(auto)           ##..Yo ma gare ko jasto ..
value[2]="bullet"            ##.. Yo bullet list  ma add garyo value[2] vane ko chai "bike" ko sata ma bullet add garye ko ho ..
auto = tuple(value)       ##..Auto lai feri tuple ma convert gareko
print(auto)            ##..Ani print gareko 

##..
var_1=("tiger","lion","elephant")
var_2=list(var_1)
var_2[1]="giraffe"
var_1=tuple(var_2)
print(var_1)


##.81>>..##....Using Asterisk*..( * )  to unpack the tuple

name_list=["shuvam","frog","dog","bird","kalo","billi"]
(value_1,value_2,*value_3)=name_list
print(value_1)
print(value_2)
print(value_3)


##..
names=("suvam","kriti","kaka","daugesh_vai","messi","ronaldo","pepe")
(my_name,my_real_name,player_name,*others)=names
print(my_name)
print(my_real_name)
print(player_name)
print(others)


##....

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)         #..The output will be like this  apple
print(yellow)       #..The output will be like this  banana
print(red)         #..The output will be like this  ['cherry', 'strawberry', 'raspberry']

## Think of it like this:
## First, assign "apple" to green
## Then assign "banana" to yellow
## Then take all the remaining fruits and put them into a list called red


##...82>>..Python - Loop Tuples....You can loop through the tuple items by using a for loop.

the_tuple=("shuvam","sag","masa")
for i in the_tuple:
  print(i)


##..83>>..##..Use the range() and len() functions to create a suitable iterable.
val_3=("value","of","python")
for i in range(len(val_3)):
    print(val_3[i])

##..
ball=("value","is the","best","value")
for i in range(len(ball)):
    print(ball[i])


##..84.>>..Using a While Loop




##.85.>>##..Multiply Tuples....If you want to multiply the content of a tuple a given number of times, you can use the * operator:

fruits=("apple","cherry","banana")
value=fruits*2
print(value)


##86.>>###...Python - Join Tuples

name=("shuvam" , "adhikari") 
age=23,                            ##..Yo 23  paxi ko 23, comma ko k use ho berse ??

total= name + age
print(total)               ##..The output will be like this ('shuvam', 'adhikari', 23)


##...87>>..Python - Tuple Methods...
# #..Tuple Methods
#.. Python has two built-in methods that you can use on tuples.


#      Method                      	Description
#..   count()	                 Returns the number of times a specified value occurs in a tuple
#..   index()               	 Searches the tuple for a specified value and returns the position of where it was found


##.88.>>..##Python Sets
#..create a Set
myset = {"apple", "banana", "cherry"}
print(myset)


##..##..Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
 

##..Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


##..
##..Example     True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


##..Example   False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


##..
##..The set() Constructor
name=("shuvam","raja")
out_put=set(name)
print(out_put)


##.....
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



##..Check if "banana" is present in the set:

the_set={"cherry","banana","apple","coconut"}
print("banana"in  the_set)                          ##..This will return True
print("coconut"in the_set)                          ##..This will return True as well


##..
name={"shuvam","srk","salman","akshay","ranbir","rakhi"}
print("srk" in name)
print("shuv" in name)
print("kriti" in name)

###...Check if "banana" is NOT present in the set:

name={"suva","raja","sujan","babu","namu"}
print("sujan" not in name)                     ##..This will return False


##..##...update() method.  in sets to add multiple items to a set
name={"shuvam","kriti","ram"}
cast={"adhikari","aacharye","karki"}
name.update(cast)
print(name)

###..Python - Remove Set Items    ..   To remove an item in a set, use the remove(), or the discard() method.

##..remove() method:
name={"shuvam","raj","kashyab"}
name.remove("shuvam")
print(name)

##...
car={"porche","prado","tata"}
car.remove("tata")
print(car)


##..###...discard() method:

name={"shuvam","saam","lala"}
name.discard("shuvam")
print(name)


###..
balls={"footbal","basketbal","tennisbal"}
balls.discard("tannisbal")
print(balls)


##..
##..
family={"shuvam","animal='rht.adk' ","mithu","prakriti","swikriti"}
name=list( family)
family.discard("animal='rht.adk'")
print(family)
for i in name:
    print(i + " " +"adhikari") 
print(i)



##..##..The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


##..Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

##.89.>>..Python - Loop Sets
##..Python - Loop Sets     You can loop through the set items by using a for loop:

fruits = {"apple", "banana", "cherry"}
for i in fruits:
    print(i)


##.90.>>......# python -  Join Sets

# Join Sets
# There are several ways to join two or more sets in Python.

# The   union() and update()   =      methods joins all items from both sets.
# The   intersection()         =      method keeps ONLY the duplicates.
# The   difference()           =      method keeps the items from the first set that are not in the other set(s).
# The   symmetric_difference() =      method keeps all items EXCEPT the duplicates.


##...# ##..Only learn these 4 operators (most important):

#....(|)  = Union (combine all unique items)

#.....(&) = Intersection (only common items)

#.....(-) =  Difference (items in first set only)

#.....(^) = Symmetric Difference (items in one set or the other, not both)


##..Union  "|"--- The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1| set2
print(set3)


##..Join Multiple Sets  --  Join multiple sets with the union() method:
##..union() method can take more than two arguments:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 | set4
print(myset)                            ##..The output will be like this {1, 2, 3, 'cherry', 'John', 'b', 'Elena', 'apple', 'bananas', 'a', 'c'}


##..Join a Set and a Tuple  ---  The union() method allows you to join a set with other data types, like lists or tuples.

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x | set(y)
print(z)


##..Update --- The update() method inserts all items from one set into another.
##..The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


##...Intersection  = "&"
#... " & " method returns It gives you ONLY the items that appear in BOTH sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

##...

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

##...The intersection_update() method will also keep ONLY the duplicates,
#.."&="  keeps only matching items between two sets.


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1 &= set2
print(set1)


##..Difference
#..The difference() method returns a set that contains the difference between two or more sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

##...Use the difference_update() method to remove the items that are present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


##..You can use the ^ operator 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)


##..
set_1={"shuvam","raj","kashyab","sujan"}
set_2={"shuvam","sajyan","raj","kashyab"}
out_put = set_1 ^ set_2
print(out_put)                                  ##..This will print {'sajyan', 'sujan'}



##..The symmetric_difference_update()

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1 ^= set2
print(set1)


##.91.>>..Python frozenset  ❌❌❌❌❌❌❌❌❌


##..92.>>...#   ...Set Methods...


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



##..

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



##..93.>>




##.94.>>


##.95.>>


##.96.>>


##.97..>>


##.98.>>


##.99.>>


##.100>>


