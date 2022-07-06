#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.scatterplot()


# In[29]:


sns.set_style('darkgrid')
plt.rcParams['font.size'] = 15
plt.rcParams['figure.figsize'] = (10,7)
plt.rcParams['figure.facecolor']= '#FFE5B4'


# In[31]:


df = pd.read_csv('salary report.csv')


# In[32]:


df


# In[34]:


df.head(5)


# In[36]:


df.tail(5)


# In[38]:


df.columns


# In[40]:


df.isnull().sum()


# In[42]:


sns.scatterplot()


# In[46]:


sns.scatterplot(x='salary',y='rank', hue = 'sex',s = 200,data=df);

plt.legend(loc = 'upper right', fontsize = '12')


# In[48]:


rank_salary  = df.groupby('rank')['salary'].sum()
rank_salary  


# In[50]:


rank_salary.plot.pie(autopct = '%1.1f%%')
plt.title('salary through rank')


# In[55]:


total_service = df.groupby('rank')[["yrs.service"]].count()
print(total_service)


# In[57]:


cor = df.corr(method = 'pearson')
f, ax = plt.subplots(figsize = (10,5))
sns.heatmap(cor, mask = np.zeros_like(cor, dtype=np.bool),
            cmap='Blues',square=True, ax=ax)


# In[63]:


total_time = df.groupby('rank')[['salary']].mean()
total_time


# In[64]:


plt.rcParams['figure.figsize'] = (12,8)
plt.title('salary with different rank')
plt.xlabel('rank', fontsize = 12)
plt.ylabel('salary', fontsize = 15)
plt.xticks(rotation = 30, ha='right')
plt.bar(total_time.index, total_time.salary)

