class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, special_skill):
        super().__init__(name, age, coat_color)
        self.special_skill = special_skill

    def special_ability(self):
        print(f"{self.name} has a special skill: {self.special_skill}.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def display_weight(self):
        print(f"{self.name} weighs {self.weight} kg.")


# Creating objects 
dog1 = Dog("Tommy", 3, "Brown")
dog1.description()
dog1.get_info()

jack_russell = JackRussellTerrier("Buddy", 2, "White", "Agility")
jack_russell.description()
jack_russell.get_info()
jack_russell.special_ability()

bulldog = Bulldog("Simba", 4, "black", 25)
bulldog.description()
bulldog.get_info()
bulldog.display_weight()
