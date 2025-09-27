'''Task 6: Series Operations

Create two Series

Perform:

Addition of s1 + s2

Subtraction of s1 - s2

Multiplication of s1 * s2'''

import pandas as pd
s1 = pd.Series([10,20,30],index=['a','b','c'])
s2 = pd.Series([5,15,25],index=['a','b','c'])
print("Addition of s1 + s2:\n",s1+s2)
print("Subtraction of s1 - s2:\n",s1-s2)
print("Multiplication of s1 * s2:\n",s1*s2) 