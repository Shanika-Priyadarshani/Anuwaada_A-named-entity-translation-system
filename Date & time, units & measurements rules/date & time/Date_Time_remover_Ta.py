#!/usr/bin/env python
# coding: utf-8

# In[20]:


import datetime


# In[21]:


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


# In[22]:


def validateTime(time_text):
    try:
        if(datetime.datetime.strptime(time_text, '%H:%M')):
            return 7
        elif(datetime.datetime.strptime(time_text, '%H:%M:%S')):
            return 8
    except ValueError:
        return False


# In[23]:


def matcherTa(inputString):
    resultList = []
    splittedArray = str(inputString).split(" ")
    for inde, ele in enumerate(splittedArray):
        outputList = []
        outputList.append(ele)
        if(validateDate(ele)):
            outputList.append(validateDate(ele))
        elif(validateTime(ele)):
            outputList.append(validateTime(ele))
        elif(ele == "முற்பகல்"):
            outputList.append(9)
        elif(ele == "பிற்பகல்"):
            outputList.append(10)
#             ------------------
        elif(ele == "ஜனவரி"):
            outputList.append(11)
        elif(ele == "பிப்ரவரி"):
            outputList.append(12)
        elif(ele == "மார்ச்"):
            outputList.append(13)
        elif(ele == "ஏப்ரல்"):
            outputList.append(14)
        elif(ele == "மே"):
            outputList.append(15)
        elif(ele == "ஜூன்"):
            outputList.append(16)
        elif(ele == "ஜூலை"):
            outputList.append(17)
        elif(ele == "ஆகஸ்ட்" or ele == "ஆகஸ்டு"):
            outputList.append(18)
        elif(ele == "செப்டம்பர்"):
            outputList.append(19)
        elif(ele == "அக்டோபர்"):
            outputList.append(20)
        elif(ele == "நவம்பர்"):
            outputList.append(21)
        elif(ele == "டிசம்பர்"):
            outputList.append(22)
#             -------------------
        elif(ele == "ஜன." or ele == "ஜன"):
            outputList.append(23)
        elif(ele == "பிப்." or ele == "பிப்"):
            outputList.append(24)
        elif(ele == "மார்." or ele == "மார்"):
            outputList.append(25)
        elif(ele == "ஏப்." or ele == "ஏப்"):
            outputList.append(26)
        elif(ele == "மே"):
            outputList.append(27)
        elif(ele == "ஜூன்"):
            outputList.append(28)
        elif(ele == "ஜூலை"):
            outputList.append(29)
        elif(ele == "ஆக." or ele == "ஆக"):
            outputList.append(30)
        elif(ele == "செப்." or ele == "செப்"):
            outputList.append(31)
        elif(ele == "அக்." or ele == "அக்"):
            outputList.append(32)
        elif(ele == "நவ." or ele == "நவ"):
            outputList.append(33)
        elif(ele == "டிச." or ele == "டிச"):
            outputList.append(34)
#             -----------------
        elif(ele == "காலாண்டு"):
            outputList.append(35)
#             -----------------
        elif(ele == "ஞாயிறு"):
            outputList.append(36)
        elif(ele == "திங்கள்"):
            outputList.append(37)
        elif(ele == "செவ்வாய்"):
            outputList.append(38)
        elif(ele == "புதன்"):
            outputList.append(39)
        elif(ele == "வியாழன்"):
            outputList.append(40)
        elif(ele == "வெள்ளி"):
            outputList.append(41)
        elif(ele == "சனி"):
            outputList.append(42)
        elif(ele == "ஞாயி." or ele == "ஞாயி"):
            outputList.append(43)
        elif(ele == "திங்." or ele == "திங்"):
            outputList.append(44)
        elif(ele == "செவ்." or ele == "செவ்"):
            outputList.append(45)
        elif(ele == "புத." or ele == "புத"):
            outputList.append(46)
        elif(ele == "வியா." or ele == "வியா"):
            outputList.append(47)
        elif(ele == "வெள்." or ele == "வெள்"):
            outputList.append(48)
        elif(ele == "சனி." or ele == "சனி"):
            outputList.append(49)
#             ------------------
        elif(ele == "நள்ளிரவு"):
            outputList.append(50)
        elif(ele == "நண்பகல்"):
            outputList.append(51)
        elif(ele == "அதிகாலை" or ele == "காலை"):
            outputList.append(52)
        elif(ele == "மதியம்" or ele == "பிற்பகல்"):
            outputList.append(53)
        elif(ele == "மாலை" or ele == "அந்தி மாலை"):
            outputList.append(54)
        elif(ele == "இரவு"):
            outputList.append(55)
#             -----------------
        elif(ele == "பொ.ச.மு" or ele == "பொசமு"):
            outputList.append(56)
        elif(ele == "பொ.ச" or ele == "பொச"):
            outputList.append(57)
        elif(ele == "கி.மு." or ele == "கிமு"):
            outputList.append(58)
        elif(ele == "பொ.ச.மு" or ele == "பொசமு"):
            outputList.append(59)
        elif(ele == "கி.பி." or ele == "கிபி"):
            outputList.append(60)
        elif(ele == "பொ.ச." or ele == "ொச"):
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
# திகதி
        elif(ele[-2:] == ('ம்') and splittedArray[inde + 1] == ('திகதி')):
#            print(splittedArray[inde + 1])
            outputList[0] = outputList[0][:-2]
            outputList.append(62)
        elif(ele == ('திகதி')):
            outputList = []
        else:
            outputList.append(0)
        if(len(outputList) != 0):
            resultList.append(outputList)
    resultList.append(3)
    return resultList


# In[24]:

#
#abc = matcher('ஜனவரி ஜனவரி 02ம் திகதி ஜனவரி 2016')
#print(abc)
#for i in abc:
#    if(isinstance(i, list)):
#        print(str(i[0]) + " " + str(i[1]))
#
#
## In[25]:
#
#
#abc = matcher('வெள்ளி 05ம் திகதி ஜனவரி முற்பகல் 10:30')
#print(abc)
#for i in abc:
#    if(isinstance(i, list)):
#        print(str(i[0]) + " " + str(i[1]))
#
#
## In[26]:
#
#
#abc = matcher('முற்பகல் 10:30')
#print(abc)
#for i in abc:
#    if(isinstance(i, list)):
#        print(str(i[0]) + " " + str(i[1]))
#
#
## In[27]:
#
#
#abc = matcher('காலை 11:50')
#print(abc)
#for i in abc:
#    if(isinstance(i, list)):
#        print(str(i[0]) + " " + str(i[1]))
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
