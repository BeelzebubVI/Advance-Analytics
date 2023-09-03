#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as pl
import pandas as pd


# In[2]:


df = pd.DataFrame(dict(
x = [1,2,3,4],
y = [1,2,3,4]
))

fig = pl.line(df, x="x", y="y", title = "Unsorted Input")
fig.show()


# In[3]:


df = df.sort_values(by="x")
fig = pl.line(df, x = "x", y="y", title = "sorted Input")
fig.show()


# In[4]:


df = pd.read_csv('Downloads/lex.csv')


# In[5]:


df.head()


# In[6]:


fig = pl.line (df, x = "country", y="1800", title = "Life Expectancy")
fig.show()


# In[11]:


import numpy as np


# In[13]:


df = pl.data.gapminder().query("continent=='Oceania'")
fig = pl.line(df, x="year", y="lifeExp", color='country')
fig.show()


# In[14]:


df = pl.data.gapminder().query("continent == 'Oceania'")
fig = pl.line(df, x='year', y='lifeExp', color='country', markers=True)
fig.show()


# In[15]:


df = pl.data.gapminder().query("country in ['Canada', 'Botswana']")

fig = pl.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
fig.update_traces(textposition="bottom right")
fig.show()


# In[17]:


df = pl.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' 
fig = pl.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()


# In[18]:


df = pl.data.gapminder().query("continent == 'Asia'")
fig = pl.pie(df, values='pop', names='country')
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.show()


# In[21]:


import numpy as np
df = pl.data.gapminder().query("year == 2008")
fig = pl.sunburst(df, path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.show()


# In[ ]:




