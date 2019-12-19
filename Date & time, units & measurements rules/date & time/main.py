#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Date_Time_remover_En import *
from Date_Time_remover_Si import *
from Date_Time_remover_Ta import *


# In[2]:


from Date_Time_adder_En import *
from Date_Time_adder_Si import *
from Date_Time_adder_Ta import *


# In[3]:


# English = 1
# Sinhala = 2
# Tamil = 3


# In[4]:


def getOutput(inputValue, sourceLanguage, targetLanguage):
    if(int(sourceLanguage)==1 and int(targetLanguage)==2):
        return formatterSi(matcherEn(inputValue))
    elif(int(sourceLanguage)==1 and int(targetLanguage)==3):
        return formatterTa(matcherEn(inputValue))
    elif(int(sourceLanguage)==2 and int(targetLanguage)==1):
        return formatterEn(matcherSi(inputValue))
    elif(int(sourceLanguage)==2 and int(targetLanguage)==3):
        return formatterTa(matcherSi(inputValue))
    elif(int(sourceLanguage)==3 and int(targetLanguage)==1):
        return formatterEn(matcherTa(inputValue))
    elif(int(sourceLanguage)==3 and int(targetLanguage)==2):
        return formatterSi(matcherTa(inputValue))
    else:
        return "Error found"


# In[5]:


getOutput("january 2017", 1, 2)


# In[6]:


getOutput("sunday 2nd of january 2017 10:30 a.m.", 1, 2)


# In[7]:


getOutput("sunday 2nd of january 2017 10:30 a.m.", 1, 3)


# In[8]:


getOutput("ජනවාරි 05වනදා  සිකුරාදා පෙ.ව. 10:30", 2, 1)


# In[9]:


getOutput("ජනවාරි 05වනදා  සිකුරාදා පෙ.ව. 10:30", 2, 3)


# In[10]:


getOutput("ஞாயிறு 2ம் திகதி ஜனவரி", 3, 1)


# In[11]:


getOutput("காலை 10:30 ", 2, 3)


# In[ ]:




