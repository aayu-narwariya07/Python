# Task1:
# Define two classes with the same method fly() and define function
class Bird:
    def fly(self):
        return "Flying high"
    
class Airplane:
    def fly(self):
        return "Flying through the skies"
    
def let_it_fly(entity):
    print(entity.fly())

# Task2:
# Create object and demonstrate Duck Typing Example usage
if __name__ == "__main__":
    bird = Bird()
    airplane = Airplane()

    let_it_fly(bird)
    let_it_fly(airplane)
