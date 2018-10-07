'''
    #### Decimal Functions in Python ###
    -Python in its definition provides certain methods to perform faster decimal floating point arithmetic using the module “decimal”.

    ## Important operations on Decimal :>>
        1. sqrt() :- This function computes the square root of the decimal number.
        2. exp() :- This function returns the e^x (exponent) of the decimal number.
        3. ln() :- This function is used to compute natural logarithm of the decimal number.
        4. log10() :- This function is used to compute log(base 10) of a decimal number.
        5. as_tuple() :- Returns the decimal number as tuple containing 3 arguments, sign(0 for +, 1 for -), digits and exponent value.
        6. fma(a,b) :- This “fma” stands for fused multiply and add. It computes (num*a)+b from the numbers in argument. No rounding of (num*a) takes place in this function.
        7. compare() :- This function is used to compare decimal numbers. Returns 1 if 1st Decimal argument is greater than 2nd, -1 if 1st Decimal argument is smaller than 2nd and 0 if both are equal.
        8. compare_total_mag() :- Compares the total magnitute of decimal numbers. Returns 1 if 1st Decimal argument is greater than 2nd(ignoring sign), -1 if 1st Decimal argument is smaller than 2nd(ignoring sign) and 0 if both are equal(ignoring sign).
        9. copy_abs() :- This function prints the absolute value of decimal argument.
        10. copy_negate() :- This function prints the negation of decimal argument.
        11. copy_sign() :- This function prints the first argument by copying the sign from 2nd argument.
        12. max() :- This function computes the maximum of two decimal numbers.
        13. min() :- This function computes the minimum of two decimal numbers
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        14. logical_and() :- This function computes digit-wise logical “and” operation of the number. Digits can only have the values 0 or 1.
        15. logical_or() :- This function computes digit-wise logical “or” operation of the number. Digits can only have the values 0 or 1.
        16. logical_xor() :- This function computes digit-wise logical “xor” operation of the number. Digits can only have the values 0 or 1.
        17. logical_invert() :- This function computes digit-wise logical “invert” operation of the number. Digits can only have the values 0 or 1.
        18. next_plus() :- This function returns the smallest number that can be represented, larger than the given number.
        19. next_plus() :- This function returns the largest number that can be represented, smaller than the given number.
        20. next_toward() :- This function returns the number nearest to the 1st argument in the direction of the second argument. In case Both the numbers are equal, returns the 2nd number with the sign of first number.
        21. normalize() :- This function prints the number after erasing all the rightmost trailing zeroes in the number.
        22. quantize() :- This function returns the 1st argument with the number of digits in decimal part(exponent) shortened by the number of digits in decimal part(exponent) of 2nd argument.
        23. same_quantum() :- This function returns 0 if both the numbers have different exponent and 1 if both numbers have same exponent.
        24. rotate() :- This function rotates the first argument by the amount mentioned in the second argument. If the sign of second argument is positive, rotation is towards left, else the rotation is towards right. The sign of first argument is unchanged.
        25. shift() :- This function shifts the first argument by the amount mentioned in the second argument. If the sign of second argument is positive, shifting is towards left, else the shifting is towards right.
        26. remainder_near() :- Returns the value “1st – (n*2nd)” where n is the integer value nearest to the result of 1st/2nd. If 2 integers have exactly similar proximity, even one is choosen.
        27. scaleb() :- This function shifts the exponent of 1st number by the value of second argument.



'''
import decimal

print("The square root of decimal num:",decimal.Decimal(4.5).sqrt())
print("The exponent of decimal num :",decimal.Decimal(4.5).exp())
print("The natural logarithm of decimal num:",decimal.Decimal(4.5).ln())
print("The log(base 10) of decimal num:",decimal.Decimal(4.5).log10())
print("The tuple form of decimal num:",decimal.Decimal(-4.5).as_tuple())
print("The fused multiply and addition of decimal num:",decimal.Decimal(5).fma(2,3))
print("The result of comparsion using comare():",decimal.Decimal(9.53).compare(decimal.Decimal(-9.56)))
print("The result of comparsion using compare_total_mag()",decimal.Decimal(9.53).compare_total_mag(decimal.Decimal(-9.56)))
print("The absolute value using copy_abs()",decimal.Decimal(-9.56).copy_abs())
print("The negated value using copy_negate()",decimal.Decimal(-9.56).copy_negate())
print("The sign effected value using copy_sign():",decimal.Decimal(9.53).copy_sign(decimal.Decimal(-9.56)))
print("The minimum of two num:",decimal.Decimal(9.53).min(decimal.Decimal(7.43)))
print("The maximum of two num:",decimal.Decimal(9.53).max(decimal.Decimal(7.43)))


########################## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
a = decimal.Decimal(1000)
b = decimal.Decimal(1110)
print("The logical_and() of two num:",a.logical_and(b))
print("The logical_or:",a.logical_or(b))
print("The logical_xor:",a.logical_xor(b))
print("The logical_invert:",a.logical_invert())

#################
a = decimal.Decimal(101.34)
print("The original num :",a)
print("The smal number larger than current num:",a.next_plus())
print("The largest number smallest than current num:",a.next_minus())
#####################
a = decimal.Decimal(101.34)
b = decimal.Decimal(-101.34)
c = decimal.Decimal(-58.68)
d = decimal.Decimal(14.010000000)
print("The number closest to 1st number direction of second num:",a.next_toward(c))
print("The second number with sign of first number :",b.next_toward(a))
print("Number after erasing rightmost trailing zeroes:",d.normalize())
####################################
a = decimal.Decimal(20.76548)
b = decimal.Decimal(12.25)
c = decimal.Decimal(6.25)
#print("The quantized first num:",a.quantized(b))
print("The same_quantum () :",b.same_quantum(c))

######################
a = decimal.Decimal(2343509394029424234334563465)
print("The rotated value:",a.rotate(-2))
print("The shifted value:",a.shift(2))

print("The computed value using remainder_near():",b.remainder_near(c))
print("The value after shifting exponent",a.scaleb(2))
