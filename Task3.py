
# coding: utf-8

# In[3]:


#Task3 (080) is the area code for fixed line telephones in Bangalore.Fixed line numbers include parentheses, so Bangalore numbers
#have the form (080)xxxxxxx.)
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
        total_count += 1
            
        if get_num_prefix(item[1]):
            code_set.add(get_num_prefix(item[1]))
            
            if get_num_prefix(item[1]) == '080':
                bangalore_count +=1
print("The numbers called by people in Bangalore have codes:\n{}".format("\n".join(sorted (code_set))))  

print("{}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      .format(round(bangalore_count/total_count*100,2)))

