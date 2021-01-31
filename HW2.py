#!/usr/bin/env python
# coding: utf-8

# 1. For all the items in your favorite color list, print out each item. (tips: create your color list first). [1 point]

# In[1]:


my_favorite_colors =["red","blue","white","teal","black"]
for i in my_favorite_colors:
    print(i)


# 2. Using For Loop. As long as n is less than 10, print out n. (Initialize n=0). [1 point]

# In[2]:


for i in range(10):
    print(i)


# 3. Using While Loop. As long as n is less than 10, print out n. (Initialize n=0). [1 point]

# In[3]:


n = 0
while n < 10:
    print(n)
    n += 1


# 4. Using while loop. While n is <= 10, print out n. Otherwise, print out “greater than 10”.  [1 point]

# In[4]:


n = 0 
while n <= 10:
    print(n)
    n += 1
else:
    print("greater than 10")


# 5. Add all the integers from 1 to 30, print out the sum. Using while loop.  [1 point]

# In[5]:


total = 0
num = 1
while num < 31:
    total = total + num
    num += 1
print(total)


# In[ ]:




