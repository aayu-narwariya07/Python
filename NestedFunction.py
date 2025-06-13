# Enclosing Scope (Nested Function)
def outer_function():
    x =  10 
    def inner_function():
        print("Enclosing variable x from inner function: ", x)
    inner_function()
outer_function()
