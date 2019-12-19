#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel("./personal_names/tamil-english.xlsx")


# In[3]:


dataFrame = df


# In[4]:


dataFrame.head(5)


# In[5]:


len(dataFrame)


# In[6]:


dataFrame.tail(5)


# In[7]:


# English = 1
# Sinhala = 2
# Tamil = 3


# In[8]:


pair = []
for col in dataFrame.columns:
    if(col.lower() == 'english'):
        pair.append(1)
    elif(col.lower() == 'sinhala'):
        pair.append(2)
    elif(col.lower() == 'tamil'):
        pair.append(3)


# In[9]:


if(1 in pair):
    dataFrame.dropna(subset=['English'], inplace=True)
if(2 in pair):
    dataFrame.dropna(subset=['Sinhala'], inplace=True)
if(3 in pair):
    dataFrame.dropna(subset=['Tamil'], inplace=True)


# In[10]:


lastLetter = ['்', 'ா', 'ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ை', 'ொ', 'ோ', 'ௌ']


# In[11]:


def lastCharacterDetails(namedEntity):
    if(namedEntity[-1] in lastLetter):
        namedEntity = namedEntity[:-1]
    else:
        namedEntity = namedEntity
    return namedEntity


# In[12]:


def addMorpologyTamil(rootNamedEntity, tag):
    namedEntity = ''
    if(tag==1):     #################  ගේ
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ின்'
        elif(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யின்'
        else:
            namedEntity = (rootNamedEntity) + 'வின்' 
    elif(tag==2):     #################  ගෙන්
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ிடமிருந்து'
        elif(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யிடமிருந்து'
        else:
            namedEntity = (rootNamedEntity) + 'விடமிருந்து' 
#    elif(tag==3):     #################  සිට
#        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
#            namedEntity = rootNamedEntity + 'யிலிருந்து'
#        else:
#            namedEntity = (rootNamedEntity) + 'ிலிருந்து' 
    elif(tag==4):     #################  ගේ
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ினது'
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யினது'
        elif(rootNamedEntity[-1] == 'ா'):
            namedEntity = (rootNamedEntity) + 'வினது'
        else:
            namedEntity = rootNamedEntity + 'வினது'
    elif(tag==5):     #################  ළග
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ிடம்'
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யிடம்'
        else:
            namedEntity = (rootNamedEntity) + 'விடம்' 
#    elif(tag==6):     #################  !
 #       if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
  #          namedEntity = rootNamedEntity + 'யே'
   #     else:
    #        namedEntity = (rootNamedEntity) + 'ே' 
    elif(tag==7):     #################  ද!
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ோ'
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யோ'
        else:
            namedEntity = (rootNamedEntity) + 'வோ' 
    elif(tag==8):     #################  විසින්
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ால்'
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யால்'
        else:
            namedEntity = (rootNamedEntity) + 'வால்' 
    elif(tag==9):     #################  සමග
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ுடன்'
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யுடன்'
        else:
            namedEntity = (rootNamedEntity) + 'வுடன்' 
    elif(tag==10):     #################  සමග
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ோடு'
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யோடு'
        else:
            namedEntity = (rootNamedEntity) + 'வோடு' 
    elif(tag==11):     #################  ව
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ை'
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யை'
        else:
            namedEntity = (rootNamedEntity) + 'வை'
    elif(tag==12):     #################  ට
        if(rootNamedEntity[-1]=='்'):
            namedEntity = rootNamedEntity[:-1] + 'ுக்கு'
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'க்கு'
        else:
            namedEntity = (rootNamedEntity) + 'வுக்கு'
    elif(tag==20):     #################  
        namedEntity = rootNamedEntity 
 #   else:
  #      namedEntity = rootNamedEntity
    return namedEntity


# In[13]:


def addMorpologySinhala(rootNamedEntity, tag):
    namedEntity = ''
    if(tag==1):
        namedEntity = rootNamedEntity + 'ගේ'
    elif(tag==2):
        namedEntity = rootNamedEntity + 'ගෙන්'
#    elif(tag==3):
#        namedEntity = rootNamedEntity + ' සිට'
    elif(tag==4):
        namedEntity = rootNamedEntity + 'ගේ'
    elif(tag==5):
        namedEntity = rootNamedEntity + ' ළග'
#    elif(tag==6):
 #       namedEntity = rootNamedEntity + '!'
    elif(tag==7):
        namedEntity = rootNamedEntity + ' ද!'
    elif(tag==8):
        namedEntity = rootNamedEntity + ' විසින්'
    elif(tag==9):
        namedEntity = rootNamedEntity + ' සමග'
    elif(tag==10):
        namedEntity = rootNamedEntity + ' සමග'
    elif(tag==11):
        namedEntity = rootNamedEntity + 'ව'
    elif(tag==12):
        namedEntity = rootNamedEntity + 'ට'
    elif(tag==20):
        namedEntity = rootNamedEntity
    return namedEntity


# In[14]:


def addMorpologyEnglish(rootNamedEntity, tag):
    namedEntity = ''
    if(tag==1):
        namedEntity = rootNamedEntity + '\'s'         # 'ගේ'
    elif(tag==2):
        namedEntity = rootNamedEntity + ' from'       # 'ගෙන්'
    elif(tag==4):
        namedEntity = rootNamedEntity + '\'s'           # 'ගේ'
    elif(tag==5):
        namedEntity = rootNamedEntity + ' near'        # ' ළග'
    elif(tag==7):
        namedEntity = rootNamedEntity + '!'            # ' ද!'
    elif(tag==8):
        namedEntity = rootNamedEntity + ' by'         # ' විසින්'
    elif(tag==9):
        namedEntity = rootNamedEntity + ' with'       # ' සමග'
    elif(tag==10):
        namedEntity = rootNamedEntity + ' with'       # ' සමග'
    elif(tag==11):
        namedEntity = rootNamedEntity + ' with'      # 'ව'
    elif(tag==12):
        namedEntity = rootNamedEntity + ' to'          # 'ට'
    elif(tag==20):
        namedEntity = rootNamedEntity
    return namedEntity


# In[15]:


sinhalaVariations = []
tamilVariations = []
englishVariations = []


# In[16]:


for index, raw in dataFrame.iterrows():
    if(1 in pair):
        englishBuffer = [raw['English']]
    if(2 in pair):
        sinhalaBuffer = [raw['Sinhala']]
    if(3 in pair):
        tamilBuffer = [raw['Tamil']]
    mixedBuffer = []
    englishMorpology = ''
    sinhalaMorpology = ''
    tamilMorpology = ''
    for tag in range(1, 13):
        if(tag == 3 or tag == 6):
            continue
        if(1 in pair):
            englishMorpology = addMorpologyEnglish(raw['English'], tag)
            englishBuffer.append(englishMorpology)
        if(2 in pair):
            sinhalaMorpology = addMorpologySinhala(raw['Sinhala'], tag)
            sinhalaBuffer.append(sinhalaMorpology)
        if(3 in pair):
            tamilMorpology = addMorpologyTamil(raw['Tamil'], tag)
            tamilBuffer.append(tamilMorpology) 
#     ----------
    if(1 in pair):
        englishVariations.extend(englishBuffer)
    if(2 in pair):
        sinhalaVariations.extend(sinhalaBuffer)
    if(3 in pair):
        tamilVariations.extend(tamilBuffer)
    


# In[17]:


if(1 in pair):
    print(len(englishVariations))
if(2 in pair):
    print(len(sinhalaVariations))
if(3 in pair):
    print(len(tamilVariations))


# In[18]:


if(1 in pair):
    englishSeries = pd.Series(englishVariations, name="English")
if(2 in pair):
    sinhalaSeries = pd.Series(sinhalaVariations, name="Sinhala")
if(3 in pair):
    tamilSeries = pd.Series(tamilVariations, name="Tamil")


# In[19]:


if((1 in pair) and (2 in pair)):
    data = pd.DataFrame({'English':englishSeries, 'Sinhala':sinhalaSeries})
if((1 in pair) and (3 in pair)):
    data = pd.DataFrame({'English':englishSeries, 'Tamil':tamilSeries})
if((2 in pair) and (3 in pair)):
    data = pd.DataFrame({'Sinhala':sinhalaSeries, 'Tamil':tamilSeries})


# In[20]:


data.head()


# In[21]:


export_excel = data.to_excel('./personal_names/tamil-english-morpo.xlsx', index = None, header=True)


# In[ ]:





# In[32]:


a = 'ின்'


# In[33]:


print(a)


# In[ ]:




