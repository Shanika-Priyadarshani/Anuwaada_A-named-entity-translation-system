#!/usr/bin/env python
# coding: utf-8

# In[24]:


import datetime


# In[25]:


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


# In[26]:


def validateTime(time_text):
    try:
        if(datetime.datetime.strptime(time_text, '%H:%M')):
            return 7
        elif(datetime.datetime.strptime(time_text, '%H:%M:%S')):
            return 8
    except ValueError:
        return False


# In[27]:


def matcherSi(inputString):
    resultList = []
    splittedArray = str(inputString).split(" ")
    for ele in splittedArray:
        outputList = []
#         outputList.append(ele.decode('utf-8'))
        outputList.append(ele)
        if(validateDate(ele)):
            outputList.append(validateDate(ele))
        elif(validateTime(ele)):
            outputList.append(validateTime(ele))
        elif(ele == "පෙ.ව." or ele == "පෙව"):
            outputList.append(9)
        elif(ele == "ප.ව." or ele == "පව"):
            outputList.append(10)
#             ------------------
        elif(ele == "ජනවාරි"):
            outputList.append(11)
        elif(ele == "පෙබරවාරි"):
            outputList.append(12)
        elif(ele == "මාර්තු"):
            outputList.append(13)
        elif(ele == "අප්‍රේල්"):
            outputList.append(14)
        elif(ele == "මැයි"):
            outputList.append(15)
        elif(ele == "ජූනි"):
            outputList.append(16)
        elif(ele == "ජූලි"):
            outputList.append(17)
        elif(ele == "අගෝස්තු"):
            outputList.append(18)
        elif(ele == "සැප්තැම්බර්"):
            outputList.append(19)
        elif(ele == "ඔක්තෝබර්"):
            outputList.append(20)
        elif(ele == "නොවැම්බර්"):
            outputList.append(21)
        elif(ele == "දෙසැම්බර්"):
            outputList.append(22)
#             -------------------
        elif(ele == "ජන." or ele == "ජන"):
            outputList.append(23)
        elif(ele == "පෙබ." or ele == "පෙබ"):
            outputList.append(24)
        elif(ele == "මාර්තු." or ele == "මාර්තු"):
            outputList.append(25)
        elif(ele == "අප්." or ele == "අප්"):
            outputList.append(26)
        elif(ele == "මැයි." or ele == "මැයි"):
            outputList.append(27)
        elif(ele == "ජූනි." or ele == "ජූනි"):
            outputList.append(28)
        elif(ele == "ජූලි." or ele == "ජූලි"):
            outputList.append(29)
        elif(ele == "අගෝ." or ele == "අගෝ"):
            outputList.append(30)
        elif(ele == "සැප්." or ele == "සැප්"):
            outputList.append(31)
        elif(ele == "ඔක්." or ele == "ඔක්"):
            outputList.append(32)
        elif(ele == "නොවැ." or ele == "නොවැ"):
            outputList.append(33)
        elif(ele == "දෙසැ." or ele == "දෙසැ"):
            outputList.append(34)
#             -----------------
        elif(ele == "කාර්තුව"):
            outputList.append(35)
#             -----------------
        elif(ele == "ඉරිදා"):
            outputList.append(36)
        elif(ele == "සඳුදා"):
            outputList.append(37)
        elif(ele == "අඟහරුවාදා"):
            outputList.append(38)
        elif(ele == "බදාදා"):
            outputList.append(39)
        elif(ele == "බ්‍රහස්පතින්දා"):
            outputList.append(40)
        elif(ele == "සිකුරාදා"):
            outputList.append(41)
        elif(ele == "සෙනසුරාදා"):
            outputList.append(42)
        elif(ele == "ඉරිදා"):
            outputList.append(43)
        elif(ele == "සඳුදා"):
            outputList.append(44)
        elif(ele == "අඟහ"):
            outputList.append(45)
        elif(ele == "බදාදා"):
            outputList.append(46)
        elif(ele == "බ්‍රහස්"):
            outputList.append(47)
        elif(ele == "සිකු"):
            outputList.append(48)
        elif(ele == "සෙන"):
            outputList.append(49)
#             ------------------
        elif(ele == "මැදියම"):
            outputList.append(50)
        elif(ele == "දහවල්"):
            outputList.append(51)
        elif(ele == "පාන්දර" or ele == "උදේ"):
            outputList.append(52)
        elif(ele == "දවල්"):
            outputList.append(53)
        elif(ele == "හවස" or ele == "සවස"):
            outputList.append(54)
        elif(ele == "රෑ"):
            outputList.append(55)
#             -----------------
        elif(ele == "පොදු යුගයට පෙර"):
            outputList.append(56)
        elif(ele == "පොදු යුගය"):
            outputList.append(57)
        elif(ele == "ක්‍රි.පූ" or ele == "ක්‍රිපූ"):
            outputList.append(58)
        elif(ele == "පො.පෙ" or ele == "පොපෙ"):
            outputList.append(59)
        elif(ele == "ක්‍රි.ව" or ele == "ක්‍රිව"):
            outputList.append(60)
        elif(ele == "පො.යු" or ele == "පොයු"):
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
        elif(ele[-2:] == ('වන')):
            outputList[0] = outputList[0][:-2]
            outputList.append(62)
#             print(outputList[0][:-2])
        elif(ele[-4:] == ('වනදා')):
            outputList[0] = outputList[0][:-4]
            outputList.append(62)
#             print(outputList[0][:-4])
        else:
#             print(ele.decode('utf8')[-4:])
#             print(ele.decode('utf8')[-4:] == ('වනදා').decode('utf8'))
            outputList.append(0)
        resultList.append(outputList)
    resultList.append(2)
    return resultList


# In[28]:

#
#resu = matcher('2016-02-08 පෙ.ව. 11:34 සිකුරාදා')
#print(resu)
#for i in resu:
#    if(isinstance(i, list)):
#        print(str(i[0]) + " " + str(i[1]))
#
#
## In[29]:
#
#
#resul = (matcher('2014 ජනවාරි 05වනදා  සිකුරාදා පෙ.ව. 10:30'))
#print(resul)
#for i in resul:
#    if(isinstance(i, list)):
#        a = ''
#        print(str(i[0]) + " " + str(i[1]))
#
#
## In[30]:
#
#
#resul = (matcher('2014 ජනවාරි 05වනදා  ඉරිදා පෙ.ව. 10:30'))
#print(resul)
#for i in resul:
#    if(isinstance(i, list)):
#        print(str(i[0]) + " " + str(i[1]))
#
#
## In[31]:
#
#
#resul = (matcher('05වනදා ඉරිදා පෙ.ව. 10:30'))
#print(resul)
#for i in resul:
#    if(isinstance(i, list)):
#        print(str(i[0]) + " " + str(i[1]))
#
#
## In[32]:
#
#
#resul = (matcher('2014 ජනවාරි පෙ.ව. 10:30'))
#print(resul)
#for i in resul:
#    if(isinstance(i, list)):
#        print(str(i[0]) + " " + str(i[1]))
#
#
## In[33]:
#
#
#resul = (matcher('පෙ.ව. 10:30'))
#print(resul)
#for i in resul:
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
## In[34]:
#
#
#resul = (matcher('පෙ.ව. 10:30'))
#print(resul)
#for i in resul:
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
