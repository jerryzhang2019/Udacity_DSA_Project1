
# coding: utf-8

# In[37]:


#Task0 任务0
""""
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

import time
start_time = time.time()

import csv
with open('texts.csv','r') as f:
    reader= csv.reader(f)
    texts=list(reader)

with open('calls.csv','r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
print("First record of texts, {} texts {} at time {}".format(*texts[0])) #操作=1
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*calls[-1])) #操作=1

end_time = time.time()
print("times:%d " % (end_time- start_time))
print("finished")
get_ipython().run_line_magic('time', '')
#O(1) 时间复杂度为O(1)


# In[38]:


#Task1 任务1
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

import time
start_time = time.time()

import csv
with open('texts.csv','r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open('calls.csv','r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
a,b,c = zip(*texts) #操作=n
e,f,g,h = zip(*calls) #操作=n
telephone_num = set(a).union(set(b), set(e), set(f)) #操作=1
print("There are {} different telephone numbers in the records".format(len(telephone_num))) #操作=1

end_time = time.time()
print("times:%d " % (end_time - start_time))
print("finished")
get_ipython().run_line_magic('time', '')
#O(n)时间复杂度为O(n)


# In[39]:


#Task2 任务2
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
import time
start_time = time.time()

import csv
with open('texts.csv','r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open('calls.csv','r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
phone_time_dict = {}
for item in calls:
    phone_time_dict[item[0]] = phone_time_dict.setdefault(item[0],0) + int(item[-1]) #操作=n
    phone_time_dict[item[1]] = phone_time_dict.setdefault(item[1],0) + int(item[-1]) #操作=n
    
result = (max(phone_time_dict.items(), key=lambda x: x[1]))
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*result)) #操作=1

end_time = time.time()
print("times: %d " % (end_time-start_time))
print("finished")
get_ipython().run_line_magic('time', '')
#O(n) 时间复杂度为O(n)+O(n)=2*O(n)约等于O(n)


# In[40]:


#任务3
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#Task3 (080) is the area code for fixed line telephones in Bangalore.Fixed line numbers include parentheses, so Bangalore numbers
#have the form (080)xxxxxxx.)
import time
start_time = time.time()

import csv
with open('texts.csv','r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open('calls.csv','r') as f:
    reader = csv.reader(f)
    calls = list(reader)
#Part A: Find all of the area codes and mobile prefixes called by people in Bangalore.   
def get_num_prefix(phone_number):
    if phone_number[0] == '(':
        num_prefix = phone_number[1:phone_number.index(')')]
    elif phone_number[0] in ('7','8','9'):
        num_prefix = phone_number[0:4]
    elif phone_number[0:3] == '140':
        num_prefix = phone_number[0:4]
    else:
        num_prefix = None
    return num_prefix

code_set = set() #?

#Part B: What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore? 
bangalore_count = 0
total_count = 0
for item in calls:
    if item[0][0:5] == '(080)':
        total_count += 1 #操作=1
        
        if get_num_prefix(item[1]):
            code_set.add(get_num_prefix(item[1]))
            
            if get_num_prefix(item[1]) == '080':
                bangalore_count +=1 #操作=1
print("The numbers called by people in Bangalore have codes:\n{}".format("\n".join(sorted (code_set))))  #操作=1

print("{}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      .format(round(bangalore_count/total_count*100,2))) #操作=1

end_time = time.time()
print("times %d" % (end_time- start_time))
print("finished")
get_ipython().run_line_magic('time', '')
#O(n^2) 时间复杂度为O (n^2)


# In[41]:


#任务4
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

import time
stat_time = time.time()

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
    
print("These number could be telemarketer:\n{}".format("\n".join(sorted(telemarketers_num)))) #操作=1

end_time = time.time()
print("times %d " % (end_time- start_time))
print("finished")
get_ipython().run_line_magic('time', '')
#O(1)

