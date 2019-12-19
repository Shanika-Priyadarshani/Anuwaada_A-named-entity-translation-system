#!/usr/bin/env python
# coding: utf-8

# In[175]:


def formatDate(inputDate, token):
    splittedList = []
    splitter = ""
    returnDate = ""
    if(token == 1 or token == 2):
        splittedList = inputDate.split("/")
        splitter = "/"
    elif(token == 3 or token == 4):
        splittedList = inputDate.split(".")
        splitter = "."
    else:
        splittedList = inputDate.split("-")
        splitter = "-"
    if(token%2 == 0):
        returnDate = splittedList[2] + splitter + splittedList[1] + splitter + splittedList[0]
    else:
        returnDate = splittedList[0] + splitter + splittedList[1] + splitter + splittedList[2]
    return returnDate


# In[176]:


def formatterEn(inputRowList):
    inputList = inputRowList[:-1]
    sender = inputRowList[-1]
    returnData = ""
    returnList = []
    newList = []
    for ele in inputList:
        if(not(ele[0] == 'of' or ele[0] == 'திகதி' or ele[0] == '')):
            newList.append([str(ele[0]), int(ele[1])])
#    print('----')
#    print(newList)
    for index, inputEle in enumerate(newList):
        inputData = inputEle[0]
        token = int(inputEle[1])
        checkList = [9, 10, 62]
        datesList = [36, 37, 38, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
        monthsList = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        
        if(sender == 2): # sinhala    
            if(token >=1 and token <= 6):
                returnList.append(' ' + formatDate(inputData, token) + ' ')
            elif(token == 7 or token == 8):
                if((index-1)>=0 and (newList[index-1][1] == 9 or newList[index-1][1] == 10)):
                    returnList.insert(-1,(' ' + inputData + ' '))
                else:
                    returnList.append(' ' + inputData + ' ')
            elif(token == 9):
                if((index+1) < len(newList) and (newList[index+1][1] == 7 or newList[index+1][1] == 8)):
                    returnList.append(' ')
                    returnList.append("a.m.")
                else:
                    returnList.append("a.m.")
            elif(token == 10):
                if((index+1) < len(newList) and (newList[index+1][1] == 7 or newList[index+1][1] == 8)):
                    returnList.append(' ')
                    returnList.append("p.m.")
                else:
                    returnList.append("p.m.")
            elif(token == 11):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" january "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" january "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" january ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" january "))
                else:
                    returnList.append(" january ")
            elif(token == 12):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" february "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" february "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" february ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" february "))
                else:
                    returnList.append(" february ")
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" february")
#                 else:
#                     returnList.append(" february")
            elif(token == 13):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" march "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" march "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" march ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" march "))
                else:
                    returnList.append(" march ")
#     #             returnData += " march"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" march")
#                 else:
#                     returnList.append(" march")
            elif(token == 14):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" april "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" april "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" april ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" april "))
                else:
                    returnList.append(" april ")
#     #             returnData += " april"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" april")
#                 else:
#                     returnList.append(" april")
            elif(token == 15):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" may "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" may "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" may ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" may "))
                else:
                    returnList.append(" may ")
#     #             returnData += " may"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" may")
#                 else:
#                     returnList.append(" may")
            elif(token == 16):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" june "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" june "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" june ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" june "))
                else:
                    returnList.append(" june ")
#     #             returnData += " june"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" june")
#                 else:
#                     returnList.append(" june")
            elif(token == 17):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" july "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" july "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" july ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" july "))
                else:
                    returnList.append(" july ")
#     #             returnData += " july"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" july")
#                 else:
#                     returnList.append(" july")
            elif(token == 18):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" august "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" august "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" august ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" august "))
                else:
                    returnList.append(" august ")
#     #             returnData += " august"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" august")
#                 else:
#                     returnList.append(" august")
            elif(token == 19):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" september "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" september "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" september ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" september "))
                else:
                    returnList.append(" september ")
#     #             returnData += " september"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" september")
#                 else:
#                     returnList.append(" september")
            elif(token == 20):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" october "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" october "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" october ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" october "))
                else:
                    returnList.append(" october ")
#     #             returnData += " october"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" october")
#                 else:
#                     returnList.append(" october")
            elif(token == 21):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" november "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" november "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" november ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" november "))
                else:
                    returnList.append(" november ")
#     #             returnData += " november"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" november")
#                 else:
#                     returnList.append(" november")
            elif(token == 22):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" december "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" december "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" december ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" december "))
                else:
                    returnList.append(" december ")
#     #             returnData += " december"
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" december")
#                 else:
#                     returnList.append(" december")
            elif(token == 23):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" jan. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" jan. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" jan. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" jan. "))
                else:
                    returnList.append(" jan. ")
#     #             returnData += " jan."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" jan.")
#                 else:
#                     returnList.append(" jan.")
            elif(token == 24):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" feb. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" feb. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" feb. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" feb. "))
                else:
                    returnList.append(" feb. ")
#     #             returnData += " feb."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" feb.")
#                 else:
#                     returnList.append(" feb.")
            elif(token == 25):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" mar. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" mar. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" mar. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" mar. "))
                else:
                    returnList.append(" mar. ")
#     #             returnData += " mar."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" mar.")
#                 else:
#                     returnList.append(" mar.")
            elif(token == 26):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" apr. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" apr. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" apr. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" apr. "))
                else:
                    returnList.append(" apr. ")
#     #             returnData += " apr."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" apr.")
#                 else:
#                     returnList.append(" apr.")
            elif(token == 27):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" may. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" may. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" may. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" may. "))
                else:
                    returnList.append(" may. ")
#     #             returnData += " may."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" may.")
#                 else:
#                     returnList.append(" may.")
            elif(token == 28):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" jun. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" jun. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" jun. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" jun. "))
                else:
                    returnList.append(" jun. ")
#     #             returnData += " jun."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" jun.")
#                 else:
#                     returnList.append(" jun.")
            elif(token == 29):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" jul. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" jul. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" jul. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" jul. "))
                else:
                    returnList.append(" jul. ")
#     #             returnData += " jul."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" jul.")
#                 else:
#                     returnList.append(" jul.")
            elif(token == 30):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" aug. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" aug. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" aug. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" aug. "))
                else:
                    returnList.append(" aug. ")
#     #             returnData += " aug."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" aug.")
#                 else:
#                     returnList.append(" aug.")
            elif(token == 31):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" sep. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" sep. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" sep. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" sep. "))
                else:
                    returnList.append(" sep. ")
#     #             returnData += " sep."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" sep.")
#                 else:
#                     returnList.append(" sep.")
            elif(token == 32):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" oct. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" oct. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" oct. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" oct. "))
                else:
                    returnList.append(" oct. ")
#     #             returnData += " oct."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" oct.")
#                 else:
#                     returnList.append(" oct.")
            elif(token == 33):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" nov. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" nov. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" nov. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" nov. "))
                else:
                    returnList.append(" nov. ")
#     #             returnData += " nov."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" nov.")
#                 else:
#                     returnList.append(" nov.")
            elif(token == 34):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" dec. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" dec. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" dec. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" dec. "))
                else:
                    returnList.append(" dec. ")
#     #             returnData += " dec."
#                 if((index+1)<=len(newList) and (newList[index+1][1] == 62)):
#                     returnList.append(' ')
#                     returnList.append(" dec.")
#                 else:
#                     returnList.append(" dec.")
            elif(token == 35):
    #             returnData += " quarter"
                returnList.append(" quarter")
        
            elif(token == 36):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " sunday")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " sunday")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " sunday")
                else:
                    returnList.append(" sunday")
            elif(token == 37):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " monday ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " monday ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " monday ")
                else:
                    returnList.append(" monday ")
    #             returnData += " monday"
#                 returnList.append(" monday")
            elif(token == 38):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " tuesday ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " tuesday ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " tuesday ")
                else:
                    returnList.append(" tuesday ")
    #             returnData += " tuesday"
#                 returnList.append(" tuesday")
            elif(token == 39):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " wednesday ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " wednesday ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " wednesday ")
                else:
                    returnList.append(" wednesday ")
    #             returnData += " wednesday"
