#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[34]:


arr = np.array(range(1, 13)).reshape(3, 4)


# In[35]:


arr


# In[36]:


x = np.array(range(1, 7), int)


# In[37]:


y = np.array(range(5, 11), int)


# In[12]:


plt.figure()
plt.title("Question 3")
plt.plot(x, y)
plt.show()


# In[32]:


plt.figure()
plt.title("Question 4")
plt.plot(x, y+2)
plt.plot(x, y)
plt.plot(x, y-2)
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()


# In[33]:


import random
plt.figure()
plt.subplot(1,2,1)
rand_x1 = random.sample(range(1, 101), 10)
rand_y1 = random.sample(range(3, 501), 10)
plt.title("random curve 1")
plt.plot(sorted(rand_x1), sorted(rand_y1))

plt.subplot(1,2,2)
rand_x2 = random.sample(range(1, 101), 10)
rand_y2 = random.sample(range(3, 501), 10)
plt.title("random curve 2")
plt.plot(sorted(rand_x2), sorted(rand_y2))
plt.show()


# In[ ]:




