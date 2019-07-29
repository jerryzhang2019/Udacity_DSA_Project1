
# coding: utf-8

# In[10]:


import csv
with open('texts.csv','r') as f:
    reader= csv.reader(f)
    texts=list(reader)

with open('calls.csv','r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
print("First record of texts, {} texts {} at time {}".format(*texts[0]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*calls[-1]))

