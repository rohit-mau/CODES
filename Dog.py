class Dogs:

    # Class Attribute
    species = 'mammal'

    # Initialize / Inatance AttributES
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Instantiate the Dog object
mikey = Dogs("Mikey", 6)

# call your instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))
