#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Units_adder_En import *
from Units_adder_Si import *
from Units_adder_Ta import *


# In[2]:


from Units_remover_En import *
from Units_remover_Si import *
from Units_remover_Ta import *


# In[3]:


# English = 1
# Sinhala = 2
# Tamil = 3


# In[4]:


def getOutput(inputString, sourceLanguage, targetLanguage):
    if(int(sourceLanguage) == 1 and int(targetLanguage) == 2):
        return converterSi(formatterEn(inputString))
    elif(int(sourceLanguage) == 1 and int(targetLanguage) == 3):
        return converterTa(formatterEn(inputString))
    elif(int(sourceLanguage) == 2 and int(targetLanguage) == 1):
        (formatterSi(inputString))
        return converterEn(formatterSi(inputString))
    elif(int(sourceLanguage) == 2 and int(targetLanguage) == 3):
        return converterTa(formatterSi(inputString))
    elif(int(sourceLanguage) == 3 and int(targetLanguage) == 1):
        return converterEn(formatterTa(inputString))
    elif(int(sourceLanguage) == 3 and int(targetLanguage) == 2):
        return converterSi(formatterTa(inputString))
    else:
        return "Error found"


# In[5]:


print(getOutput("1 cm", 1, 2))


# In[6]:


print(getOutput("1 Centimeter", 1, 3))


# In[7]:


print(getOutput("මි.මී. 100.98", 2, 1))


# In[8]:


print(getOutput("මි.මී. 100.98", 2, 1))


# In[9]:


print(getOutput("මි.මී. 100.98", 2, 1))


# In[10]:


print(getOutput("சென்டிமீட்டர் 1.0", 3, 1))


# In[11]:


print(getOutput("சென்டிமீட்டர் 1.0", 3, 2))


# In[12]:


print(getOutput("මි.මී. 100.98", 2, 3))


# In[ ]:




