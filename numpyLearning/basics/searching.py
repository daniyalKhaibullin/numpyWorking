import numpy as np
#search
np1 = np.array(np.arange(1, 11))
#concatenating an integer with np1 into np2
np2 = np.concatenate((np1, [3]))

x = np.where(np1==3)
y = np.where(np2==3)
print(np1)
print(np2)
print(x)
print(y)

#return even items 
print(np.where(np2%2==0))