#################################
# To handle simple runtime error#
#################################

a=[1,2,3]
#print(a[2])
#print(a[4])
try:
    print("a first value is = %d" %(a[1]))

    print("a fourth value is = %d" %(a[4]))

except IndexError:
    print("An error occurred")


##################################
# TO Handle Multiple Errors ######
##################################

try:
    a=3
    if a<4:
        b=a/(a-3)
    print("value of b = ",b)

except(ZeroDivisionError,NameError):
    print("both are error")


###############################
# Raising Exception ##########
############################
try:
    raise NameError("Hey all of you !")
except NameError:
    print("Sorry!")
    raise
