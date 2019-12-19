#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel("./locations/Tamil-English.xlsx")


# In[3]:


dataFrame = df


# In[4]:


dataFrame.tail(5)


# In[5]:


# English = 1
# Sinhala = 2
# Tamil = 3


# In[6]:


pair = []
for col in dataFrame.columns:
    if(col.lower() == 'english'):
        pair.append(1)
    elif(col.lower() == 'sinhala'):
        pair.append(2)
    elif(col.lower() == 'tamil'):
        pair.append(3)


# In[7]:


if(1 in pair):
    dataFrame.dropna(subset=['English'], inplace=True)
if(2 in pair):
    dataFrame.dropna(subset=['Sinhala'], inplace=True)
if(3 in pair):
    dataFrame.dropna(subset=['Tamil'], inplace=True)


# In[8]:


lastLetter = ['்', 'ா', 'ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ை', 'ொ', 'ோ', 'ௌ']


# In[9]:


def lastCharacterDetails(namedEntity):
    if(namedEntity[-1] in lastLetter):
        namedEntity = namedEntity[:-1]
    else:
        namedEntity = namedEntity
    return namedEntity


# In[10]:


def addMorpologyTamil(rootNamedEntity, tag):
    namedEntity = ''
    if(tag==1):     #################  සිට
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யிலிருந்து'
        else:
            namedEntity = lastCharacterDetails(rootNamedEntity) + 'ிலிருந்து' 
    elif(tag==2):     #################  ළග
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யிடம்'
        else:
            namedEntity = lastCharacterDetails(rootNamedEntity) + 'விடம்'  
    elif(tag==3):     #################  ද!
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யோ'
        else:
            namedEntity = lastCharacterDetails(rootNamedEntity) + 'ோ' 
    elif(tag==4):     #################  ට
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'க்கு'
        else:
            namedEntity = lastCharacterDetails(rootNamedEntity) + 'ுக்கு'
    elif(tag==5):     #################  දක්වා
     #   if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
      #      namedEntity = rootNamedEntity + 'க்கு'
       # else:
        namedEntity = rootNamedEntity + 'வரை'
    elif(tag==6):     ################# ඉන්, එන් - ම
        namedEntity = rootNamedEntity + 'யில்'
    elif(tag==10):     #################  
        namedEntity = rootNamedEntity 
    return namedEntity


# In[11]:


def addMorpologySinhala(rootNamedEntity, tag):
    namedEntity = ''
    if(tag==1):
        namedEntity = rootNamedEntity + ' සිට' #-----  'from '
    elif(tag==2):
        namedEntity = rootNamedEntity + ' ළග' #-----  'near '
    elif(tag==3):
        namedEntity = rootNamedEntity + ' ද!' #----- '!'
    elif(tag==4):
        namedEntity = rootNamedEntity + 'ට' #-----    'to '
    elif(tag==5):
        namedEntity = rootNamedEntity + ' දක්වා' #----- 'to '
    elif(tag==6):                                # 'from '
        listException = ['ක', 'ල', 'ව', 'ය', 'න', 'ත', 'ග', 'ද']
        lastLetter = ['்', 'ா', 'ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ை', 'ொ', 'ோ', 'ௌ']
        if(rootNamedEntity[-1] in lastLetter):
            namedEntity = rootNamedEntity + 'න්'
        elif(rootNamedEntity[-1] in listException):
            namedEntity = rootNamedEntity + 'ෙන්'
        else:
            namedEntity = rootNamedEntity + 'ින්' #-----
    elif(tag==10):
        namedEntity = rootNamedEntity
    return namedEntity


# In[12]:


def addMorpologyEnglish(rootNamedEntity, tag):
    namedEntity = ''
    if(tag==1):
        namedEntity = rootNamedEntity + ' from'       # ' සිට' 
    elif(tag==2):
        namedEntity = rootNamedEntity + ' near'      # ' ළග'
    elif(tag==3):
        namedEntity = rootNamedEntity + '!'            # ' ද!'
    elif(tag==4):
        namedEntity = rootNamedEntity + ' to'          # 'ට'
    elif(tag==5):
        namedEntity = rootNamedEntity + ' to'          # ' දක්වා'
    elif(tag==6):
        namedEntity = rootNamedEntity + ' from'        # 'ඉන්'
    elif(tag==10):
        namedEntity = rootNamedEntity
    return namedEntity


# In[13]:


sinhalaVariations = []
tamilVariations = []
englishVariations = []


# In[14]:


for index, raw in dataFrame.iterrows():
    if(1 in pair):
        englishBuffer = [raw['English']]
    if(2 in pair):
        sinhalaBuffer = [raw['Sinhala']]
    if(3 in pair):
        tamilBuffer = [raw['Tamil']]
    
    mixedBuffer = []
    for tag in range(1, 7):
        if(1 in pair):
            englishMorpology = addMorpologyEnglish(raw['English'], tag)
            englishBuffer.append(englishMorpology)
        if(2 in pair):
            sinhalaMorpology = addMorpologySinhala(raw['Sinhala'], tag)
            sinhalaBuffer.append(sinhalaMorpology)
        if(3 in pair):
            tamilMorpology = addMorpologyTamil(raw['Tamil'], tag)
            tamilBuffer.append(tamilMorpology)
    if(1 in pair):
        englishVariations.extend(englishBuffer)
    if(2 in pair):
        sinhalaVariations.extend(sinhalaBuffer)
    if(3 in pair):
        tamilVariations.extend(tamilBuffer)


# In[15]:


if(1 in pair):
    print(len(englishVariations))
if(2 in pair):
    print(len(sinhalaVariations))
if(3 in pair):
    print(len(tamilVariations))


# In[16]:


if(1 in pair):
    englishSeries = pd.Series(englishVariations, name="English")
if(2 in pair):
    sinhalaSeries = pd.Series(sinhalaVariations, name="Sinhala")
if(3 in pair):
    tamilSeries = pd.Series(tamilVariations, name="Tamil")


# In[17]:


if((1 in pair) and (2 in pair)):
    data = pd.DataFrame({'English':englishSeries, 'Sinhala':sinhalaSeries})
if((1 in pair) and (3 in pair)):
    data = pd.DataFrame({'English':englishSeries, 'Tamil':tamilSeries})
if((2 in pair) and (3 in pair)):
    data = pd.DataFrame({'Sinhala':sinhalaSeries, 'Tamil':tamilSeries})


# In[18]:


data.head()


# In[19]:


export_excel = data.to_excel('./locations/Tamil-English-morpo.xlsx', index = None, header=True)


# In[ ]:





# In[24]:


a = 'ுக்கு'
print(a)


# In[ ]:




