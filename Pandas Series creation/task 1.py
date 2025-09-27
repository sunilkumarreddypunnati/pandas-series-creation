'''Task 1: Series from List

Create a Series from the list [5, 10, 15, 20, 25].

Print the Series.

Access the 2nd and 4th elements.

Find the sum of all values.'''

import pandas as pd
list= [5, 10, 15, 20, 25]
s=pd.Series(list)
print(s)
print("second element:",s[1])
print("fourth element:",s[3])

print("sum:",s.sum())
