class Animal:
    def __init__(self, species = "animal", language = "sounds"):
        self.species = species
        self.language = language

    def setSpecies(self, species):
        self.species = species
    
    def setLanguage(self, language):
        self.language = language
    
    def speak(self):
        print(f"I am a {self.species} and I {self.language}")

cat = Animal("cat", "meow")
cat.speak()

animal = Animal()
animal.speak()

dog = Animal(language = "bark")
dog.speak()
