#!/usr/bin/env python
# coding: utf-8

# In[119]:


import requests
import pandas as pd  
import json
from datetime import datetime
from datetime import timedelta


# In[125]:


dates = [datetime.now().strftime('%d-%m-%Y'),(datetime.now() + timedelta(days=7) ).strftime('%d-%m-%Y'),(datetime.now() + timedelta(days=14) ).strftime('%d-%m-%Y')]


# In[147]:


pincode = input('Enter your pincode: ')


# In[148]:


def checkIfVaccineAvailable(response,date): 
    json_data = json.loads(response.text)
    flag = False
    for val in json_data['centers']:
        for session in val.get('sessions'):
            if(session.get('min_age_limit') != 45):
                print("Vaccination found in Center: ",val.get('name')+" on Date: "+session.get('date'))
                flag = True
        
    if not flag:
        print("Vaccination not found")
        


# In[149]:


for date in dates:
    body = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=' + pincode +'&date=' + date
    response = requests.get(body)
    checkIfVaccineAvailable(response,date)


# In[ ]:




