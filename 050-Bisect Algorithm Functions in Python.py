'''
    #### Bisect Algorithm Functions in Python ###
    -The purpose of Bisect algorithm is to find a position in list where an element needs to be inserted to keep the list sorted.
    -Python in its definition provides the bisect algorithms using the module “bisect” which allows to keep the list in sorted order
    -after insertion of each element.
    -This is essential as this reduces overhead time required to sort the list again and again after insertion of each element.

    ## Important Bisection function: >>
        1. bisect(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order.
        2. bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order.
        3. bisect_right(list, num, beg, end) :- This function works similar to the “bisect()” and mentioned above.
        4. insort(list, num, beg, end) :- This function returns the sorted list after inserting number in appropriate position, if the element is already present in the list, the element is inserted at the rightmost possible position.
        5. insort_left(list, num, beg, end) :- This function returns the sorted list after inserting number in appropriate position, if the element is already present in the list, the element is inserted at the leftmost possible position.
        6. insort_right(list, num, beg, end) :- This function works similar to the “insort()” as mentioned above.


'''
import bisect
li = [1,3,4,4,4,6,7]

print("The rightmost index to insert so list remins sorted: ",bisect.bisect(li,1))
print("The leftmost index sorted :",bisect.bisect_left(li,4))
print("The rightmost index sorted :",bisect.bisect_right(li,4,0,4))
