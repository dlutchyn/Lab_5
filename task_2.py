class Animal:
    def __init__(self, phylum, clas):
        self.phylum = phylum
        self.clas = clas
    
    def __str__(self):
        return f"<animal class is {self.clas}>"


class Cat(Animal):
    def __init__(self, phylum, clas, genus):
        super().__init__(phylum, clas)
        self.genus = genus
    
    def sound(self):
        return "Meow"

    def __str__(self):
        return f"<This {self.genus} animal class is {self.clas}>"


class Furniture:
    def __init__(self, style, assign):
        self.style = style
        self.assign = assign

    def __str__(self):
        return f"<furniture style is {self.style}>"


class Chair(Furniture):
    def __init__(self, style, assign, tipe):
        super().__init__(style, assign)
        self.tipe = tipe
    
    def get_assign(self):
        return self.assign
    
    def __str__(self):
        return f"<This {self.tipe} furniture style is {self.style}>"


if __name__ == "__main__":
    
    animal1 = Animal("chordata", "mammalia")

    assert(animal1.phylum == "chordata")

    assert(animal1.clas == "mammalia")

    assert(str(animal1) == "<animal class is mammalia>")

    animal2 = Animal("chordata", "birds")

    assert(not (animal1 == animal2))

    cat1 = Cat("chordata", "mammalia", "felis")

    assert(cat1.sound() == "Meow")

    assert(cat1.genus == "felis")

    assert(isinstance(cat1, Animal))

    assert(str(cat1) == "<This felis animal class is mammalia>")


    furniture1 = Furniture("empire", "bedroom")

    furniture2 = Furniture("modern", "bathroom")

    assert(not (furniture1 == furniture2))

    assert(furniture1.style == "empire")

    assert(furniture1.assign == "bedroom")

    assert(str(furniture1) == "<furniture style is empire>")

    chair1 = Chair("empire", "bedroom", "armchair")

    assert(chair1.tipe == "armchair")

    assert(isinstance(chair1, Furniture))

    assert(str(chair1) == "<This armchair furniture style is empire>")

    assert(chair1.get_assign() == "bedroom")