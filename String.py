#  creating and accessing string
my_string = "Hello, Edunet!"
print("original string", my_string)
print("first char", my_string[0])
print("last char", my_string[-1])
# string concatention and repettion
str1 = "Edunet"
str2 = "founation"
concat_srt = str1 + " " + str2
repeated_str = concat_srt * 3
print("concatenated string", concat_srt)
print("repeated string", repeated_str)
# string case manipulation
upper_str = my_string.upper()
lower_str = my_string.lower()
title_str = my_string.title()
swapcase_str = my_string.swapcase()
print("uppercase:", upper_str)
print("lowercase:", lower_str)
print("title case:", title_str)
print("swap case:", swapcase_str)
# searching in string
substring = "Edunet"
found_index = my_string.find(substring)
if found_index != -1:
    print(f"substring '{substring}' found at index {found_index}")
else:
    print(f"substring '{substring}' not found")
# replacing substring
new_string = my_string.replace("Edunet", "world")
print("string after replacment:", new_string)
# string formatting
name = "ramar"
age = 25
formatted_str = f"my name is {name} and i am {age} years old."
print("Formatted string :", formatted_str)
# trimming and padding string
padded_str = my_string.center(20, "*")
trimmed_str = "   extra space   ".strip()
print("padded string:", padded_str)
print("trimmed string:", trimmed_str)
# splitting and joining string
set = "python is a sencetive lunguage"
words = set.split()
joined_sentence = '=' .join(words)
print("splitted words:", words)
print("joined sentence:", joined_sentence)
# counting characters
char_count = my_string.count("l")
print(f"character 'l' appears {char_count} item in the string ") 
# checking string properties
is_alpha = "Hello".isalpha()
is_digit = "12345".isdigit()
is_alnum = "Hello123".isalnum()
is_sapce = "   ".isspace()
print("Is 'Hello' alphabetic?", is_alpha)
print("Is '12345' numeric?", is_digit)
print("Is 'Hello123' alphanumeric?", is_alnum)
print("is '   'all spaces?", is_sapce)
