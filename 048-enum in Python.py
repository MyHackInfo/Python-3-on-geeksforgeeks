'''
    #### Enum in Python ####
    -Enumerations in Python are implemented by using the module named “enum“.
    -Enumerations are created using classes. Enums have names and values associated with them.

    ## Properties of enum:
        1. Enums can be displayed as string or repr.
        2. Enum can be checked for their types using type().
        3. “name” keyword is used to display the name of the enum member.
        4. Enumerations are iterable. They can be iterated using loops.
        5. Enumerations support hashing. Enums can be used in dictionaries or sets.


'''
import enum
class Animal(enum.Enum):
    dog=1
    cat=2
    lion=3

print("The String representation of enum :",Animal.dog)
print("The type of enum:",type(Animal.dog))
print("The repr representation of enum:",repr(Animal.dog))
print("The name of enum:",Animal.dog.name)


# Print all enum using loop
for a in (Animal):
    print("\n",a)
