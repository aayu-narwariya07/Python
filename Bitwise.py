# Define two integer variables
a = 60 
b = 13
and_result = a & b
print(f"bitwise and: {a} & {b} = {and_result} (binary:{bin(and_result)}) ")
# bitwise or
or_result = a | b
print(f"bitwise or:{a} | {b} = {or_result} (binary:{bin(or_result)})")
# bitwise XOR
xor_result = a ^ b
print(f"bitwise xor: {a} ^ {b} = {xor_result} (binary: {bin(xor_result)})")
# bitwise NoT
not_result = ~a
print(f"bitwise not: ~{a} = {not_result} (binary: {bin(not_result)})")
# bitwise left shift
left_shift_result = a<<2
print(f"bitwise left shift: {a} << 2 = {left_shift_result} (binary:{bin(left_shift_result)})")
# bitwise right shift 
right_shift_result = a >> 2
print(f"bitwise right shift: {a} >>2 = {right_shift_result} (binary {bin(right_shift_result)})")
