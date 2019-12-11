#!/usr/bin/env python
# coding: utf-8

# In[160]:


def load_api_txt(filepath):
    api_matrix = np.loadtxt(filepath)
    api_matrix = api_matrix[:,list([0])+list(range(3,11))]
    return api_matrix

def load_location_txt(filepath):
    location_matrix = np.loadtxt(filepath)
    location_matrix = location_matrix[:,list([0])+list(range(3,7))]
    return location_matrix

def load_motion_txt(filepath):
    motion_matrix = np.loadtxt(filepath)
    motion_matrix = motion_matrix[:,list(range(0,20))]
    return motion_matrix


# In[172]:


import numpy as np
users = ["1","2","3"]
days = {"1": ["220617","260617","270617"],
       "2": ["140617","140717","180717"],
       "3": ["030717","070717","140617"]}
locations = ["Bag","Hand","Hips","Torso"]
# data = ["API","Location","Motion"]
data = ["API","Location"]


# In[175]:


# WARNING WARNING WARNING
# THE TOTAL DATA SIZE IS 27GB, so DON'T RUN THE ENTIRE LOOP
# Avoid loading motion data, since it is significantly large

# stores all data in a dictionary([user][day][location][data]),
# with each file represented as a matrix
# the 0th column of the matrix should be treated as a key in the database
user_dict = {}
for user in users:
    day_dict = {}
    for day in days[user]:
        location_dict = {}
        for location in locations:
            data_dict={}
            for datum in data:
                filepath = "User" + user + "/" + day + "/" + location + "_" + datum + ".txt"  
                if datum == "API":
                    matrix = load_api_txt(filepath)
                elif datum == "Location":
                    matrix = load_location_txt(filepath)
                elif datum == "Motion":
                    matrix = load_motion_txt(filepath)
                data_dict[datum] = matrix
            location_dict[location] = data_dict
        day_dict[day] = location_dict
    user_dict[user] = day_dict


# In[177]:


user_dict['1']['260617']['Hand']['API']


# In[174]:


filepath


# In[152]:


load_location_txt(filepath)

