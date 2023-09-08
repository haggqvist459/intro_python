# Operators and operations


# Arithmetic operators, numerical calculations or string concatenation 
# +, -, *, /, %, //, **
print("Arithmetic operators")
num_value = 420
print(num_value)
num_value = num_value + 7
print(num_value)
# modulo operation, provides the remainder of a division 
print(num_value % 3)
# floor operation, discards the remainder of a division
print(num_value // 3)
# calculate num_value to the power of 2
print(num_value ** 2)
# num_value has not changed since adding 7 
print(num_value)

# String concatenation
first_name = "Tim"
middle_name = "Ilmari"
print(first_name + " " + middle_name)
name = first_name + " " + middle_name
print(name)
print("__________")
# Assignment operators, assign values to variables
#  =
#  +=. -=, *=, /=, %=, //=, **=
print("Assignment operators")
another_num_value = 200
print(another_num_value)
# same as another_num_value = another_num_value = 220
another_num_value += 220
print(another_num_value)
another_num_value -= 220
print(another_num_value)
# string assignment  
another_name = "tim"
print(another_name)
another_name += " ilmari"
print(another_name)
print("__________")


# Comparison operators, compares two values, tests equality 
# Can be numerical, string or boolean values 
#  ==, !=, >, >=, <, <=
# >, >=, <, <= returns true or false based on the evaluation
# ==, != tests equality, also returns a bool value 
print("Comparison operations")
result = 5 > 2 
print(result)
print(type(result))
print(5 == 2)
print(5 != 2)
print(5 == 5.0)
# Case sensitivity
# Will evaluate to false, since "Tim Ilmari" does not equal "tim ilmari"
print(name == another_name)
a = "a"
a_ = "A"
print(a == a_)
# Also evaluates to false, as "b" is further along in the alphabet, and has a higher value. 
b = "b"
print(a > b)
print("__________")


# Logical operators, test additional conditions 
# Mostly used on booleans 
# not, or, and 
print("Logical operations")
# reverse a boolean, not
random_bool_value = False
print(random_bool_value)
random_bool_value = not random_bool_value
print(random_bool_value)
first_num = 420
second_num = 420
# evaluates to true, since both first_num and second_num evaluates to true 
print(first_num == 420 and second_num == 420)
# evaluates to false, since second_num evaluates to false 
print(first_num == 420 and second_num == 421)
# evaluates to true since at least one evaluates to true 
print(first_num == 420 or second_num == 421)




# Other operators 
# Ternary operator: if else 
# Identity: is, is not 
# Membership: in, not in 
# Bitwise: &, |, ^, ~, <<, >>



