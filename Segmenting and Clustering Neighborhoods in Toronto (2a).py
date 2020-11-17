#!/usr/bin/env python
# coding: utf-8

# <h1>To explore, segment, and cluster the neighborhoods in the city of Toronto</h1>
# 

# import libaries

# In[1]:


get_ipython().system('pip install lxml')


# In[2]:


get_ipython().system('pip install wikipedia')


# In[3]:


import wikipedia as wp
import pandas as pd

import requests
import io

get_ipython().system('pip install bs4')
from bs4 import BeautifulSoup


# Scrape the data from wikipedia page

# In[4]:


html=wp.page("List of postal codes of Canada: M").html().encode("UTF-8")


# The dataframe will consist of three columns: PostalCode, Borough, and Neighborhood

# In[33]:


df=pd.read_html(html,header =0)[0]
df.columns=["Postalcode","Borough","Neighbourhood"]
df.head(10)


# import numpy as np # library to handle data in a vectorized manner
# 
# import pandas as pd # library for data analsysis
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# 
# import json # library to handle JSON files
# 
# !conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
# from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
# 
# import requests # library to handle requests
# from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe
# 
# # Matplotlib and associated plotting modules
# import matplotlib.cm as cm
# import matplotlib.colors as colors
# 
# # import k-means from clustering stage
# from sklearn.cluster import KMeans
# 
# #!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
# import folium # map rendering library
# 
# print('Libraries imported.')

# #!pip install html5lib

# Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned.

# In[34]:


# Ignore cells with a borough that is Not assigned
df=df[df.Borough!='Not assigned']
df.head()


# In[36]:


# Reset index
df.reset_index(drop=True, inplace=True)


# In[37]:


df.head()


# In[46]:


# More than one neighborhood can exist in one postal code area. 
# These rows will be combined into one row with the neighborhoods
df.loc[df['Neighbourhood']=='Not assigned', 'Neighbourhood']=df['Borough']
df.head()


# In[43]:


# Check how many unique neighbourhoos exist
df['Borough'].unique()


# If a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough.

# In[48]:


# Not assigned neighbourhood will be assigned the same as the borough
df.groupby(['Borough'])['Neighbourhood'].apply(', '.join)
df.head()


# In[50]:


# Check the size
df.shape


# In[52]:


get_ipython().system('pip install geopy')


# In[53]:


get_ipython().system('pip install geocoder')


# In[54]:


import geocoder


# from geopy.geocoder import Nominatim

# In[55]:


latitude=[]
longitude=[]
for code in neighbours['Postal Code']:
    g = geocoder.arcgis('{}, Toronto, Ontario'.format(code))
    print(code, g.latlng)
    while (g.latlng is None):
        g = geocoder.arcgis('{}, Toronto, Ontario'.format(code))
        print(code, g.latlng)
    latlng = g.latlng
    latitude.append(latlng[0])
    longitude.append(latlng[1])


# df = pd.DataFrame[neighbours[neighbours.Borough]
# 

# In[ ]:





# In[ ]:




