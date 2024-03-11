import numpy as np

#sorting in numpy 
#np.sort()
#creating an array of random int variables - length of the array = 9
np1 = np.array([np.random.randint(1, 9) for i in range(9)])

print(np1)
#sorting the numbers
print(np.sort(np1))


#alphabetical sorting also works with np.sort()
np2 = np.array(["John", "Adam", "Nick", "Bob", "Craig"])
print(np2)
print(np.sort(np2))

#also works with booleans
np3 = np.array([True, False, False, True])
print(np3)
print(np.sort(np3))

#return a copy, not change the original
#print(np1) prints the original unsorted array

#2-d
np4 = np.array([[6,7,1,9], [8, 3, 5, 0]])
print(np4)
print(np.sort(np4))