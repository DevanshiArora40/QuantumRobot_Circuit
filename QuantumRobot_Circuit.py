#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qiskit


# In[2]:


from qiskit import IBMQ


# In[4]:


from qiskit import*


# In[5]:


qr= QuantumRegister(1)


# In[6]:


cr=ClassicalRegister(1)


# In[7]:


qc=QuantumCircuit(qr,cr)


# In[8]:


qc.draw()


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


qc.draw('mpl')


# In[12]:


qc.measure(qr,c)


# In[29]:


qc.draw(output='mpl')


# In[18]:


job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=1)


# In[19]:


result = job.result().get_counts(qc)


# In[26]:


qc.draw('mpl'%result)


# In[27]:


answer(result)


# In[30]:


simulator =Aer.get_backend('qasm_simulator')


# In[32]:


result = execute(qc, backend = simulator).result()


# In[33]:


from qiskit.tools.visualization import plot_histogram


# In[35]:


plot_histogram(result.get_counts(qc))


# In[36]:


IBMQ.load_account()


# In[37]:


provider = IBMQ.get_provider('ibm-q')


# In[38]:


qcomp = provider.get_backend('ibmq_16_melbourne')


# In[39]:


job=execute(qc,backend=qcomp)


# In[40]:


from qiskit.tools.monitor import job_monitor


# In[41]:


job_monitor(job)


# In[42]:


result=job.result()


# In[43]:


plot_histogram(result.get_counts(qc))


# In[ ]:




