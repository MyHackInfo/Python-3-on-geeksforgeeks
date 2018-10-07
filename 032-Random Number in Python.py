'''
    #### Random Number in Python ####
    -Python defines a set of functions that are used to generate or manipulate random numbers.
    -This particular type of functions are used in a lot of games,
    -lotteries or any application requiring random number generation.

    ## Randon Number Operations :
        1. choice() :- This function is used to generate 1 random number from a container.
        2. randrange(beg, end, step) :- This function is also used to generate random number but within a range
        3. random() :- This number is used to generate a float random number less than 1 and greater or equal to 0.
        4. seed() :- This function maps a particular random number with the seed argument mentioned.
        5. shuffle() :- This function is used to shuffle the entire list to randomly arrange them.
        6. uniform(a, b) :- This function is used to generate a floating point random number between the numbers mentioned in its arguments.
                            It takes two arguments, lower limit(included in generation) and upper limit(not included in generation).


'''
import random

print('random choice method',random.choice([1,3,5,7,9]))
print('random randrange method',random.randrange(10,50,5))
print('random random method',random.random())
print('random seed method')
random.seed(7)
print('random random method',random.random())

li=[1,3,5,7,9]
print('before shuffle',*li)
random.shuffle(li)
print('after shuffle',*li)

print('random uniform method',random.uniform(5,100))
