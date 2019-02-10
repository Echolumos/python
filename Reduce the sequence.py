# In[2]:



# In[3]:


    # num_of_is = int(optimize.fsolve(lambda x: x*math.log(2)-math.log(n), x0=2)) 


# In[9]:


n = 4294967295654332198456789528
import time
start = time.time()
get_a_number(n)
end = time.time()
print end - start

