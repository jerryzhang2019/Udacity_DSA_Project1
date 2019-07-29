
# coding: utf-8

# In[4]:


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    texts_incoming_num, texts_answering_num, texts_timestamp = zip(*texts)
    calls_incoming_num, calls_answering_num, calls_timestamp, calls_duration = zip(*calls)
    
    texts_incoming_num_set = set(texts_incoming_num)
    texts_answering_num_set = set(texts_answering_num)
    
    calls_incoming_num_set = set(calls_incoming_num)
    calls_answering_num_set = set(calls_answering_num)
    
    telemarketers_num = calls_incoming_num_set.difference(calls_answering_num_set, texts_incoming_num_set, texts_answering_num_set)
    
print("These number could be telemarketer:\n{}".format("\n".join(sorted(telemarketers_num))))

