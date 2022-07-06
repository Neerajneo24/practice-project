#!/usr/bin/env python
# coding: utf-8

# In[204]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[205]:


sns.set_style('darkgrid')
plt.rcParams['font.size'] = 15
plt.rcParams['figure.figsize'] = (10,7)
plt.rcParams['figure.facecolor']= '#FFE5B4'


# In[206]:


df = pd.read_csv('happiness report.csv')


# In[207]:


df = pd.read_csv('happiness report.csv')


# In[208]:


type(df)


# In[209]:


df


# In[210]:


df.head(5)


# In[211]:


df.tail(2)


# In[212]:


df.columns


# In[213]:


df.isnull().sum()


# In[214]:


import seaborn as sns


# In[215]:


sns.scatterplot()


# In[216]:


sns.scatterplot(x='Happiness Rank',y='Economy (GDP per Capita)', hue = 'Region',s = 200,data=df);

plt.legend(loc = 'lower left', fontsize = '8')


# In[217]:


gdp_region = df.groupby('Region')['Economy (GDP per Capita)'].sum()
gdp_region


# In[218]:


gdp_region.plot.pie(autopct = '%1.1f%%')
plt.title('GDP by region')


# In[219]:


total_country = df.groupby('Region')[["Country"]].count()
print(total_country)


# In[220]:


cor = df.corr(method = 'pearson')
f, ax = plt.subplots(figsize = (10,5))
sns.heatmap(cor, mask = np.zeros_like(cor, dtype=np.bool),
            cmap='Blues',square=True, ax=ax)


# In[221]:


#corruption in region
corruption = df.groupby('Region')[['Trust (Government Corruption)']].mean()
corruption


# In[222]:


plt.rcParams['figure.figsize'] = (12,8)
plt.title('perception of corruption in various regions')
plt.xlabel('Region', fontsize = 12)
plt.ylabel('Trust (Government Corruption)', fontsize = 15)
plt.xticks(rotation = 30, ha='right')
plt.bar(corruption.index, corruption.index)


# In[223]:


top_10 = df.head(10)
bottom_10 = df.tail(10)


# In[264]:


fig, axes= plt.subplots(1,2, figsize= (16,6))
plt.tight_layout(pad=2)
xlabels= top_10.Country
axes[0].set_title('top 10 happiest country Generosity ')
axes[0].set_xticklabels(xlabels, rotation=45, ha='right')
sns.barplot(x= top_10.Country, y= top_10.Generosity , ax = axes[0])
axes[0].set_xlabel('Country')
axes[0].set_ylabel('Generosity')

xlabels= bottom_10.Country
axes[1].set_title('top 10 least happiest country Generosity ')
axes[1].set_xticklabels(xlabels, rotation=45, ha='right')
sns.barplot(x=bottom_10.Country, y=bottom_10.Generosity , ax=axes[1])
axes[1].set_xlabel('Country')
axes[1].set_ylabel('Generosity')



# In[ ]:





# In[ ]:





# In[ ]:




