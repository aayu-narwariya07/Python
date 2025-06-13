# Task1:
class Animal:
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
def make_animal_speak(animal):
    print(animal.speak())

# Task3:
# Example usage
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    make_animal_speak(dog)
    make_animal_speak(cat)
