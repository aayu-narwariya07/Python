# single-quoted strings 
single_quoted = 'Hello, World!'
print("Hello, World")

# string operations with single-quoted string 
lenght =len(single_quoted)
upper_case =single_quoted.upper()
lower_case = single_quoted.lower()
contains_substring = 'World' in single_quoted

#printing results
print("single-quoted string:", single_quoted)
print("Length of the string:",lenght)
print("Uppercase version:",upper_case)
print("Lowercase version:",lower_case)
print("Contains 'World':",contains_substring)

# Double-quoted strings
double_quoted ="Edunet is awesome!"

length = len(double_quoted)
replace_text = double_quoted.replace("awesome", "great")
split_words =double_quoted.split()
# printing results 
print("\nDouble-quoted string:",double_quoted)
print("length of the stirng:",length)
print("String after replacement:",replace_text)
print("World in the string:",split_words)

# Integer values 
int1 = 10 
int2 = -5
int3 = 0 
# converting integer to floats 
float1 = float(int1)
float2 = float(int2)
float3 = float(int3)

print("Original integer values:")
print("int1 =",int1)
print("int2 =", int2)
print("int3 =", int3)
print("\nconverted float values:")
print("float =",float1)
print("float2 =", float2)
print("float3 =", float3)

# Define a string and an integer 
string_value = "The number is "
integer_value = 42

# convert the integer to a string using explicit conversion
integer_as_string = str(integer_value)
# concatenate the string and the converted integer 
result = string_value + integer_as_string
# print the result 
print(result)
