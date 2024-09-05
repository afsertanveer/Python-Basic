class Mammal:
    def walk(self):
        print("Walk")

class Other(Mammal):
    pass


class Dog(Mammal):

    def is_pettable(self):
        print("Yes")



class Cat(Mammal) :
    pass
    def sound(self):
        print("Meow")



other1 = Other()
other1.walk()
dog1 = Dog()
dog1.walk()
dog1.is_pettable()