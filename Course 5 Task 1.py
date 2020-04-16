#!/usr/bin/env python
# coding: utf-8

# In[174]:


import pandas


# In[175]:


import csv


# In[176]:


with open('C:/Users/Sully/Desktop/C5 T1/default of credit card clients short.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(', '.join(row))


# In[177]:


import math


# In[178]:


math.sqrt(197)


# In[179]:


math.pi


# In[180]:


import numpy as np
import scipy


# In[181]:


import scipy.stats


# In[182]:


from numpy import random


# In[183]:


# uniform random numbers in [0,1]
randno = np.random.rand(10,5)
#print(randno) but no print occurs....


# In[184]:


randno = numpy.random.rand(10,5)
print(randno)


# In[185]:


np.mean(randno)


# In[186]:


np.max(randno)


# In[187]:


np.min(randno)


# In[188]:


import matplotlib


# In[189]:


import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.write_html('first_figure.html', auto_open=True)


# In[190]:


import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[10, 20, 30]))
fig.show()


# In[191]:


math.prod(randno)
# But the Web site said it did!!!!


# In[192]:


math.sqrt(4)


# In[193]:


math.isinf(5)


# In[194]:


math.isinf(1/0)
# if 1/0 is not infinite, then what is? (I get it that we like to say "Division by 0 is undefined.")


# In[195]:


math.isfinite(0)


# In[196]:


scipy.stats.median_absolute_deviation(randno)


# In[197]:


scipy.stats.gmean(randno)


# In[198]:


randnox = numpy.random.rand(100)
print(randnox)


# In[199]:


scipy.stats.gmean(randnox)


# In[200]:


get_ipython().system('pip list')


# In[201]:


get_ipython().run_line_magic('lsmagic', '')


# In[202]:


get_ipython().run_line_magic('pwd', '')


# In[203]:


get_ipython().run_line_magic('ls', '')


# In[204]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[205]:


import matplotlib.pyplot as plt
N=10000
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (10*np.random.rand(N))**2

plt.scatter(x,y, s=area, c=colors, alpha=0.5)
plt.show()


# In[206]:


get_ipython().run_cell_magic('timeit', '', 'squaressss =(n*n for n in (range(1000)))')


# In[207]:


variableName1 = 'I Love data Science'
print(variableName1)


# In[208]:


V1 = 25
V2 = 25.00
V3 = V1 + V2
print(V3)


# In[209]:


Work_Week = {'Monday': 7, 'Tuesday': 9, 'Wednesday': 6, 'Thursday': 8, 'Friday': 8}
Tot_Hrs = Work_Week['Monday'] + Work_Week['Tuesday']+ Work_Week['Wednesday']+Work_Week['Thursday']+Work_Week['Friday']
Tot_Hrs


# In[210]:


#np.min(Work_Week['Monday'], Work_Week['Tuesday'], Work_Week['Wednesday'], Work_Week['Thursday'], Work_Week['Friday'])
Mon = Work_Week['Monday']
Tue = Work_Week['Tuesday']
Wed = Work_Week['Wednesday']
Thu = Work_Week['Thursday']
Fri = Work_Week['Friday']
DAY = (Mon, Tue, Wed, Thu, Fri)

print (DAY)
np.min(DAY)


# In[ ]:




