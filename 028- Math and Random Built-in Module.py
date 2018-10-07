'''
    # Numeric Functions(ceil(),floor(),factorial(),copysign(),gcd())
    # Power Functions(pow())
    # Trigonometric Functions(sin(),cos(),tan())
    # Special Functions and Constants( pi,e )


'''

import math
print(dir(math))
print('math nan method',math.nan)
print('math sqrt method=',math.sqrt(25))
print('math pow method=',math.pow(2,8))
print('math pi method=',math.pi)
print('math degrees method',math.degrees(20))
print('math radians method',math.radians(60))
print('math sin method',math.sin(2))
print('math cos method',math.cos(0.5))
print('math tan method',math.tan(0.23))
print('math factorial method',math.factorial(4))
print('math copysign method',math.copysign(-5.5,+10))
print('math gcd method',math.gcd(3,15))

import random
print("\n")
print()
print('random randint',random.randint(0,5))
print('random random',random.random())
print('random random between 0 to 50',random.random()* 50)
print('random choice', random.choice([1,2,True,False,"yes","no"]))
