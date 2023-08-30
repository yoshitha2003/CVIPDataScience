#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


# Load data from CSV file
data = pd.read_csv('country_wise_latest.csv')
data


# In[11]:


print(data.head())
print(data.info())


# In[17]:


data.dtypes[data.dtypes == 'int64']


# In[18]:


data.isnull().any()


# In[23]:


data_original= data[data['Country/Region'].isin(['US', 'India'])][['Country/Region', 'Confirmed','Recovered']]
data_original = data_original.set_index('Country/Region')
data_original


# In[46]:


data_original.plot.bar()


# In[25]:


data_new = data[['Country/Region', 'New cases', 'New deaths', 'New recovered']]
data_new


# In[47]:


data_new= data[data['Country/Region'].isin(['US', 'India'])][['Country/Region', 'New cases', 'New deaths', 'New recovered']]
data_new = data_new.set_index('Country/Region')
data_new


# In[48]:


data_new.plot.bar()


# In[26]:


Country_based_new_case = data_new.groupby('Country/Region')['New cases'].sum()
Country_based_new_case


# In[45]:


Top_20_countries = Country_based_new_case.sort_values(ascending=False).head(20)
colors = plt.cm.rainbow(range(len(Top_20_countries)))
plt.bar(Top_10_countries.index, Top_20_countries.values,color=colors)
plt.xlabel('Country',color='r')
plt.ylabel('New cases',color='r')
plt.title('Top 20 Countries by New cases')
plt.xticks(rotation=65)
plt.show()


# In[41]:


import numpy as np
Recovered_number=data['Recovered']
Deaths_number=data['Deaths']
Recovered_number = np.array(Recovered_number)
Deaths_number = np.array(Deaths_number)
color_map = np.where(Deaths_number < 1000, 'green', 'red')
plt.scatter(Recovered_number, Deaths_number, color=color_map)
x_label = plt.xlabel('Recovered Number')
x_label.set_color('blue')
y_label = plt.ylabel('Deaths Number')
y_label.set_color('blue')
plt.title('Relationship between Recover Number and Deaths Number')
plt.show()


# In[42]:


data[data.Deaths<100]
data_2=data[~(data.Deaths<100)]
data_2


# In[ ]:




