
# coding: utf-8

# # Beginning Gini Index Score Calculation

# ## What is a gini index?
# The gini index or gini coefficient measures "the distribution of income across a population developed by the Italian statistician Corrado Gini in 1912. It is often used as a gauge of economic inequality, measuring income distribution or, less commonly, wealth distribution among a population. The coefficient ranges from 0 (or 0%) to 1 (or 100%), with 0 representing perfect equality and 1 representing perfect inequality." - *Investopedia*
# 
# **Key Point:**
# A higher Gini index indicates greater inequality, with high income individuals receiving much larger percentages of the total income of the population.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("Income/Income_Asian_2.csv")
df


# In[3]:


df_asian = df #making a copy of our orginial df
df_asian.head()


# Since the incomes are in ranges, we'll convert them to midpoint amounts to make them easier to work with

# In[4]:


list_values = df_asian.iloc[1:,0]
list_values


# # Data Cleaning

# In[5]:


#new values for each income are the midpoint for the ranges
new_amounts = [4999, 12499, 17499, 22499, 27499, 32499, 37499, 42499, 47499, 54999, 67499, 
              87499, 112499, 137499, 174999, 200000]

for i in range(0,16):
    df_asian.iloc[i+1,0] = new_amounts[i]
df_asian.head()


# Need to rename columns so it contains county only, and we need to make the amounts of people into integers since they are currently strings. To make those numbers integers, we must first remove the commas - then we can convert type.

# In[6]:


# want to delete everything after the county name in the string
column_list = []
for i in range(0,len(df_asian.columns)):
    if i != 0: #we don't want to change the 1st column at all
        comma = df_asian.columns[i].find(",") #finds where the commas are in the string
        col_name = df_asian.columns[i][0:comma] #keeps the name of the county onlyy
        column_list = column_list + [col_name] #puts the corrected names into the list we made
column_list 


# In[7]:


#we'll rename our columns now
for i in range(0,len(column_list)):
    df_asian = df_asian.rename(columns = {df_asian.columns[i+1]: column_list[i]}) #renames the old columns to our corrected names
df_asian.head() 


# In[8]:


df_asian


# In[23]:


type(df_asian.iloc[1,3])


# Note: some numbers are strings and some are type numpy.int64. Need to convert the strings only - so make a mask.

# In[ ]:


#make a mask


# In[16]:


#some rows may have numbers with commas, we must delete the commas
#only deleted commas in Bronx at the moment
for i in range(1,len(df_asian.columns)): #searching per column
    for j in range(0,len(df_asian)): #going into that column and looking at all the rows in it
        if df_asian.iloc[j,i] == 0: #don't want to change zeros
            df_asian.iloc[j,i] = df_asian.iloc[j,i]
        elif df_asian.iloc[j,i].find(",") != -1:
            df_asian.iloc[j,i] = df_asian.iloc[j,i].replace(",","")
print(f" {df_asian.iloc[1,1]} is {type(df_asian.iloc[1,1])}")
df_asian


# In[ ]:


# need to make every row integers - all except the 1st one
for i in range(1,len(df_asian.columns)): #searching per column
    for j in range(0,len(df_asian)): #going into that column and looking at all the rows in it
        df_asian.iloc[j,i] = int(df_asian.iloc[j,i])
print(f" {df_asian.iloc[1,1]} is {type(df_asian.iloc[1,1])}")    


# ## Columns of Gini Calculation
# <img src=columns_gini.jpg width ='600'>

# ## Process for calculations
# 
# ### Fraction of Income:
# fraction = household income / sum of all incomes (so the sum of the 1st column)
# 
# ### Fraction of Pop:
# fraction = number of people with specific income/ total population of the county
# 
# The total population number for each county is the 1st row of every column
# 
# ### % Pop Richer:
# fraction = (number of people richer than specific income) / (total population of the county) **or** (sum of people above income group) / (total population of county)
# 
# For the 1st row of this category, you could do 1-(fraction of pop) since everyone would be richer than the 1st group. Last row in category should be zero since no one is richer than the last group.

# In[ ]:


#building rows of our columns
#total_income = df_asian.iloc[1:,0].sum()
#fraction_income = [round(df_asian.iloc[i+1,0]/total_income,2) for i in range(0,16)]
#fraction_population = [round(df_asian.iloc[i+1,1]/df_asian.iloc[0,1]),2 for i in range(0,16)]
#fraction_richer = [round(int(df_asian.iloc[i+1,1])/int(df_asian.iloc[i+2:,1]),2) for i in range(0,16)]


# In[ ]:


#df_asian.iloc[2:,1]


# In[ ]:


#income_series = pd.Series(fraction_income, name = "% Cumulative Share Income")
#income_pop_series = pd.Series(fraction_population, name = "% Household Income Dist")

#income_df = income_series.to_frame()
#income_pop_df = income_pop_series.to_frame()

#income_pop_combo = pd.concat([income_df, income_pop_df],axis=1)

#let's see what curve looks like
#fig, ax = plt.subplots(figsize=(15, 6))
#plt.ylabel("Number of Accidents")

#plt.scatter(fraction_income, fraction_population)

