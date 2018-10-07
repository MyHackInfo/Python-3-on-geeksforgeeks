# Accessing items using for-in loop

cars = ["Aston", "Audi", "McLaren"]
for x in cars:
    print (x)


# Indexing using Range function
for i in range(len(cars)):
    print (cars[i])


# Enumerate is built-in python function that takes input as iterator
for q, x in enumerate(cars):
    print (x)
for x in enumerate(cars):
    print (x[0], x[1])

# Enumerate takes parameter start which is default set to zero.
# We can change this parameter to any value we like. In the below code we have used start as 1
for x in enumerate(cars, start=5):
    print (x[0], x[1])


# Python program to demonstrate working of zip

# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit",
               "Dolby sound kit"]

# Combining lists and printing
for c, a in zip(cars, accessories):
    print ("Car: %s, Accessory required: %s"\
          %(c, a))
