
# coding: utf-8

# In[1]:


#Task1
import csv
with open('texts.csv','r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open('calls.csv','r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
a,b,c = zip(*texts)
e,f,g,h = zip(*calls)
telephone_num = set(a).union(set(b), set(e), set(f))
print("There are {} different telephone numbers in the records".format(len(telephone_num)))

