#!/usr/bin/env python
# coding: utf-8

# In[23]:


import datetime


# In[24]:


def validateDate(date_text):
    try:
        (datetime.datetime.strptime(date_text, '%Y/%m/%d'))
        return 1
    except ValueError:
        try:
            (datetime.datetime.strptime(date_text, '%d/%m/%Y'))
            return 2
        except ValueError:
            try:
                (datetime.datetime.strptime(date_text, '%Y.%m.%d'))
                return 3
            except ValueError:
                try:
                    (datetime.datetime.strptime(date_text, '%d.%m.%Y'))
                    return 4
                except ValueError:
                    try:
                        (datetime.datetime.strptime(date_text, '%Y-%m-%d'))
                        return 5
                    except ValueError:
                        try:
                            (datetime.datetime.strptime(date_text, '%d-%m-%Y'))
                            return 6
                        except ValueError:
                            return False


# In[25]:


def validateTime(time_text):
    try:
        if(datetime.datetime.strptime(time_text, '%H:%M')):
            return 7
        elif(datetime.datetime.strptime(time_text, '%H:%M:%S')):
            return 8
    except ValueError:
        return False


# In[26]:


def matcherEn(inputString):
    resultList = []
    splittedArray = str(inputString).split(" ")
    for ele in splittedArray:
        outputList = []
        outputList.append(ele)
        if(validateDate(ele)):
            outputList.append(validateDate(ele))
        elif(validateTime(ele)):
            outputList.append(validateTime(ele))
        elif(ele.lower() == "a.m." or ele.lower() == "am"):
            outputList.append(9)
        elif(ele.lower() == "p.m." or ele.lower() == "pm"):
            outputList.append(10)
#             ------------------
        elif(ele.lower() == "january"):
            outputList.append(11)
        elif(ele.lower() == "february"):
            outputList.append(12)
        elif(ele.lower() == "march"):
            outputList.append(13)
        elif(ele.lower() == "april"):
            outputList.append(14)
        elif(ele.lower() == "may"):
            outputList.append(15)
        elif(ele.lower() == "june"):
            outputList.append(16)
        elif(ele.lower() == "july"):
            outputList.append(17)
        elif(ele.lower() == "august"):
            outputList.append(18)
        elif(ele.lower() == "september"):
            outputList.append(19)
        elif(ele.lower() == "october"):
            outputList.append(20)
        elif(ele.lower() == "november"):
            outputList.append(21)
        elif(ele.lower() == "december"):
            outputList.append(22)
#             -------------------
        elif(ele.lower() == "jan." or ele.lower() == "jan"):
            outputList.append(23)
        elif(ele.lower() == "feb." or ele.lower() == "feb"):
            outputList.append(24)
        elif(ele.lower() == "mar." or ele.lower() == "mar"):
            outputList.append(25)
        elif(ele.lower() == "apr." or ele.lower() == "apr"):
            outputList.append(26)
        elif(ele.lower() == "may." or ele.lower() == "may"):
            outputList.append(27)
        elif(ele.lower() == "jun." or ele.lower() == "jun"):
            outputList.append(28)
        elif(ele.lower() == "jul." or ele.lower() == "jul"):
            outputList.append(29)
        elif(ele.lower() == "aug." or ele.lower() == "aug"):
            outputList.append(30)
        elif(ele.lower() == "sep." or ele.lower() == "sep"):
            outputList.append(31)
        elif(ele.lower() == "oct." or ele.lower() == "oct"):
            outputList.append(32)
        elif(ele.lower() == "nov." or ele.lower() == "nov"):
            outputList.append(33)
        elif(ele.lower() == "dec." or ele.lower() == "dec"):
            outputList.append(34)
#             -----------------
        elif(ele.lower() == "quarter"):
            outputList.append(35)
#             -----------------
        elif(ele.lower() == "sunday"):
            outputList.append(36)
        elif(ele.lower() == "monday"):
            outputList.append(37)
        elif(ele.lower() == "tuesday"):
            outputList.append(38)
        elif(ele.lower() == "wednesday"):
            outputList.append(39)
        elif(ele.lower() == "thursday"):
            outputList.append(40)
        elif(ele.lower() == "friday"):
            outputList.append(41)
        elif(ele.lower() == "saturday"):
            outputList.append(42)
        elif(ele.lower() == "sun"):
            outputList.append(43)
        elif(ele.lower() == "mon"):
            outputList.append(44)
        elif(ele.lower() == "tue"):
            outputList.append(45)
        elif(ele.lower() == "wed"):
            outputList.append(46)
        elif(ele.lower() == "thu"):
            outputList.append(47)
        elif(ele.lower() == "fri"):
            outputList.append(48)
        elif(ele.lower() == "sat"):
            outputList.append(49)
#             ------------------
        elif(ele.lower() == "midnight"):
            outputList.append(50)
        elif(ele.lower() == "noon"):
            outputList.append(51)
        elif(ele.lower() == "in the morning"):
            outputList.append(52)
        elif(ele.lower() == "in the afternoon"):
            outputList.append(53)
        elif(ele.lower() == "in the evening"):
            outputList.append(54)
        elif(ele.lower() == "at night"):
            outputList.append(55)
#             -----------------
        elif(ele.lower() == "before common era"):
            outputList.append(56)
        elif(ele.lower() == "common era"):
            outputList.append(57)
        elif(ele.lower() == "bc"):
            outputList.append(58)
        elif(ele.lower() == "bce"):
            outputList.append(59)
        elif(ele.lower() == "ad"):
            outputList.append(60)
        elif(ele.lower() == "ce"):
            outputList.append(61)
#             -----------------
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
#         elif():
#             outputList.append()
        elif(ele.lower()[-2:] == 'st' or ele.lower()[-2:] == 'nd' or ele.lower()[-2:] == 'rd' or ele.lower()[-2:] == 'th'):
            outputList[0] = outputList[0][:-2]
            outputList.append(62)
        else:
            outputList.append(0)
        resultList.append(outputList)
    resultList.append(1)
    return resultList


# In[27]:

#
#print(matcher('friday 05th of january 10:30 a.m.'))
#
#
## In[28]:
#
#
#print(matcher('2nd of November 2017'))
#
#
## In[29]:
#
#
#print(matcher('friday 5th of january 10:30 a.m.'))
#
#
## In[30]:
#
#
#print(matcher('sunday 2nd of january 2017 10:30 a.m.'))
#
#
## In[31]:
#
#
#print(matcher('10:30 a.m.'))
#
#
## In[32]:
#
#
#print(matcher('14/12/2018'))
#
#
## In[33]:
#
#
#print(matcher('2nd of january 2017 10:30 a.m.'))
#
#
## In[ ]:
#
#
#
#
#
## In[ ]:
#
#
#
#
#
## In[ ]:
#
#
#
#