#                 returnList.append(" wednesday")
            elif(token == 40):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " thursday ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " thursday ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " thursday ")
                else:
                    returnList.append(" thursday ")
    #             returnData += " thursday"
#                 returnList.append(" thursday")
            elif(token == 41):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " friday ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " friday ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " friday ")
                else:
                    returnList.append(" friday ")
    #             returnData += " friday"
#                 returnList.append(" friday")
            elif(token == 42):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " saturday ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " saturday ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " saturday ")
                else:
                    returnList.append(" saturday ")
    #             returnData += " saturday"
#                 returnList.append(" saturday")
            elif(token == 43):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " sun ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " sun ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " sun ")
                else:
                    returnList.append(" sun ")
    #             returnData += " sun"
#                 returnList.append(" sun")
            elif(token == 44):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " mon ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " mon ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " mon ")
                else:
                    returnList.append(" mon ")
    #             returnData += " mon"
#                 returnList.append(" mon")
            elif(token == 45):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " tue ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " tue ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " tue ")
                else:
                    returnList.append(" tue ")
    #             returnData += " tue"
#                 returnList.append(" tue")
            elif(token == 46):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " wed ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " wed ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " wed ")
                else:
                    returnList.append(" wed ")
    #             returnData += " wed"
#                 returnList.append(" wed")
            elif(token == 47):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " thu ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " thu ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " thu ")
                else:
                    returnList.append(" thu ")
    #             returnData += " thu"
#                 returnList.append(" thu")
            elif(token == 48):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " fri ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " fri ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " fri ")
                else:
                    returnList.append(" fri ")
    #             returnData += " fri"
#                 returnList.append(" fri")
            elif(token == 49):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " sat ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " sat ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " sat ")
                else:
                    returnList.append(" sat ")
    #             returnData += " sat"
#                 returnList.append(" sat")
            elif(token == 50):
    #             returnData += " midnight"
                returnList.append(" midnight")
            elif(token == 51):
    #             returnData += " noon"
                returnList.append(" noon")
            elif(token == 52):
    #             returnData += " in the morning"
                returnList.append(" in the morning")
            elif(token == 53):
    #             returnData += " in the afternoon"
                returnList.append(" in the afternoon")
            elif(token == 54):
    #             returnData += " in the evening"
                returnList.append(" in the evening")
            elif(token == 55):
    #             returnData += " at night"
                returnList.append(" at night")
            elif(token == 56):
    #             returnData += " before common era"
                returnList.append(" before common era")
            elif(token == 57):
    #             returnData += " common era"
                returnList.append(" common era")
            elif(token == 58):
    #             returnData += " bc"
                returnList.append(" bc")
            elif(token == 59):
    #             returnData += " bce"
                returnList.append(" bce")
            elif(token == 60):
    #             returnData += " ad"
                returnList.append(" ad")
            elif(token == 61):
    #             returnData += " ce"
                returnList.append(" ce")
            elif(token == 62):
                ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
                if((index-1)>=0 and (index-2)>=0 and (index+1)<len(newList) and (newList[index-2][1] == 0) and (newList[index-1][1] in monthsList) and (newList[index+1][1] in datesList)):
                    returnList.insert(-2, (' ' + ordinal(int(inputData)) + ' of'))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-2][1] == 0) and (newList[index-1][1] in monthsList)):
                    returnList.insert(-2, (' ' + ordinal(int(inputData)) + ' of'))
                elif((index-1)>=0 and (index+1)>=0 and (newList[index+1][1] in datesList) and (newList[index-1][1] in monthsList)):
                    returnList.insert(-1, (' ' + ordinal(int(inputData)) + ' of'))
                elif((index-1)>=0 and (newList[index-1][1] in monthsList)):
                    returnList.insert(-1, (' ' + ordinal(int(inputData)) + ' of'))
                elif((index+1)<len(newList) and (newList[index+1][1] in datesList)):
                    returnList.append((' ' + ordinal(int(inputData)) + ' '))
                else:
                    returnList.append((' ' + ordinal(int(inputData)) + ' '))
            else:
                if(inputData == 'of' or inputData == 'in' or inputData == 'වන' or inputData == 'වැනි'):
                    returnData = returnData
                elif((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] in monthsList) and (newList[index+2][1]==62) and (newList[index+3][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(inputData)
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] in monthsList) and (newList[index+2][1]==62)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(inputData)
                elif((index+1)<len(newList) and (newList[index+1][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(inputData)
                else:
                    returnList.append(inputData)
        
#         ----------------------------------------------------------------------------------------------------
        
        elif(sender == 3): #tamil
            if(token >=1 and token <= 6):
                returnList.append(' ' + formatDate(inputData, token) + ' ')
            elif(token == 7 or token == 8):
                if((index-1)>=0 and (newList[index-1][1] == 9 or newList[index-1][1] == 10)):
                    returnList.insert(-1,(' ' + inputData + ' '))
                else:
                    returnList.append(' ' + inputData + ' ')
            elif(token == 9):
                if((index+1) < len(newList) and (newList[index+1][1] == 7 or newList[index+1][1] == 8)):
                    returnList.append(' ')
                    returnList.append("a.m.")
                else:
                    returnList.append("a.m.")
            elif(token == 10):
                if((index+1) < len(newList) and (newList[index+1][1] == 7 or newList[index+1][1] == 8)):
                    returnList.append(' ')
                    returnList.append("p.m.")
                else:
                    returnList.append("p.m.")
            elif(token == 11):
#                 if((index+1)<len(newList) and (index-1)>=0 and (index-2)<len(newList) and (newList[index+1][1] == 0) and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
#                     returnList.append((" january "))
#                 elif((index-1)<len(newList) and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
#                     returnList.append((" january "))
#                 elif((index-1)<len(newList) and (index+1)<len(newList) and (newList[index-1][1] == 62) and (newList[index+1][1] == 0)):
#                     returnList.append(" january ")
#                 elif((index-1)>=0 and (newList[index-1][1] == 62)):
#                     returnList.append((" january "))
#                 else:
#                     returnList.append(" january ")
                returnList.append(" january ")
    #             returnData += " january"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" january"))
#                 else:
#                     returnList.append(" january")
            elif(token == 12):
                returnList.append(" february ")
    #             returnData += " february"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" february"))
#                 else:
#                     returnList.append(" february")
            elif(token == 13):
                returnList.append(" march ")
#     #             returnData += " march"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" march"))
#                 else:
#                     returnList.append(" march")
            elif(token == 14):
                returnList.append(" april ")
#     #             returnData += " april"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" april"))
#                 else:
#                     returnList.append(" april")
            elif(token == 15):
                returnList.append(" may ")
#     #             returnData += " may"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" may"))
#                 else:
#                     returnList.append(" may")
            elif(token == 16):
                returnList.append(" june ")
#     #             returnData += " june"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" june"))
#                 else:
#                     returnList.append(" june")
            elif(token == 17):
                returnList.append(" july ")
#     #             returnData += " july"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" july"))
#                 else:
#                     returnList.append(" july")
            elif(token == 18):
                returnList.append(" august ")
#     #             returnData += " august"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" august"))
#                 else:
#                     returnList.append(" august")
            elif(token == 19):
                returnList.append(" september ")
#     #             returnData += " september"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" september"))
#                 else:
#                     returnList.append(" september")
            elif(token == 20):
                returnList.append(" october ")
#     #             returnData += " october"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" october"))
#                 else:
#                     returnList.append(" october")
            elif(token == 21):
                returnList.append(" november ")
#     #             returnData += " november"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" november"))
#                 else:
#                     returnList.append(" november")
            elif(token == 22):
                returnList.append(" december ")
#     #             returnData += " december"
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" december"))
#                 else:
#                     returnList.append(" december")
            elif(token == 23):
                returnList.append(" jan. ")
#     #             returnData += " jan."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" jan."))
#                 else:
#                     returnList.append(" jan.")
            elif(token == 24):
                returnList.append(" feb. ")
#     #             returnData += " feb."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" feb."))
#                 else:
#                     returnList.append(" feb.")
            elif(token == 25):
                returnList.append(" mar. ")
#     #             returnData += " mar."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" mar."))
#                 else:
#                     returnList.append(" mar.")
            elif(token == 26):
                returnList.append(" apr. ")
#     #             returnData += " apr."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" apr."))
#                 else:
#                     returnList.append(" apr.")
            elif(token == 27):
                returnList.append(" may. ")
#     #             returnData += " may."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" may."))
#                 else:
#                     returnList.append(" may.")
            elif(token == 28):
                returnList.append(" jun. ")
#     #             returnData += " jun."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" jun."))
#                 else:
#                     returnList.append(" jun.")
            elif(token == 29):
                returnList.append(" jul. ")
#     #             returnData += " jul."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" jul."))
#                 else:
#                     returnList.append(" jul.")
            elif(token == 30):
                returnList.append(" aug. ")
#     #             returnData += " aug."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" aug."))
#                 else:
#                     returnList.append(" aug.")
            elif(token == 31):
                returnList.append(" sep. ")
#     #             returnData += " sep."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" sep."))
#                 else:
#                     returnList.append(" sep.")
            elif(token == 32):
                returnList.append(" oct. ")
#     #             returnData += " oct."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" oct."))
#                 else:
#                     returnList.append(" oct.")
            elif(token == 33):
                returnList.append(" nov. ")
#     #             returnData += " nov."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" nov."))
#                 else:
#                     returnList.append(" nov.")
            elif(token == 34):
                returnList.append(" dec. ")
#     #             returnData += " dec."
#                 if((index-1)>=0 and (newList[index-1][1] in checkList)):
#                     returnList.insert(-1, (" dec."))
#                 else:
#                     returnList.append(" dec.")
            elif(token == 35):
    #             returnData += " quarter"
                returnList.append(" quarter")
            elif(token == 36):
    #             returnData += " sunday"
                if((index-1)>=0 and (index-2)>=0 and (newList[index-1] in checkList) and (newList[index-2] in monthsList)):
                    returnList.insert(-3, " sunday")
                elif((index-1)>=0 and (newList[index-1] in checkList)):
                    returnList.insert(-2, " sunday")
                else:
                    returnList.append(" sunday")
            elif(token == 37):
    #             returnData += " monday"
                returnList.append(" monday")
            elif(token == 38):
    #             returnData += " tuesday"
                returnList.append(" tuesday")
            elif(token == 39):
    #             returnData += " wednesday"
                returnList.append(" wednesday")
            elif(token == 40):
    #             returnData += " thursday"
                returnList.append(" thursday")
            elif(token == 41):
    #             returnData += " friday"
                returnList.append(" friday")
            elif(token == 42):
    #             returnData += " saturday"
                returnList.append(" saturday")
            elif(token == 43):
    #             returnData += " sun"
                returnList.append(" sun")
            elif(token == 44):
    #             returnData += " mon"
                returnList.append(" mon")
            elif(token == 45):
    #             returnData += " tue"
                returnList.append(" tue")
            elif(token == 46):
    #             returnData += " wed"
                returnList.append(" wed")
            elif(token == 47):
    #             returnData += " thu"
                returnList.append(" thu")
            elif(token == 48):
    #             returnData += " fri"
                returnList.append(" fri")
            elif(token == 49):
    #             returnData += " sat"
                returnList.append(" sat")
            elif(token == 50):
    #             returnData += " midnight"
                returnList.append(" midnight")
            elif(token == 51):
    #             returnData += " noon"
                returnList.append(" noon")
            elif(token == 52):
    #             returnData += " in the morning"
                returnList.append(" in the morning")
            elif(token == 53):
    #             returnData += " in the afternoon"
                returnList.append(" in the afternoon")
            elif(token == 54):
    #             returnData += " in the evening"
                returnList.append(" in the evening")
            elif(token == 55):
    #             returnData += " at night"
                returnList.append(" at night")
            elif(token == 56):
    #             returnData += " before common era"
                returnList.append(" before common era")
            elif(token == 57):
    #             returnData += " common era"
                returnList.append(" common era")
            elif(token == 58):
    #             returnData += " bc"
                returnList.append(" bc")
            elif(token == 59):
    #             returnData += " bce"
                returnList.append(" bce")
            elif(token == 60):
    #             returnData += " ad"
                returnList.append(" ad")
            elif(token == 61):
    #             returnData += " ce"
                returnList.append(" ce")
        #         -------------
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
        #     elif(token == ):
        #         returnData = ""
            elif(token == 62):
                ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
                returnList.append((' ' + ordinal(int(inputData)) + ' of '))
#                 returnList.append(' ' + (inputData) + '')
            else:
                returnList.append(inputData)
#                 if(inputData == 'of' or inputData == 'in' or inputData == 'වන' or inputData == 'වැනි'):
#                     returnData = returnData
#                 else:
#                     returnList.append(inputData)
    #         print(returnList)
#     ------------------------------------------------------------------------------------------------------
        else:
            returnList = ['Error']
    returnList = [ elem for elem in returnList if elem != ' ' ]
    return returnList


# In[ ]:



#
#
## In[182]:
#
#
#inpu = [['2014', 0], ['\xe0\xb6\xa2\xe0\xb6\xb1\xe0\xb7\x80\xe0\xb7\x8f\xe0\xb6\xbb\xe0\xb7\x92', 11], [u'05', 62], ['', 0], ['\xe0\xb6\x89\xe0\xb6\xbb\xe0\xb7\x92\xe0\xb6\xaf\xe0\xb7\x8f', 36], ['\xe0\xb6\xb4\xe0\xb7\x99.\xe0\xb7\x80.', 9], ['10:30', 7], 2]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[183]:
#
#
#inpu = [['\xe0\xb6\xb4\xe0\xb7\x99.\xe0\xb7\x80.', 9], ['10:30', 7], ['2014', 0], ['\xe0\xb6\xa2\xe0\xb6\xb1\xe0\xb7\x80\xe0\xb7\x8f\xe0\xb6\xbb\xe0\xb7\x92', 11], [u'05', 62], ['', 0], ['\xe0\xb6\xb4\xe0\xb7\x99.\xe0\xb7\x80.', 9], ['10:30', 7], 2]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[184]:
#
#
#inpu = [['\xe0\xb6\xa2\xe0\xb6\xb1\xe0\xb7\x80\xe0\xb7\x8f\xe0\xb6\xbb\xe0\xb7\x92', 11], [u'05', 62], ['', 0], ['\xe0\xb6\x89\xe0\xb6\xbb\xe0\xb7\x92\xe0\xb6\xaf\xe0\xb7\x8f', 36], ['\xe0\xb6\xb4\xe0\xb7\x99.\xe0\xb7\x80.', 9], ['10:30', 7], 2]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[185]:
#
#
#inpu = [['\xe0\xb6\xb4\xe0\xb7\x99.\xe0\xb7\x80.', 9], ['10:30', 7], [u'05', 62], ['\xe0\xb6\x89\xe0\xb6\xbb\xe0\xb7\x92\xe0\xb6\xaf\xe0\xb7\x8f', 36], ['\xe0\xb6\xb4\xe0\xb7\x99.\xe0\xb7\x80.', 9], ['10:30', 7], 2]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[186]:
#
#
#inpu = [['2014', 0], ['\xe0\xb6\xa2\xe0\xb6\xb1\xe0\xb7\x80\xe0\xb7\x8f\xe0\xb6\xbb\xe0\xb7\x92', 11], 2]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[187]:
#
#
#inpu = [['\xe0\xb6\xb4\xe0\xb7\x99.\xe0\xb7\x80.', 9], ['10:30', 7], 2]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[ ]:
#
#
#
#
#
## In[188]:
#
#
## ---------------------------------------------------------------------------------------------------------------
#
#
## In[ ]:
#
#
#
#
#
## In[189]:
#
#
#inpu = [['\xe0\xae\xb5\xe0\xaf\x86\xe0\xae\xb3\xe0\xaf\x8d\xe0\xae\xb3\xe0\xae\xbf', 41], [u'05', 62], ['\xe0\xae\x9c\xe0\xae\xa9\xe0\xae\xb5\xe0\xae\xb0\xe0\xae\xbf', 11], ['\xe0\xae\xae\xe0\xaf\x81\xe0\xae\xb1\xe0\xaf\x8d\xe0\xae\xaa\xe0\xae\x95\xe0\xae\xb2\xe0\xaf\x8d', 9], ['10:30', 7], 3]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
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
