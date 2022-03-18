#!/usr/bin/env python
# coding: utf-8

# In[1]:


# List of high schools
high_schools = ["Hernandez High School", "Figueroa High School",
                "Wilson High School","Wright High School"]


# In[2]:


for school in high_schools:
    print(school)


# In[ ]:


# A dictionary of high schools and the type of school.
high_school_types = [{"High School": "Griffin", "Type":"District"},
                    {"High School": "Figueroa", "Type": "District"},
                    {"High School": "Wilson", "Type": "Charter"},
                    {"High School": "Wright", "Type": "Charter"}]


# In[18]:


for i in high_school_types:
    print(i)


# In[21]:


# List of high schools
high_schools = ["Huang High School",  "Figueroa High School", "Shelton High School", "Hernandez High School","Griffin High School","Wilson High School", "Cabrera High School", "Bailey High School", "Holden High School", "Pena High School", "Wright High School","Rodriguez High School", "Johnson High School", "Ford High School", "Thomas High School"]


# In[22]:


# Add the Pandas dependency.
import pandas as pd


# In[23]:


# Create a Pandas Series from a list.
school_series = pd.Series(high_schools)


# In[49]:


# Iterate through the school_series and print out each high school
school = list(school_series)
for i in school:
    print(i)
       


# In[50]:


# A dictionary of high schools
high_school_dicts = [{"School ID": 0, "school_name": "Huang High    School", "type": "District"},
                   {"School ID": 1, "school_name": "Figueroa High School", "type": "District"},
                    {"School ID": 2, "school_name":"Shelton High School", "type": "Charter"},
                    {"School ID": 3, "school_name":"Hernandez High School", "type": "District"},
                    {"School ID": 4, "school_name":"Griffin High School", "type": "Charter"}]


# In[51]:


school_df = pd.DataFrame(high_school_dicts)
school_df


# In[52]:


# Three separate lists of information on high schools
school_id = [0, 1, 2, 3, 4]

school_name = ["Huang High School", "Figueroa High School",
"Shelton High School", "Hernandez High School","Griffin High School"]

type_of_school = ["District", "District", "Charter", "District","Charter"]


# In[53]:


# Initialize a new DataFrame.
schools_df = pd.DataFrame()


# In[54]:


# Add the list to a new DataFrame.
schools_df["School ID"] = school_id

# Print the DataFrame.
schools_df


# In[60]:


schools_df["school_name"] = school_name
schools_df["type"] = type_of_school
print(schools_df)


# In[61]:


# Add the list to a new DataFrame.
schools_df["School ID"] = school_id

# Print the DataFrame.
schools_df


# In[62]:


# Create a dictionary of information on high schools.
high_schools_dict = {'School ID': school_id, 'school_name':school_name, 'type':type_of_school}


# In[63]:


high_schools_dict = pd.DataFrame()


# In[64]:


school_df.columns


# In[65]:


school_df.index


# In[66]:


school_df.values


# In[85]:


for i in schools_df:
    b = list(school_id)
    c = list(school_name)
    d = list(type_of_school)


# In[86]:


new_df = pd.DataFrame()
new_df["b"] = school_id
new_df["c"] = school_name
new_df["d"] = type_of_school
print(new_df.values)


# In[ ]:




