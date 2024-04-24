# class Animal:
#     def __init__(self, animal):
#         print(animal, 'is an animal.')

# class Mammal(Animal):
#     def __init__(self, mammal_name):
#         print(mammal_name, 'is a warm-blooded animal.')
#         super().__init__(mammal_name)

# class NonWingedMammal(Mammal):
#     def __init__(self, non_winged_mammal):
#         print(non_winged_mammal, "can't fly.")
#         super().__init__(non_winged_mammal)

# class NonMarineMammal(Mammal):
#     def __init__(self, non_marine_mammal):
#         print(non_marine_mammal, "can't swim.")
#         super().__init__(non_marine_mammal)

# class Dog(NonMarineMammal, NonWingedMammal):
#     def __init__(self):
#         print('Dog has 4 legs.')
#         super().__init__('Dog')

# d = Dog()
# bat = NonMarineMammal('Bat')


 
class Animal:

  def __init__(self, Animal):

    print(Animal, 'is an animal.');
 
class Mammal(Animal):

  def __init__(self, mammalName):

    print(mammalName, 'is a warm-blooded animal.')

    super().__init__(mammalName)

class NonWingedMammal(Mammal):

  def __init__(self, NonWingedMammal):

    print(NonWingedMammal, "can't fly.")

    super().__init__(NonWingedMammal)
 
class NonMarineMammal(Mammal):

  def __init__(self, NonMarineMammal):

    print(NonMarineMammal, "can't swim.")

    super().__init__(NonMarineMammal)
 
class Dog(NonMarineMammal, NonWingedMammal):

  def __init__(self):

    print('Dog has 4 legs.');

    super().__init__('Dog')

d = Dog()

print('')

bat = NonMarineMammal('Bat')

print("\nThe  order in which  methods are inheritedin the presence  of MIH")
print(Dog.__mro__)
