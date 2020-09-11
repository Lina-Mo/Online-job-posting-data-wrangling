#!/usr/bin/env python
# coding: utf-8

# # Data Wrangling of Job posting Data Set

# ## Gather

# In[1]:


# Import libraries
import zipfile
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


# Extract all content from zip file
with zipfile.ZipFile('armenian-online-job-postings.zip','r') as myzip:
    myzip.extractall()


# In[3]:


# Read CSV (comma-separated) file into Dataframe
df = pd.read_csv('online-job-postings.csv')


# ## Assess

# In[4]:


# Review data set
df


# ### Data Set issues
# 
# - Missing values (NaN)
# - StartDate inconsistencies (ASAP)

# In[5]:


# Display the first five rows of the DataFrame using .head
df.head()


# In[6]:


# Display the last five rows of the DataFrame using .tail
df.tail()


# In[7]:


# Display a basic summary of the DataFrame using .info
df.info()


# In[8]:


# Display the entry counts for the Year column using .value_counts
df.Year.value_counts()


# - Nondescriptive column headers.
# - Missing values (NaN)
# - StartDate inconsistencies (ASAP)
# - Nondescriptive column headers (ApplicationP, AboutC, RequiredQual ... and also JobRequirment)

# ## Clean

# #### Define
# 
# - Select all nondescriptive and misspelled column headers (ApplicationP, AboutC, RequiredQual, JobRequirment) and replace them with full words (ApplicationProcedure, AboutCompany, RequiredQualifications, JobRequirement)
# - Select all records in the StartDate column that have "As soon as possible", "Immediately", etc. and replace the text in those cells with "ASAP"

# #### Code

# In[9]:


# Create copy of data set
df_clean = df.copy()


# - Select all nondescriptive and misspelled column headers (ApplicationP, AboutC, RequiredQual, JobRequirment) and replace them with full words (ApplicationProcedure, AboutCompany, RequiredQualifications, JobRequirement)

# In[10]:


df_clean = df_clean.rename(columns={'ApplicationP': 'ApplicationProcedure', 'AboutC':'AboutCompany', 'RequiredQual': 'RequiredQualifications', 
                                    'JobRequirment': 'JobRequirement'})


# - Select all records in the StartDate column that have "As soon as possible", "Immediately", etc. and replace the text in those cells with "ASAP"

# In[11]:


asap_list = ['Immediately', 'As soon as possible', 'Upon hiring',
             'Immediate', 'Immediate employment', 'As soon as possible.', 'Immediate job opportunity',
             '"Immediate employment, after passing the interview."',
             'ASAP preferred', 'Employment contract signature date',
             'Immediate employment opportunity', 'Immidiately', 'ASA',
             'Asap', '"The position is open immediately but has a flexible start date depending on the candidates earliest availability."',
             'Immediately upon agreement', '20 November 2014 or ASAP',
             'immediately', 'Immediatelly',
             '"Immediately upon selection or no later than November 15, 2009."',
             'Immediate job opening', 'Immediate hiring', 'Upon selection',
             'As soon as practical', 'Immadiate', 'As soon as posible',
             'Immediately with 2 months probation period',
             '12 November 2012 or ASAP', 'Immediate employment after passing the interview',
             'Immediately/ upon agreement', '01 September 2014 or ASAP',
             'Immediately or as per agreement', 'as soon as possible',
             'As soon as Possible', 'in the nearest future', 'immediate',
             '01 April 2014 or ASAP', 'Immidiatly', 'Urgent',
             'Immediate or earliest possible', 'Immediate hire',
             'Earliest  possible', 'ASAP with 3 months probation period.',
             'Immediate employment opportunity.', 'Immediate employment.',
             'Immidietly', 'Imminent', 'September 2014 or ASAP', 'Imediately']

for a in asap_list:
    df_clean.StartDate.replace( to_replace=a, value='ASAP', inplace=True)


# #### Test

# In[12]:


df_clean.head()


# In[13]:


df_clean.info()


# In[14]:


df_clean.StartDate.value_counts()


# In[15]:


for a in asap_list:
    assert a not in df_clean.StartDate.values


# ## Analysis & Visualization

# In[16]:


# Number of 'ASAP' start dates (numerator)
asap_counts = df_clean.StartDate.value_counts()['ASAP']
asap_counts


# In[17]:


# Number of non-empty start dates (denominator)
non_empty_counts = df_clean.StartDate.count()
non_empty_counts


# In[18]:


# Precentage of positions with an urgent start data i.e. 'ASAP'
asap_counts/non_empty_counts


# In[19]:


# Create visualization for Start Date 
labels = np.full(len(df_clean.StartDate.value_counts()), "", dtype=object)
labels[0] = 'ASAP'
df_clean.StartDate.value_counts().plot(kind="pie", labels=labels)


# In[ ]:




