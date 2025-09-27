'''Task 2: Series from List with Custom Index

Create a Series from the list [90, 85, 78, 92]
 with custom indexes ['Math', 'Science', 'English', 'History'].

Print the Series.

Access the marks of Science.

Update the marks of English to 80.'''

import pandas as pd
marks=[90, 85, 78, 92]
subjects= ['Math', 'Science', 'English', 'History']
data=pd.Series(marks,index=subjects)
print(data)
print("Access the marks of Science:")
print(data['Science'])
print("Update the marks of English to 80:")
data['English']=80
print(data)