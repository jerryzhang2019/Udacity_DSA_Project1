
# coding: utf-8

# In[3]:


#Task2
import csv
with open('texts.csv','r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open('calls.csv','r') as f:
    reader = csv.reader(f)
    calls = list(reader)
phone_time_dict = {}
for item in calls:
    phone_time_dict[item[0]] = phone_time_dict.setdefault(item[0],0) + int(item[-1])
    phone_time_dict[item[1]] = phone_time_dict.setdefault(item[1],0) + int(item[-1])
    
    
result = (max(phone_time_dict.items(), key=lambda x: x[1]))
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*result))

