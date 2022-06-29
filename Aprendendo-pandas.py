import numpy as np
import pandas as pd

# my_labels = ['x', 'y', 'z']
# demo_list = [1, 2, 3]
# demo_array = np.array([1, 2, 3])
# demo_dict = {'x':1, 'y':2, 'z':3}

# pd.Series(data = demo_array, index = my_labels)

# demo_series = pd.Series([1,45,33,451,50])
# #demo_list = demo_series.to_list()

# print("Data type before converting = ",type(demo_series))
# print("Data type after converting = ",type(demo_list))

# demo_list = demo_series.sort_values(ascending=False)
# print(demo_list)

##### Dataframes #####

# one dimensional list
demo_list = [1, 2, 3]
#print(pd.DataFrame(demo_list))

# two dimensional list

demo_list2 = [['roy', 1], ['jason', 2],['Paulo', 3]]
demo_dataframe = pd.DataFrame(demo_list2, columns=['Name', 'Roll Number'])
(demo_dataframe)

# using dicts

demo_dict = {"Name":["roy", "jason", "Paulo"], "Roll number":[1,2,3]}
demo_dataframe2 = pd.DataFrame(demo_dict)
(demo_dataframe2)

# adding new column
demo_dataframe2["Marks"] = [90,50,80]
(demo_dataframe2)



# To append Pandas dataframes to another dataframe

dataframe1 = pd.DataFrame({'Name' : ['a', 'b', 'c', 'd'], 'Roll No' : [1, 2, 3, 4]})
dataframe2 = pd.DataFrame({'Name' : ['f', 'g', 'h', 'i'], 'Roll No' : [5, 6, 7, 8]})

# appending:
(dataframe2.append(dataframe1, ignore_index=True))

# export to CSV

demo_dataframe.to_csv("Studend.CVS")

print(dataframe1.describe())