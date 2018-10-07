'''
    ### Heap Queue in python ###
    -Heap data structure is mainly used to represent a priority queue.
    -In Python, it is available using “heapq” module. The property of this
    -data structure in python is that each time the smallest of heap element is popped(min heap).
    -Whenever elements are pushed or popped, heap structure in maintained.
    -The heap[0] element also returns the smallest element each time.

    ## Operations on heap :>>
        1. heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.
        2. heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. The order is adjusted, so as heap structure is maintained.
        3. heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained.
        4. heappushpop(heap, ele) :- This function combines the functioning of both push and pop operations in one statement, increasing efficiency. Heap order is maintained after this operation.
        5. heapreplace(heap, ele) :- This function also inserts and pops element in one statement, but it is different from above function. In this, element is first popped, then element is pushed.i.e, the value larger than the pushed value can be returned.
        6. nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements from the iterable specified and satisfying the key if mentioned.
        7. nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest elements from the iterable specified and satisfying the key if mentioned.


'''
import heapq

# list
li=[4,6,2,7,4,8]

# convert list to  heap
heapq.heapify(li)
print("The created heap is:",li) # list(li)

heapq.heappush(li,9)
print("The modified heap after push :",li)

print("The popped and smallest elements:",heapq.heappop(li))
print("After pop :",li)

heapq.heappushpop(li,4)
print("The popped item using heappushpop():",li )

heapq.heapreplace(li,3)
print("The popped item using heapreplace():",li)

print("The 3 largest number is :",heapq.nlargest(3,li))
print("The 3 smallest number is :",heapq.nsmallest(3,li))
