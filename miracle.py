""""
def greeting_mine(name="Vin"):
    print(f"Hello,{name}. Enjoy")
print(greeting_mine("Charles"))

def default_menu(food="Spaghetti"):
      print(f"The " +"" + food + " is ready")
print(default_menu())

print("..................................................")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...")
print("VARIABLE SCOPE")

name = "Joe"
def greeting():
     print(f"Hello, {name}")
print(greeting())

name = "Vincent"
def greeting(name):
     print(f"Love you, {name}")
print(greeting(name))
print(greeting("Sophie"))

evil_monster = "Dracula"

def tukio():
     print(f"{evil_monster} is trying to kill me.")
print(tukio())

def tukio2():
     evil_one = "Lucifer Christ"
print(tukio2() and "has come")

print(tukio2())
print("................................")
print("GLOBAL KEYWORD")

best_coder = "Vincent Rugundu"

def who_is_he():
    global best_coder
    best_coder = "Irungu"
print(who_is_he())
print(best_coder)
"""

""""
print("CONTROL FLOW :OPERATORS")
print("Comparison Operators")
print("1" == 1)
print(1 == 1)
print(1.0 == 1)
print(3 > 5)
print(5 >= 5)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Logical operators")
print(True and True)
print(False and False)
print(False and True)
print(True and True)
print(False or False)
print(False or True)
print(not True)
print(not not True)
"""
""""
print("...................................................")
print("CONTROL FLOW :Conditional Statements")

print("If/else statements")

brother = "Aleko"
if brother == "Aleko":
    bro = "Vinnie"
elif brother == "Kerash":
    bro = "Irosh"
elif brother == "Alex":
    bro = "Vincent"
elif brother == "Kiragu":
    bro = "Irungu"
else:
    bro = "Vincent Irungu Rugundu"
print (brother)

brother = "Aleko"
def who_is_sibling(brother):
    if brother == "Aleko":
        return "Vinnie"
    elif brother == "Kerash":
        return "Irosh"
    elif brother == "Alex":
        return "Vincent"
    else:
        return"Vincent Irungu Rugundu"

print(who_is_sibling(brother))
print(who_is_sibling("Aleko"))
print(who_is_sibling("Kerash"))
print(who_is_sibling("Alex"))
print(".........................................")
print("TRUTHY AND FALSY VALUES")

def love(girl):
    if girl:
        #if the value is truthy
        print("yep!")
    else:
        #if the value is falsy
        print("nope!")

print(love(False))
print(love(None))
print(love(True))
print(love(""))
print(love(0))
print(love("0"))




print("........................................")
print("Conditional Expressions")
"""
"""
age = 1
is_baby ="baby" if age < 2 else "not baby"

print (age(2))
"""
"""
#Try and Expect Statements

def divison (num1, num2):
    try:
        quotient = num1/num2
        print(quotient)
    except:
        print("An error occured")

print (divison(3,4))

def divison(num1, num2):
    try:
        quotient = num1/num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to zero")
    except TypeError:
        print("Error: input must be of type int or float")

print(divison(3,0))
print(divison(0,3))
print(divison("2",3))
"""

"""
print("...............................................")

# Try, Except and Finally 

def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: mum2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")
print(divide(10,2))
print(divide(600,2))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("DICTIONARY MAPPING")

dog = "cuddly"

if dog == "hungry":
    owner = "Refilling food bowl."
elif dog == "thirsty":
    owner = "Refilling water bowl."
elif dog == "playful":
    owner = "Playing tug-of-war."
elif dog == "cuddly":
    owner = "Snuggling."
else:
    owner = "Reading newspaper."
print(owner)

#Conditional Statements

name ="cuddly"
def dog_catch(name):
    if name == "hungry":
         return "Refilling food bowl."
    elif name == "thirsty":
        return "Refilling water bowl."
    elif name == "playful":
        return "Playing tug-of-war."
    elif name == "cuddly":
        return "Snuggling."
    else:
        return "Reading newspaper."
print(dog_catch("cuddly"))
print(dog_catch("thirsty"))
print(dog_catch("playful"))
print(dog_catch("hungry"))

#OR

dog_state = "cuddly"

dict_map= {
    "hungry": "Refilling the food bowl boy.",
    "thirsty": "Drinks coming your way boy",
    "playful": "Be there for games in a sec",
    "cuddly": "I am coming to snuggle.",
}
print(owner = dict_map.get(dog,"Reading newspaper."))
"""
"""
# Extra Practise
def admin_login(username, password):
    if (username == "admin") or (username == "ADMIN") and (password == "12345"):
        return "Access granted"
    else:
        return "Access denied"
print(admin_login("ADMIN", "12345"))
print(admin_login("vincent", "65432"))
print(admin_login("admin", "12345"))
print(admin_login("admin","11234"))
print(".....................................")

def hows_the_weather(temp):
    if temp < 40:
        return "It's brisk out there!"
    elif temp >=40 and temp <=65:
        return "It's a bit chilly out there!"
    elif temp > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
print(hows_the_weather(0))
print(hows_the_weather(20))
print(hows_the_weather(50))
print(hows_the_weather(70))
print(hows_the_weather(95))

print("....................................................")

def fizzbuzz(num):
    if (num %3 == 0) and (num %5 == 0):
        return "FizzBuzz"
    elif (num %3 == 0):
        return "Fizz"
    elif (num %5 == 0):
        return "Buzz"
    else:
        return num
    pass
print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(9))
print(fizzbuzz(10))
print(fizzbuzz(7))
print(fizzbuzz(15))

print("..........................................")

def calculator(opper, num1, num2):
    if (opper == "+"):
        return num1 + num2
    elif (opper == "-"):
        return num1 - num2
    elif (opper == "*"):
        return num1 * num2
    elif (opper == "/"):
        return num1 / num2 
    else: 
        return "Invalid Operation"
    
print(calculator("+", 2, 3))
print(calculator("-", 3, 2))
print(calculator("*", 2, 3))
print(calculator("/", 3, 2 ))
print(calculator("add", 2, 3))
"""
print("..................................................................")

"""
print("CONTROL FLOW: LOOPS")
#Baic Loops
i = 0
while i < 10:
    print("Looping!")
    i += 1
print("oooooooooooooooooooooooooooooooooo")
#Looping with for

for i in range(10):
    print("Looping!")
    print(f"i is: {i}")
"""
"""
list_abc = [2,3,4,5,6]
for i in list_abc:
    print("New loop!")
    print(f"I is,  {i} digit on", i in list_abc)

print(".............................................................")

#LIST COMPREHENSIONS
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

inch_heights = list()
for height in player_heights:
    inch_height = height * 7920
    inch_heights.append(inch_height)

print(inch_heights)

#OR
inch_heights = [height *7920 for height in player_heights]
print(inch_heights)


def happy_new_year():
    #code here
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

print(happy_new_year())

list_integers = [1, 2, 3, 4, 5]
square_integers = []
for num in list_integers:
    square_integers.append(num**2)
    
print(square_integers)
"""
"""

def fizzbuzz():
    for num in range(1, 101):
      if num %3 == 0  and num %5 == 0:
          print("FizzBuzz")
      elif num %3 == 0:
          print("Fizz")
      elif num%5 == 0:
          print("Buzz")
      else:
          print(num)
print (fizzbuzz())
    
"""
"""
print(">.......................................................................")
        
#Sequences

magic_sequence = [0, 3, 6, 9, 9, 9,  12, 15, 18, 21, 24, 27, 30] 
print(magic_sequence[3])  
print(magic_sequence[1:5])
print(magic_sequence[1:9:5])
print(len(magic_sequence))
print(min(magic_sequence))
print(max(magic_sequence))
print(magic_sequence.index(9))
print(magic_sequence.count(9))

"""
"""
#Lists
#Sorting lists
energy_list = [3,12,18,81,27,72,36,63,45,54,90,9,6 ]
energy_list.sort()
print(energy_list)

food_fields = ['Avocado', 'Tnagerine', 'Brocolli', 'Warer-melon']
food_fields.sort()   
print(food_fields)
#Ascending order
my_list = ['This is a long sentence', 'Word', 'z']
my_list.sort(key = len)
print(my_list)
#Descending order
my_list.sort(key = len, reverse = True)
print(my_list) 

my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]
def sort_tuple(tuple_value):
    return tuple_value[1]
my_list.sort(key=sort_tuple)
print(my_list)

#Sorted functions
vin_list = [3,6,4,2,1,5,9,3,6,18,27]
sorted_list = sorted(vin_list)
print(vin_list)
print(sorted_list)

fam_mem = ['Vin', 'Ale', 'Dad', 'Mom', 'Njeri']
sorted_list = sorted(fam_mem, key=len, reverse=True)
print(fam_mem)
print(sorted_list)
"""


