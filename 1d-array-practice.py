
# 1. create and traverse array O(n)
from array import *
my_array = array('i', [1, 2, 3, 4, 5])

for i in my_array:
    print(i)

# 2. Access individual elements through the indexes O(n)

print(my_array[1])

# 3. append element to the end of the array O(1)

my_array.append(6)
print(my_array)

# 4. insert value into array O(n)

my_array.insert(3, 30)
print(my_array)

# 5. extend array

my_array.extend([11, 12, 13, 14])

print(my_array)
