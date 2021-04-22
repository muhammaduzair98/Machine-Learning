**White Space Formatting**

for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
print("Looping in Process")



twoPlusThree = 2 + 3
                 

**Modules**

import re #Regular Exp
my_regex = re.compile("[0-9]+", re.I)

import matplotlib.pyplot as plt #GraphLib

**Arithmetics**

5/2

5//2

**Functions**

def double(x):
    """this is where you put an optional docstring
    that explains what the function does.
    for example, this function multiplies its input by 2"""
    return x * 2


def apply_to_one(f):
    """calls the function f with 1 as its argument"""
    return f(1)

my_double = double
x = apply_to_one(my_double)


y = apply_to_one(lambda x: x + 4)

**Strings**

single_quoted_string = 'data science'
double_quoted_string = "data science"


tab_string = "\t"
len(tab_string)


not_tab_string = r"\t"
len(not_tab_string)

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

**Exceptions**

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

**Lists**

integer_list = [1, 2, 3]
heterogenous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogenous_list, [] ]

list_length = len(integer_list)
list_sum    = sum(integer_list)

x = range(10)
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
first_of_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

1 in [1, 2, 3]
0 in [1, 2, 3]

x = [1, 2, 3]
x.extend([4, 5, 6])

x = [1, 2, 3]
y = x + [4, 5, 6]

x = [1, 2, 3]
y = x + [4, 5, 6]

x, y = [1, 2]

_, y = [1, 2]

**Tuples**

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

**Dictionaries**

empty_dict = {}
empty_dict2 = dict()
grades = {"Joel" : 80, "Tim" : 95}

joels_grade = grades["Joel"]

joes_has_grade = "Joel"in grades
kate_has_grade = "Kate" in grades

joels_grade = grades.get("Joel", 0)
Kates_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No One")

tweet = {
    "user" : "Joelgrus",
    "test" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}


tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

"user" in tweet_keys
"user" in tweet

**Sets**

s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s)
y = 2 in s
z = 3 in s

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_set)
distinct_item_list = list(item_set)

**Control Flows**

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

parity = "even" if x % 2 == 0 else "odd"

**Loops**

x = 0
while x < 10:
    print(x, "is less than 10")    
    x += 1

for x in range(10):
    print(x, "is less than 10")

for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)

**Boolean**

one_is_less_than_two = 1 < 2
true_equals_false = True == False

x = None
print(x == None)
print(x is None)

**Sorting**

x = [4, 1, 2, 3]
y = sorted(x)
x.sort()

**List Comprehensions**

even_numbers = [x for x in range(5) if x % 2 == 0]
squares      = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]

even_numbers = [x for x in range(5) if x % 2 == 0]
squares      = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]

zeroes = [0 for _ in even_numbers]

pairs = [(x, y)
          for x in range(10)
          for y in range(10)]
                

**Randomness**

import random

four_uniform_randoms = [random.random() for _ in range(4)]


random.seed(10)
print(random.random())
random.seed(10)
print(random.random())

random.randrange(10)
random.randrange(3, 6)

**Regular Expressions**

up_to_ten = range(10)
print(up_to_ten)

my_best_friend = random.choice(["Alice", "Bob", "Charlie"])

lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)

four_with_replacement = [random.choice(range(10))
                          for _ in range(4)]