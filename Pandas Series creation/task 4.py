'''Task 4: Series from NumPy Array with Custom Index

Create a NumPy array with values [100, 200, 300, 400].

Convert it into a Series with index labels 
['A', 'B', 'C', 'D'].

Print the Series.

Access the value of index 'C'.'''

import pandas as pd
import numpy as np
arr=np.array([100,200,300,400])
data=pd.Series(arr,index=['A', 'B', 'C', 'D'])
print(data)
print("Access the value of index 'C':\n",data['C'])