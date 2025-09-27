'''Task 5: Series from Dictionary

Create a Series from dictionary:

fruits = {"Apple": 50, "Banana": 100, "Mango": 70, "Orange": 80}


Print the Series.

Access the quantity of Mango.

Add a new fruit "Grapes": 120 to the Series.'''

import pandas as pd
fruits = {"Apple": 50, "Banana": 100, "Mango": 70, "Orange": 80}
data=pd.Series(fruits)
print(data,'\n')
print("Access the quantity of Mango:",data['Mango'],'\n')
data["Grapes"]=120
print(data,'\n')