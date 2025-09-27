'''Task 3: Series from NumPy Array

Import NumPy and create an array of numbers 
from 10 to 50 with a step of 10.

arr = np.arange(10, 60, 10)


Convert it into a Series.

Print the Series.

Multiply all values in the Series by 2.'''

import pandas as pd
import numpy as np
 
arr=np.arange(10,60,10)
s=pd.Series(arr)
print(s,'\n')
print("Multiply all values in the Series by 2:\n",s.mul(2))