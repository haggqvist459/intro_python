
random_bool_value = False 
random_num_value = 5 
random_dec_value = 4.20
name = "Tim"
name_none = None


# convert int to str
print("String conversion")
str_num_value = str(random_num_value)
str_bool_value = str(random_bool_value)
# random_num_value and str_num_value might look the same, but have different types 
print(random_num_value)
print(type(random_num_value))
print(str_num_value)
print(type(str_num_value))
# Converting booleans to string
print(str_bool_value)
print(type(str_bool_value))
print("__________")


# Convertion to bool, bool()
# 0 is considered false, 1 is considered true 
print("Bool conversion")
print(bool(0))
print(bool(1))
# Everything except the exact value of 0 will evaluate to true 
print(bool(random_num_value))
# Strings will also evaluate to true
print(bool(name))
# "False" will evaluate to true since it's a string and has a value that does not equal 0. 
print(bool("False"))
# Variables with None value will evaluate to false 
print(bool(name_none))
print("__________")


# Conversion to int, int()
print("Int conversion")
print(int("1"))
# Floats will have its decimal chopped off unless libraries are used 
print(int(random_dec_value))
# Converting bool to int
# False values will convert to 0
print(int(False))
# True values will convert to 1 
print(int(True))
# Taking a number value higher than one, converting it to a boolean which evalues to true and then back to an int will turn it into a 1.
print(int(bool(random_num_value)))
# converting a variable with None to int throws error, since int() argument can not be None
# print(int(name_none))
print("__________")


# Conversion to float 
print("Float conversion")
print(float("1"))
print(float(random_num_value))
print(float(random_bool_value))
print(float(True))
print("__________")
