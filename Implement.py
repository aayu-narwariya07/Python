temp = input("input the temperature you like to convert? (e.g.,45F, 102C etc.) :")
degree = int(temp[:-1])
i_convention = temp[-1]
if i_convention.upper() == "C" and "c":
    result = int(round(9 * degree / 5 + 32)) 
    o_convention = "Fahrenheit"
elif i_convention.upper() == "F" and "f":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
else:
    print("Input proper convention. ")
print("The temperature in",o_convention, "is", result, "degree.")
