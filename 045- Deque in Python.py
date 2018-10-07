'''
    ## Deque in Python ##
    -Deque can be implemented in python using the module “collections“.
    -Deque is preferred over list in the cases where we need quicker
    -append and pop operations from both the ends of container,
    -as deque provides an O(1) time complexity for append and pop
    -operations as compared to list which provides O(n) time complexity.

    # operations on deque:>>
        1. append() :- This function is used to insert the value in its argument to the right end of deque.
        2. appendleft() :- This function is used to insert the value in its argument to the left end of deque.
        3. pop() :- This function is used to delete an argument from the right end of deque.
        4. popleft() :- This function is used to delete an argument from the left end of deque.
        5. index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
        6. insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
        7. remove() :- This function removes the first occurrence of value mentioned in arguments.
        8. count() :- This function counts the number of occurrences of value mentioned in arguments.
        9. extend(iterable) :- This function is used to add multiple values at the right end of deque. The argument passed is an iterable.
        10. extendleft(iterable) :- This function is used to add multiple values at the left end of deque. The argument passed is an iterable. Order is reversed as a result of left appends.
        11. reverse() :- This function is used to reverse order of deque elements.
        12. rotate() :- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to left. Else rotation is to right.


'''
import collections

de=collections.deque([1,2,3])
# Append()
de.append(4)
print("append :",de)

de.appendleft(6)
print("appendleft :",de)

de.pop()
print("pop :",de)

de.popleft()
print("popleft :",de)

de=collections.deque([1,2,3,3,4,5,6,7])
print("index :",de.index(4,1,6))

de.insert(3,8)
print(" before remove insert :",de)

print("count :" ,de.count(3))

de.remove(8)
print(" after remove :",de)

de.extend([9,8,7])
print("extend :",de)

de.extendleft([6,7,8])
print("extendleft :",de)

de.rotate(-3)
print("after rotate :",de)

de.reverse()
print("after reverse :",de)
