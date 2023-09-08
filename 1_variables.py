# In python, variables takes on None as value if no value is assigned. 
# Variable types are flexible, can change if necessary 
# Types can be custom


# Bool
random_bool_value = False 
print(random_bool_value)
random_bool_value = True
print(random_bool_value)
# Bool value can be determined by mathematical expressions 
random_bool_value = 5 > 6
print(random_bool_value)



# Int
random_num_value = 5 
print(random_num_value)
# Float
another_num_value = 0.5
print(another_num_value)
# Int can turn into Float since variable types are flexible
random_num_value = random_num_value - another_num_value
print(random_num_value)

# String
name = "Tim"
print(name)
# Since Tim and tim contain different characters, values are considered different
# Single or double quotes can be used
another_name = 'tim'
print(another_name)
# Simple way of changing the value of a String
name = "Tim" + " Ilmari"
# Bad convention, stick to either single or double quotes 
name = name + ' Haeggqvist'
print(name)

# type() can determine the variable type 
print(type(random_bool_value))
print(type(random_num_value))
print(type(name))

