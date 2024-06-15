#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing os i.e operating system and shutil : it is basically used for moving the files

import os, shutil


# In[4]:


#creating a variable for files list and importing the path

path = r"C:/Users/CW/OneDrive/Desktop/MASAI/POWER BI/assignments/assign 4  n 5 files/"


# In[18]:


#printing the list of all the files

file_name = os.listdir(path)
file_name


# In[20]:


#creating a folder name for each files

folder_name = ["csv files", "Excel files", "txt files", "Images"]

for loop in range(4): 
    if not os.path.exists(path + folder_name[loop]): #checking if the foler_name exists or not 
        print(path + folder_name[loop])
        
        os.makedirs(path + folder_name[loop]) #if the folder_name does not exists then making the folder


# In[21]:


#for checking the files and moving them to its specific folder

for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "Excel files/" + file):
        shutil.move(path+file, path + "Excel files/" + file)

    elif ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path+file, path + "csv files/" + file)
        
    elif ".txt" in file and not os.path.exists(path + "txt files/" + file):
        shutil.move(path+file, path + "txt files/" + file)
        
    elif ".png" in file and not os.path.exists(path + "Images" + file):
        shutil.move(path+file, path + "Images/" + file)
        
            
    


# In[ ]:





# In[ ]:




