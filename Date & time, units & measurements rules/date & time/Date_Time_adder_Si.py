#!/usr/bin/env python
# coding: utf-8

# In[143]:


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


# In[199]:


def formatterSi(inputRowList):
    inputList = inputRowList[:-1]
    sender = inputRowList[-1]
    returnData = ""
    returnList = []
    newList = []
    for ele in inputList:
        if(not (ele[0] == 'of' or ele[0] == 'திகதி' or ele[0] == '')):
            newList.append([str(ele[0]), int(ele[1])])
#    print(newList)
    for index, inputEle in enumerate(newList):
        inputData = inputEle[0]
        token = int(inputEle[1])
        checkList = [9, 10, 62]
        datesList = [36, 37, 38, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
        monthsList = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        
        
        if(sender == 1 or sender == 3): # english or tamil
            if(token >=1 and token <= 6):
    #             returnData += ' ' + formatDate(inputData, token)
                returnList.append(' ' + formatDate(inputData, token) + ' ')
            elif(token == 7 or token == 8):
    #             returnData += ' ' + inputData
#                 returnList.append(' ' + inputData + ' ')
                returnList.append(' ')
                returnList.append(' ' + inputData + ' ')
            elif(token == 9):
    #             returnData = " පෙ.ව." + returnData                
                if(sender == 1):
                    if((index - 1)>=0 and (int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8)):
                        returnList.insert(-1, (" පෙ.ව."))
                    else:
                        returnList.append(" පෙ.ව.")
                else:
                    if((index + 1)< len(newList) and (int(newList[index + 1][1]) == 7 or int(newList[index + 1][1]) == 8)):
                        returnList.append((" පෙ.ව."))
                    else:
                        returnList.append(" පෙ.ව.")
            elif(token == 10):
                if(sender == 1):
                    if((index - 1)>= 0 and (int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8)):
                        returnList.insert(-1, (" ප.ව."))
                    else:
                        returnList.append(" ප.ව.")
                else:
                    if((index + 1)< len(newList) and (int(newList[index + 1][1]) == 7 or int(newList[index + 1][1]) == 8)):
                        returnList.append((" ප.ව."))
                    else:
                        returnList.append(" ප.ව.")
    #             returnData = " ප.ව." + returnData
            elif(token == 11):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" ජනවාරි "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ජනවාරි "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" ජනවාරි "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" ජනවාරි "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ජනවාරි "))
                else:
                    returnList.append(" ජනවාරි ")
            elif(token == 12):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" පෙබරවාරි "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" පෙබරවාරි "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" පෙබරවාරි "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" පෙබරවාරි "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" පෙබරවාරි "))
                else:
                    returnList.append(" පෙබරවාරි ")
    #             returnList.append("පෙබරවාරි")
            elif(token == 13):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" මාර්තු "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" මාර්තු "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" මාර්තු "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" මාර්තු "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" මාර්තු "))
                else:
                    returnList.append(" මාර්තු ")
    #             returnList.append("මාර්තු")
            elif(token == 14):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" අප්‍රේල් "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" අප්‍රේල් "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" අප්‍රේල් "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" අප්‍රේල් "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" අප්‍රේල් "))
                else:
                    returnList.append(" අප්‍රේල් ")
    #             returnList.append("අප්‍රේල්")
            elif(token == 15):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" මැයි "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" මැයි "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" මැයි "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" මැයි "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" මැයි "))
                else:
                    returnList.append(" මැයි ")
    #             returnList.append("මැයි")
            elif(token == 16):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" ජූනි "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ජූනි "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" ජූනි "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" ජූනි "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ජූනි "))
                else:
                    returnList.append(" ජූනි ")
    #             returnList.append("ජූනි")
            elif(token == 17):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" ජූලි "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ජූලි "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" ජූලි "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" ජූලි "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ජූලි "))
                else:
                    returnList.append(" ජූලි ")
    #             returnList.append("ජූලි")
            elif(token == 18):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" අගෝස්තු "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" අගෝස්තු "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" අගෝස්තු "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" අගෝස්තු "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" අගෝස්තු "))
                else:
                    returnList.append(" අගෝස්තු ")
    #             returnList.append("අගෝස්තු")
            elif(token == 19):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" සැප්තැම්බර් "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" සැප්තැම්බර් "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" සැප්තැම්බර් "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" සැප්තැම්බර් "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" සැප්තැම්බර් "))
                else:
                    returnList.append(" සැප්තැම්බර් ")
    #             returnList.append("සැප්තැම්බර්")
            elif(token == 20):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" ඔක්තෝබර් "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ඔක්තෝබර් "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" ඔක්තෝබර් "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" ඔක්තෝබර් "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ඔක්තෝබර් "))
                else:
                    returnList.append(" ඔක්තෝබර් ")
    #             returnList.append("ඔක්තෝබර්")
            elif(token == 21):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" නොවැම්බර් "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" නොවැම්බර් "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" නොවැම්බර් "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" නොවැම්බර් "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" නොවැම්බර් "))
                else:
                    returnList.append(" නොවැම්බර් ")
    #             returnList.append("නොවැම්බර්")
            elif(token == 22):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" දෙසැම්බර් "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" දෙසැම්බර් "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" දෙසැම්බර් "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" දෙසැම්බර් "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" දෙසැම්බර් "))
                else:
                    returnList.append(" දෙසැම්බර් ")
    #             returnList.append("දෙසැම්බර්")
            elif(token == 23):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" ජන. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ජන. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" ජන. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" ජන. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ජන. "))
                else:
                    returnList.append(" ජන. ")
    #             returnList.append("ජන.")
            elif(token == 24):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" පෙබ. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" පෙබ. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" පෙබ. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" පෙබ. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" පෙබ. "))
                else:
                    returnList.append(" පෙබ. ")
    #             returnList.append("පෙබ.")
            elif(token == 25):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" මාර්තු. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" මාර්තු. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" මාර්තු. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" මාර්තු. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" මාර්තු. "))
                else:
                    returnList.append(" මාර්තු. ")
    #             returnList.append("මාර්තු.")
            elif(token == 26):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" අප්. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" අප්. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" අප්. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" අප්. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" අප්. "))
                else:
                    returnList.append(" අප්. ")
    #             returnList.append("අප්.")
            elif(token == 27):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" මැයි. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" මැයි. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" මැයි. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" මැයි. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" මැයි. "))
                else:
                    returnList.append(" මැයි. ")
    #             returnList.append("මැයි.")
            elif(token == 28):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" ජූනි. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ජූනි. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" ජූනි. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" ජූනි. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ජූනි. "))
                else:
                    returnList.append(" ජූනි. ")
    #             returnList.append("ජූනි.")
            elif(token == 29):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" ජූලි. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ජූලි. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" ජූලි. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" ජූලි. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ජූලි. "))
                else:
                    returnList.append(" ජූලි. ")
    #             returnList.append("ජූලි.")
            elif(token == 30):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" අගෝ. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" අගෝ. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" අගෝ. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" අගෝ. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" අගෝ. "))
                else:
                    returnList.append(" අගෝ. ")
    #             returnList.append("අගෝ.")
            elif(token == 31):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" සැප්. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" සැප්. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" සැප්. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" සැප්. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" සැප්. "))
                else:
                    returnList.append(" සැප්. ")
    #             returnList.append("සැප්.")
            elif(token == 32):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" ඔක්. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ඔක්. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" ඔක්. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" ඔක්. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ඔක්. "))
                else:
                    returnList.append(" ඔක්. ")
    #             returnList.append("ඔක්.")
            elif(token == 33):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" නොවැ. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" නොවැ. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" නොවැ. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" නොවැ. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" නොවැ. "))
                else:
                    returnList.append(" නොවැ. ")
    #             returnList.append("නොවැ.")
            elif(token == 34):
                if((index-1)>=0 and (newList[index-1][1] in checkList) and (index-2)>=0 and (newList[index-2][1] in datesList) and (index+1)<len(newList) and (newList[index+1][1] == 0)):
                    returnList.insert(-2, (" දෙසැ. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" දෙසැ. "))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and (newList[index-2][1] in datesList)):
                    returnList.insert(-2, (" දෙසැ. "))
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1,(" දෙසැ. "))
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" දෙසැ. "))
                else:
                    returnList.append(" දෙසැ. ")
    #             returnList.append("දෙසැ.")

    # -------------------------------------------------------------

            elif(token == 35):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" කාර්තුව ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" කාර්තුව ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" කාර්තුව ")
                else:
                    returnList.append(" කාර්තුව ")
            elif(token == 36):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ඉරිදා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ඉරිදා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" ඉරිදා ")
                else:
                    returnList.append(" ඉරිදා ")
            elif(token == 37):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සඳුදා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සඳුදා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" සඳුදා ")
                else:
                    returnList.append(" සඳුදා ")
            elif(token == 38):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" අඟහරුවාදා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" අඟහරුවාදා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" අඟහරුවාදා ")
                else:
                    returnList.append(" අඟහරුවාදා ")
            elif(token == 39):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" බදාදා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" බදාදා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" බදාදා ")
                else:
                    returnList.append(" බදාදා ")
            elif(token == 40):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" බ්‍රහස්පතින්දා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" බ්‍රහස්පතින්දා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" බ්‍රහස්පතින්දා ")
                else:
                    returnList.append(" බ්‍රහස්පතින්දා ")
            elif(token == 41):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සිකුරාදා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සිකුරාදා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" සිකුරාදා ")
                else:
                    returnList.append(" සිකුරාදා ")
            elif(token == 42):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සෙනසුරාදා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සෙනසුරාදා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" සෙනසුරාදා ")
                else:
                    returnList.append(" සෙනසුරාදා ")
            elif(token == 43):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ඉරිදා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ඉරිදා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" ඉරිදා ")
                else:
                    returnList.append(" ඉරිදා ")
            elif(token == 44):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සඳුදා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සඳුදා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" සඳුදා ")
                else:
                    returnList.append(" සඳුදා ")
            elif(token == 45):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" අඟහ ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" අඟහ ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" අඟහ ")
                else:
                    returnList.append(" අඟහ ")
            elif(token == 46):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" බදාදා ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" බදාදා ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" බදාදා ")
                else:
                    returnList.append(" බදාදා ")
            elif(token == 47):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" බ්‍රහස් ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" බ්‍රහස් ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" බ්‍රහස් ")
                else:
                    returnList.append(" බ්‍රහස් ")
            elif(token == 48):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සිකු ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සිකු ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" සිකු ")
                else:
                    returnList.append(" සිකු ")
            elif(token == 49):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සෙන ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" සෙන ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" සෙන ")
                else:
                    returnList.append(" සෙන ")
            elif(token == 50):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" මැදියම ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" මැදියම ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" මැදියම ")
                else:
                    returnList.append(" මැදියම ")
            elif(token == 51):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" දහවල් ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" දහවල් ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" දහවල් ")
                else:
                    returnList.append(" දහවල් ")
            elif(token == 52):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පාන්දර ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පාන්දර ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" පාන්දර ")
                else:
                    returnList.append(" පාන්දර ")
            elif(token == 53):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" දවල් ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" දවල් ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" දවල් ")
                else:
                    returnList.append(" දවල් ")
            elif(token == 54):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" හවස ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" හවස ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" හවස ")
                else:
                    returnList.append(" හවස ")
            elif(token == 55):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" රෑ ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" රෑ ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" රෑ ")
                else:
                    returnList.append(" රෑ ")
            elif(token == 56):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පොදු යුගයට පෙර ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පොදු යුගයට පෙර ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" පොදු යුගයට පෙර ")
                else:
                    returnList.append(" පොදු යුගයට පෙර ")
            elif(token == 57):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පොදු යුගය ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පොදු යුගය ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" පොදු යුගය ")
                else:
                    returnList.append(" පොදු යුගය ")
            elif(token == 58):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ක්‍රි.පූ ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ක්‍රි.පූ ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" ක්‍රි.පූ ")
                else:
                    returnList.append(" ක්‍රි.පූ ")
            elif(token == 59):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පො.පෙ ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පො.පෙ ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" පො.පෙ ")
                else:
                    returnList.append(" පො.පෙ ")
            elif(token == 60):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ක්‍රි.ව ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ක්‍රි.ව ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" ක්‍රි.ව ")
                else:
                    returnList.append(" ක්‍රි.ව ")
            elif(token == 61):
                if((index+1)<len(newList) and (index+2)<len(newList) and (index+3)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList) and (newList[index+3][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පො.යු ")
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and(newList[index+2][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" පො.යු ")
                elif((index+1)<len(newList) and (newList[index+1][1] == 62)):
                    returnList.append(' ')
                    returnList.append(" පො.යු ")
                else:
                    returnList.append(" පො.යු ")
            elif(token == 62):
                if((index-1)>=0 and (index+1)<len(newList) and (index+2)<len(newList) and (newList[index+2][1] == 0) and (newList[index+1][1] in monthsList) and (newList[index-1][1] in datesList)):
                    returnList.insert(-1, ((' ' + inputData + "වනදා ")))
                elif((index-1)>=0 and (index+1)<len(newList) and (newList[index-1][1] in datesList) and (newList[index+1][1] in monthsList)):
                    returnList.insert(-1, ((' ' + inputData + "වනදා ")))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] in monthsList) and (newList[index+2][1] == 0)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(((' ' + inputData + "වනදා ")))
                elif((index+1)<len(newList) and (newList[index+1][1] in monthsList)):
                    returnList.append(' ')
                    returnList.append(((' ' + inputData + "වනදා ")))
                elif((index-1)>=0 and (newList[index-1][1] in datesList)):
                    returnList.append((' ' + inputData + "වනදා "))
                else:
                    returnList.append((' ' + inputData + "වනදා "))
            else:
                if(inputData == 'of' or inputData == 'in' or inputData == 'වන' or inputData == 'වැනි'):
                    returnData = returnData
                else:
                    if((index-1)>=0 and (index-2)>=0 and (index-3)>=0 and (newList[index-1][1] in monthsList) and newList[index-2][1] == 62 and (newList[index-3][1] in datesList)):
                        returnList.insert(-3, ((' ' + inputData + " ")))
                    elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] in monthsList) and newList[index-2][1] == 62):
                        returnList.insert(-2, ((' ' + inputData + " ")))
                    elif((index-1)>=0 and (newList[index-1][1] in monthsList)):
                        returnList.insert(-1, ((' ' + inputData + " ")))
                    else:
                        returnList.append(inputData)
        else:
            returnList = ['Error']
#         print(returnList)
    returnList = [ elem for elem in returnList if elem != ' ' ]
    return(returnList)


# In[ ]:


#
#
#
## In[ ]:
#
#
#
#
#
## In[181]:
#
#
#inpu = [['sunday', 36], ['2', 62], ['of', 0], ['january', 11], ['2017', 0], ['10:30', 7], ['a.m.', 9], 1]
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
## In[182]:
#
#
#inpu = [['10:30', 7], ['a.m.', 9], ['sunday', 36], ['2', 62], ['of', 0], ['january', 11], ['2017', 0], ['10:30', 7], ['a.m.', 9], 1]
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
#inpu = [['sunday', 36], ['2', 62], ['of', 0], ['january', 11], 1]
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
#inpu = [['january', 11], ['2017', 0], 1]
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
## In[194]:
#
#
#inpu =[['friday', 41], ['05', 62], ['of', 0], ['january', 11], ['10:30', 7], ['a.m.', 10], 1]
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
## resul = formatter([['2016-02-08','5'], ['11:34','7'], ['a.m.','9'], ['05', 62]])
## # ['சனி','42'],
## # print(resul)
## stri = ''
## for i in resul:
##     stri += (i)
## #     print((i))
## print(stri)
#
#
## In[187]:
#
#
## resul = formatter([['05', 62], ['of', 0], ['january', 11], ['10:30', 7], ['a.m.', 9], ['friday', 41]])
## # print(resul)
## stri = ''
## for i in resul:
##     stri += (i)
## #     print((i))
## print(stri)
#
#
## In[188]:
#
#
#inpu =[['\xe0\xae\xb5\xe0\xaf\x86\xe0\xae\xb3\xe0\xaf\x8d\xe0\xae\xb3\xe0\xae\xbf', 41], [u'05', 62], ['\xe0\xae\x9c\xe0\xae\xa9\xe0\xae\xb5\xe0\xae\xb0\xe0\xae\xbf', 11], ['\xe0\xae\x95\xe0\xae\xbe\xe0\xae\xb2\xe0\xaf\x88', 52], ['10:30', 7], 3]
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
## In[200]:
#
#
#inpu = [['\xe0\xae\xb5\xe0\xaf\x86\xe0\xae\xb3\xe0\xaf\x8d\xe0\xae\xb3\xe0\xae\xbf', 41], [u'05', 62], ['\xe0\xae\x9c\xe0\xae\xa9\xe0\xae\xb5\xe0\xae\xb0\xe0\xae\xbf', 11], ['\xe0\xae\x95\xe0\xae\xbe\xe0\xae\xb2\xe0\xaf\x88', 52], ['10:30', 7], 3]
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
## In[201]:
#
#
#inpu = [['friday', 41], ['05', 62], ['of', 0], ['january', 11], ['10:30', 7], ['a.m.', 9], 3]
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
## In[204]:
#
#
#inpu = [['a.m.', 9], ['10:30', 7], 3]
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
## In[205]:
#
#
#inpu = [['\xe0\xae\xb5\xe0\xaf\x86\xe0\xae\xb3\xe0\xaf\x8d\xe0\xae\xb3\xe0\xae\xbf', 41], [u'05', 62], ['10:30', 7], ['\xe0\xae\x9c\xe0\xae\xa9\xe0\xae\xb5\xe0\xae\xb0\xe0\xae\xbf', 11], ['\xe0\xae\xae\xe0\xaf\x81\xe0\xae\xb1\xe0\xaf\x8d\xe0\xae\xaa\xe0\xae\x95\xe0\xae\xb2\xe0\xaf\x8d', 9], 3]
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
## In[207]:
#
#
#inpu = [['\xe0\xae\xae\xe0\xaf\x81\xe0\xae\xb1\xe0\xaf\x8d\xe0\xae\xaa\xe0\xae\x95\xe0\xae\xb2\xe0\xaf\x8d', 9], ['10:30', 7], 3]
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
## In[208]:
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
## In[209]:
#
#
#inpu = [['10:30', 7], ['a.m.', 9], 1]
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
## In[210]:
#
#
#inpu = [['14/12/2018', 2], 1]
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
## In[211]:
#
#
#inpu = [['14/12/2018', 2], 1]
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
## In[212]:
#
#
#inpu = [['\xe0\xae\x95\xe0\xae\xbe\xe0\xae\xb2\xe0\xaf\x88', 52], ['11:50', 7], 3]
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
## In[213]:
#
#
#inpu = [['10:30', 7], ['a.m.', 9], 1]
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
## In[214]:
#
#
#inpu = [['sunday', 36], ['2', 62], ['of', 0], ['january', 11], ['2017', 0], ['10:30', 7], ['a.m.', 9], 1]
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
## In[215]:
#
#
#inpu = [['10:30', 7], ['a.m.', 9], 1]
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
## In[216]:
#
#
#inpu = [['14/12/2018', 2], 1]
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