""""
customer_ratings = [1,2,5,7,8,9,12,16,12,13,43]
customer_ratings[0] = None
print(customer_ratings)
print(customer_ratings)

#Appending
customer_ratings = [0,1,2,3,4,5,6,7,8,9]
customer_ratings.append(10)
print(customer_ratings)

#Inserting
millions_future = [3,6,8,43,8,35,8,4,77]
millions_future.insert(50, 'Str')
print(millions_future)
millions_future.insert(999, "Str2")
print(millions_future)

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del(my_list[0])
print(my_list)
my_list.pop()
print(my_list)
my_list.remove('d')
print(my_list)
"""
"""
#Tuples-are immutable thus cannot destructive trans cannot be done on them.

for n in range(10):
    print(n)
print('..........................')
for n in range(1,18,2):
    print(n)


vin_string = 'Vin you can do it!'
for char in vin_string:
    print(char)
print("...............................")
print(vin_string[0])
print(vin_string[1])
print(vin_string[2])
print(vin_string[3])
print(vin_string[0])
print(vin_string[12])
print(vin_string.upper())
print(vin_string.lower())
print(vin_string.title())

vin_word = "We did it!"
vin_word.upper()
print(vin_word.upper())

def print_fibonacci(length):
    fibonacci_sequence = []
    if length > 0:
        fibonacci_sequence.append(0)
        if length > 1:
            fibonacci_sequence.append(1)
            if length > 2:
                for i in range(2, length):
                    fibonacci_sequence.append(fibonacci_sequence[i -1] + fibonacci_sequence[i-2])
print(print_fibonacci(6))


#List Comprehension
squared = list()
for n in range(1, 5):
    squared.append (n**2)

print(squared)

squared2 = [(n**2) for n in range(2,9)]
print(squared2)

#Generator Expressions

seqnum = range(1,7)
squared_lc = [n**2 for n in seqnum]
squared_gen = (n**2 for n in seqnum )

for n in squared_lc:
    print(n)

for n in squared_gen:
    print(n)

print(squared_gen)
print(squared_lc)




even_namabari = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,19,20,21]
return_evens = list()
for n in even_namabari:
        if n %2 == 0:
            print(n)
            return_evens.append(n)
        
        
print(return_evens)

words = ["Money", "Cash", "Rules", "Everything"]
make_exclamation = []
for tuple in words:
      make_exclamation.append(tuple + "!")


print(make_exclamation)


#DICTIONARIES

new_word = {
     "python-coding": "Python has classes which are defined wireframes of objects. Python supports class inheritance. A class may have many subclasses but may only inherit directly from one superclass.",
     "Vincent": "The guy from Atlantis"
}

print(new_word["Vincent"])

Vincent_engineer ={
    "languages": ["JavaScript","React JS","HTML"],
    "certifications": ["Moringa School Certificate of Completion"],
    "experience": "3 months and counting!",
}

print(Vincent_engineer["experience"])
print(Vincent_engineer["languages"])
print(Vincent_engineer["certifications"])


size_to_ounce_map ={
    "tall":12,
    "grande":16,
    "venti":9
}

print(size_to_ounce_map["tall"])

def pour_coffee(size):
    size_to_ounce_map ={
    "tall":12,
    "grande":16,
    "venti":9
}
    return size_to_ounce_map[size]
print(pour_coffee("tall"))
print(pour_coffee["Jumbo"])


print("...............................")
def pour_coffee(size):
    size_to_ounce_map ={
    "tall":12,
    "grande":16,
    "venti":9
}
    return size_to_ounce_map.get(size, "Please eneter a avalid cup size.")
print(pour_coffee("tall"))


my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
print([key for key in my_dict])
#Finding a value of a dictionary 
print([my_dict[key]for key in my_dict])
print([item for item in my_dict.items()])
print([key for key, value in my_dict.items()])
print([value for key, value in my_dict.items()])




family_names = {
    "Vincent":"Irungu",
    "Alex":"Kiragu",
    "Francis":"Rugundu",
    "Judy":"Nyambura"
}

print([key for key in family_names])
print([item for item in family_names.items()])
print([key for key, value in family_names.items()])
print([value for key, value in family_names.items()])

#SETS
print("............................................")

vin_set = set([0,3,6,9])
#or
vin_set={0,3,6,9}

my_list = [1, 2, 1, 3, 2]
set(my_list)
print(my_list)
print(set(my_list))
my_string = "the big red cat ate the fat rat"
set(my_string)
print(my_string)
print(set(my_string))

set(range(1, 10)) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
print(set_1 & set_2)#shows intersection what both sets have in common
print(set_1 - set_2)# shows disjunction what these sets don't have in common, or shows the unique elements in set 1 relative to set2
print(set_2 - set_1)
spell = "In energy, all is attainable, believe and receive."

"""            

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 8,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]


def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

print(get_names(spicy_foods))

def get_spiciest_foods():
    return [food for food in spicy_foods if food["heat_level"] > 5]
print(get_spiciest_foods())

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')
print(print_spicy_foods(spicy_foods))

    







