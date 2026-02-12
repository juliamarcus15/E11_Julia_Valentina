#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/juliamarcus15/E11_Julia_Valentina/refs/heads/main/data_vF.csv')
data_column = df['25um']
plt.figure()
plt.hist(data_column, bins=20)
plt.show()


# In[ ]:




