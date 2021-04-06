#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Queue:
    def __init__(self):
        self.queue = []
        
    def print(self):
        print(self.queue)
        
    def insert(self, num):
        self.queue.append(num)
    
    def remove(self):
        if len(self.queue) == 0:
            print("queue is empty now")
        else:
            return self.queue.pop(0)


# In[18]:


q = Queue()
q.insert(1)
q.insert(2)
q.print()
#[1,2]


# In[19]:


q.insert(3)
q.remove()
q.print()
#[2,3]


# In[20]:


q.remove()
q.remove()
q.remove()
# queue is empty now


# In[ ]:




