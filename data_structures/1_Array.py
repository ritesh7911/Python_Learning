import array as arr


l = arr.array('i',[1,2,3,4,5])

# Import the array module
# from array import array

# Create an array of signed integers
signed_arr = arr.array('i', [-1, 2, -3, 4, -5])

# Create an array of unsigned integers
unsigned_arr = arr.array('I', [1, 2, 3, 4, 5])


##1.Insertion and removing of an element from end has O(1)

print(l.append(22))
print(l)
print(l.pop())


##2. Inserting and removing of an element at beginning and in middle has 0(n)

l.remove(1)
l.insert(2,4345)

##3 Accessing elements of an array has time complexity of O(1)

print(l[2])

##4 Searching element in an array has TC of O(n)
print(l)

print(l.index(5))
print('yes')

##5.Complexities for updating elements in the Arrays has TC of O(n)

#When you update an element at a particular index, especially if the array needs to shift elements to accommodate the change, it can require multiple operations that depend on the size of the array.

l[4]=25

print(l)

##6. TC for counting an element is O(n)

print(l.count(4))












# Print the arrays
# print("Signed Array:", signed_arr)
# print("Unsigned Array:", unsigned_arr)



