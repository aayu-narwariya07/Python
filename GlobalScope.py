#  Global Scope
x = 10
def global_scope_example():
    print("Global variable x: ", x)
global_scope_example()
print("Global variable x outside function:", x)

# modify global variables
x = 10
def modify_global():
    global x
    x = 20
modify_global()
print("Global variable x after modification", x)
