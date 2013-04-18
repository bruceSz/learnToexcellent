import random
class PetShop:
    """ a pet shop"""
    def __init__(self,animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("this is a lovely",pet)
        print("it says",pet.speak())
        print("it eats",self.pet_factory.get_food())

class Dog:
    def speak(self):
        return "woof"
    def __str__(self):
        return "Dog"

class Cat:
    def speak(self):
        return "meow"
    def __str__(self):
        return "Cat"

class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "Dog food"

class CatFactory:
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "Cat food"

def get_factory():
    
    return random.choice([DogFactory,CatFactory])()
if __name__ == "__main__":
    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("="*20)
