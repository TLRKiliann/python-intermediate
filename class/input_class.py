#!/usr/bin/python3


class Animal(object):
    def __init__(self, name, age, race, eat, quantity, satisfact):
        self.name = name
        self.age = age
        self.race = race
        self.eat = eat
        self.quantity = quantity
        self.satisfact = satisfact

    @staticmethod
    def command(quantity):
        if quantity > 20:
            print("No problem")
        if quantity > 10:
            print("Middle pay ATTENTION!")
        else:
            print("Don't forget to command others !!!")

    def __str__(self):
        return f'My animal is {self.race}'


class Dog(Animal):
    def __init__(self, name, age, race, eat, quantity, satisfact, improveDog):
        super().__init__(name, age, race, eat, quantity, satisfact)
        self.improveDog = improveDog

    def declinaison(self):
        return f'Animal name\'s: {self.name} age: {self.age} race: {self.race}'

    def eaten(self):
        return f'Food: {self.eat} Quantity: {self.quantity} Satisfy: {self.satisfact}'

    def notification(self):
        print(f"Dog will be satisfy by: {self.improveDog}!\n")


class Cat(Animal):
    def __init__(self, name, age, race, eat, quantity, satisfact, improve):
        super().__init__(name, age, race, eat, quantity, satisfact)
        self.improve = improve

    def declinaison(self):
        return f'Animal name\'s: {self.name} age: {self.age} race: {self.race}'

    def eaten(self):
        return f'Food: {self.eat} Quantity: {self.quantity} Satisfy: {self.satisfact}'

    def notification(self):
        print(f"Cat will be satisfy by: {self.improve}!\n")

Animal.command(8)

animalDog = 0
animalCat = 0

while True:
    ask = input("Is it for a Dog or for a Cat ? (press d or c (n if none)): ")
    if ask == 'd':
        dogName = input("What's name of the dog ? : ")
        dogAge = int(input("How old is he ?: "))
        dogRace = input("What's his race ?: ")
        dogEaten = input("What's he eat ?: ")
        dogQuantity = int(input("Quantity: "))
        dogSatisfact = input("Is he satisfy ? (y/n): ")
        if dogSatisfact == "yes" or dogSatisfact == "y":
            dogStyle = "He is already happy"
        else:
            dogStyle = input("Choose something to be happy: ")
        print("All values are instanciated.\n")
        animalDog = 1
    elif ask == 'c':
        catName = input("What's name of the cat ?: ")
        catAge = int(input("How old is he ?: "))
        catRace = input("What's his race ?: ")
        catEaten = input("What's he eat ?: ")
        catQuantity = int(input("Quantity: "))
        catSatisfact = input("Is he satisfy ? (y/n): ")
        if catSatisfact == "yes" or catSatisfact == "y":
            catStyle = "He is already happy"
        else:
            catStyle = input("Choose something to be happy: ")
        print("All values are instanciated.\n")
        animalCat = 2
    else:
        print("\nDone !\n")
        break

try:
    print(f"values of animalDog: {animalDog} and animalCat: {animalCat}\n")
    if animalDog == 1:
        animalDog = Dog(dogName, dogAge, dogRace, dogEaten, dogQuantity, dogSatisfact, dogStyle)
        def callDog(animalDog):
            print(animalDog.declinaison())
            print(animalDog.eaten())
            animalDog.notification()
        callDog(animalDog)

    if animalCat == 2:
        animalCat = Cat(catName, catAge, catRace, catEaten, catQuantity, catSatisfact, catStyle)
        def callCat(animalCat):
            print(animalCat.declinaison())
            print(animalCat.eaten())
            animalCat.notification()
        callCat(animalCat)
    else:
        animalPet = [Dog(dogName, dogAge, dogRace, dogEaten, dogQuantity, dogSatisfact, dogStyle),
                     Cat(catName, catAge, catRace, catEaten, catQuantity, catSatisfact, catStyle)]

        def callAnimal(animalPet):
            for animal in animalPet:
                print(animal.declinaison())
                print(animal.eaten())
                animal.notification()

        callAnimal(animalPet)

except NameError:
    print("Command is finished !")
