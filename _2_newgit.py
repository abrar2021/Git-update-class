class Human:
    def __init__(self,name,country):
        self.name = name
        self.country = country

    def introduce(self):
        print(f"Hello {self.name} and I am {self.country}.")

nasrin =Human("Nasrin","BD")
nasrin.introduce()

akter = Human("Akter","BD")
akter.introduce()