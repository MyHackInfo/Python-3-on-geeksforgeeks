'''
1-Using enumerate():
    enumerate() is used to loop through the containers printing the
    index number along with the value present in that particular index.

2-Using zip():
    zip() is used to combine 2 similar containers(list-list or dict-dict)
    printing the values sequentially. The loop exists only till the smaller container ends.


3-Using items():
    items() performs the similar task on dictionary as iteritems()
    but have certain disadvantages when compared with iteritems().

4-Using sorted():
    sorted() is used to print the container is sorted order. It doesn’t sort the container,
    but just prints the container in sorted order for 1 instance.
    Use of set() can be combined to remove duplicate occurrences.

5-Using reversed():
    reversed() is used to print the values of container in the descending order as declared.

'''
# Here start all Examaple  

'''
# 1-Using enumerate():
for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)
'''

'''
# 2-Using zip():
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']
# using zip() to combine two containers
# and print values
for question, answer in zip(questions, answers):
    print('What is your {0}?  I am {1}.'.format(question, answer))

'''

'''
# 3-Using items():
d = { "geeks" : "for", "only" : "geeks" }
for i,j in d.items():
    print (i,j)

'''

'''
# 4-Using sorted():
lis = [ 1 , 3, 5, 6, 2, 1, 3 ]
print ("The list in sorted order is : ")
for i in sorted(lis) :
    print (i,end=" ")

print("\n")
print ("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)) :
    print (i,end=" ")

'''

'''
#5-Using reversed():
lis = [ 1 , 3, 5, 6, 2, 1, 3 ]
# using revered() to print the list in reversed order
print ("The list in reversed order is : ")
for i in reversed(lis) :
    print (i,end=" ")

'''
