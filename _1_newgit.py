class Animal:
    def sound(self):
      pass

class Dog(Animal):
    def sound(self):
        print("Geu Geu")

class Cat(Animal):
    def sound(self):
        print("Mew Mew")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()